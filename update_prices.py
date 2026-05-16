"""
update_prices.py
Hämtar aktuellt månadsmedel för Nord Pool SE3 spotpris och uppdaterar
den hårdkodade elSpot-datan i sjovagen22.html.

Körs dagligen av GitHub Actions. Skriver bara till filen om data faktiskt
ändrats, så commits inte skapas i onödan.
"""

import json
import re
import sys
from datetime import datetime, timezone
import requests

# ── Konfiguration ─────────────────────────────────────────────
HTML_FILE   = "sjovagen22.html"
SE3_AREA    = "SE3"

# Nord Pool öppen API — day-ahead månadsmedel
# Docs: https://data.nordpoolgroup.com
NORDPOOL_URL = (
    "https://data.nordpoolgroup.com/api/v1/auction/prices/areas"
    "?deliveryDate=latest&currency=SEK"
    "&aggregation=Monthly&deliveryAreas=SE3"
)

# Pelletsförbundet har inget öppet API — pelletspriset uppdateras
# manuellt den 15:e varje månad via inmatning i HTML-filen (se README).
# Detta script hanterar bara elpriset automatiskt.

# ── Hjälpfunktioner ───────────────────────────────────────────

def fetch_spot_price() -> tuple[int, int, float] | None:
    """
    Hämtar senaste tillgängliga månadsmedelpris för SE3 från Nord Pool.
    Returnerar (år, månad_0-indexerad, pris_ore_per_kwh) eller None vid fel.
    """
    try:
        resp = requests.get(NORDPOOL_URL, timeout=15,
                            headers={"Accept": "application/json"})
        resp.raise_for_status()
        data = resp.json()

        # Svaret varierar — försök navigera till prisvärdet
        # Struktur: { "multiAreaEntries": [ { "deliveryStart": "...", "entryPerArea": {"SE3": X} } ] }
        entries = data.get("multiAreaEntries") or data.get("data") or []
        if not entries:
            print("Nord Pool: tomt svar", data)
            return None

        latest = entries[-1]
        delivery = latest.get("deliveryStart") or latest.get("date") or ""
        price_eur_mwh = (
            latest.get("entryPerArea", {}).get(SE3_AREA)
            or latest.get(SE3_AREA)
        )

        if price_eur_mwh is None:
            print("Nord Pool: hittade inte SE3-priset i svaret:", latest)
            return None

        # Hämta SEK/EUR-kurs från ECB (gratis, ingen nyckel)
        ecb = requests.get(
            "https://api.frankfurter.app/latest?from=EUR&to=SEK",
            timeout=10
        )
        ecb.raise_for_status()
        sek_per_eur = ecb.json()["rates"]["SEK"]

        # EUR/MWh → öre/kWh: × sek_per_eur / 10
        price_ore_kwh = round(float(price_eur_mwh) * sek_per_eur / 10, 1)

        # Datum för leveransmånaden
        if delivery:
            dt = datetime.fromisoformat(delivery.replace("Z", "+00:00"))
        else:
            dt = datetime.now(tz=timezone.utc)

        year  = dt.year
        month = dt.month - 1  # 0-indexerad

        print(f"Nord Pool SE3: {price_ore_kwh} öre/kWh  ({year}-{month+1:02d})")
        return year, month, price_ore_kwh

    except Exception as exc:
        print(f"Fel vid hämtning av Nord Pool-data: {exc}")
        return None


def update_html(year: int, month: int, price: float) -> bool:
    """
    Letar upp elSpot-objektet i HTML-filen och uppdaterar rätt år/månad.
    Returnerar True om filen faktiskt ändrades.
    """
    with open(HTML_FILE, encoding="utf-8") as f:
        content = f.read()

    original = content

    year_str = str(year)

    # Hitta raden för aktuellt år: '2026':[val,val,...] eller "2026":[...]
    pattern = re.compile(
        r"(['\"]" + re.escape(year_str) + r"['\"]:\[)([^\]]+)(\])",
        re.DOTALL
    )

    match = pattern.search(content)
    if not match:
        # Året finns inte ännu — lägg till det sist i elSpot-objektet
        # Hitta sista raden i elSpot och infoga efter den
        insert_after = re.compile(
            r"(const elSpot=\{.*?)'(\d{4})':\[([^\]]+)\](\s*\})",
            re.DOTALL
        )
        m2 = insert_after.search(content)
        if m2:
            new_row = ",'" + year_str + "':[" + ",".join(
                [str(round(price, 1)) if i == month else "null" for i in range(12)]
            ) + "]"
            content = content[:m2.end(3)+1] + new_row + content[m2.end(3)+1:]
        else:
            print("Kunde inte infoga nytt år i elSpot — kontrollera HTML-strukturen.")
            return False
    else:
        # Pars befintliga värden
        values_str = match.group(2)
        values = [v.strip() for v in values_str.split(",")]

        # Säkerställ att listan har 12 element
        while len(values) < 12:
            values.append("null")

        # Uppdatera aktuell månad
        values[month] = str(round(price, 1))

        new_row = match.group(1) + ",".join(values) + match.group(3)
        content = content[:match.start()] + new_row + content[match.end():]

    if content == original:
        print("Ingen förändring — hoppar över skrivning.")
        return False

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"sjovagen22.html uppdaterad: elSpot['{year_str}'][{month}] = {price}")
    return True


# ── Main ──────────────────────────────────────────────────────

def main():
    result = fetch_spot_price()
    if result is None:
        print("Ingen data hämtad — filen lämnas oförändrad.")
        sys.exit(0)   # Inte fel, bara ingen uppdatering

    year, month, price = result
    changed = update_html(year, month, price)

    if changed:
        print("Klar — filen uppdaterad och redo för commit.")
    else:
        print("Klar — ingen förändring, ingen commit behövs.")


if __name__ == "__main__":
    main()
