"""
update_pellets.py
Läser pellets_data.json och injicerar uppdaterad diagramdata i pellets.html.
Körs av GitHub Actions vid varje push som ändrar pellets_data.json.
"""

import json
import re
import sys
from collections import defaultdict
from datetime import datetime

DATA_FILE = "pellets_data.json"
HTML_FILE = "pellets.html"

def load_data():
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)

def build_chart_data(leveranser):
    """
    Bygger månadsvis förbruknings- och kostnadsdata ur leveranslistan.
    Returnerar sorterade listor för Chart.js.
    """
    by_month = defaultdict(lambda: {"ton": 0.0, "kr": 0.0, "leveranser": []})

    for lev in leveranser:
        dt = datetime.fromisoformat(lev["datum"])
        key = f"{dt.year}-{dt.month:02d}"
        ton = float(lev["ton"])
        kr_ton = float(lev["kr_per_ton"])
        by_month[key]["ton"] += ton
        by_month[key]["kr"] += ton * kr_ton
        by_month[key]["leveranser"].append(lev)

    sorted_keys = sorted(by_month.keys())
    labels = sorted_keys
    ton_data = [round(by_month[k]["ton"], 2) for k in sorted_keys]
    kr_data = [round(by_month[k]["kr"], 0) for k in sorted_keys]
    kr_per_ton = [
        round(by_month[k]["kr"] / by_month[k]["ton"])
        if by_month[k]["ton"] > 0 else 0
        for k in sorted_keys
    ]

    totalt_ton = round(sum(lev["ton"] for lev in leveranser), 2)
    totalt_kr = round(sum(float(l["ton"]) * float(l["kr_per_ton"]) for l in leveranser), 0)
    snittpris = round(totalt_kr / totalt_ton) if totalt_ton > 0 else 0

    return {
        "labels": labels,
        "ton": ton_data,
        "kr": kr_data,
        "kr_per_ton": kr_per_ton,
        "totalt_ton": totalt_ton,
        "totalt_kr": int(totalt_kr),
        "snittpris": snittpris,
        "antal_leveranser": len(leveranser),
        "senaste_leverans": leveranser[-1]["datum"] if leveranser else None,
    }

def update_html(chart_data):
    with open(HTML_FILE, encoding="utf-8") as f:
        content = f.read()

    original = content
    json_str = json.dumps(chart_data, ensure_ascii=False)

    # Ersätt CHART_DATA_PLACEHOLDER med faktisk data
    pattern = re.compile(r'const CHART_DATA\s*=\s*\{[^;]+\};', re.DOTALL)
    replacement = f"const CHART_DATA = {json_str};"

    if pattern.search(content):
        content = pattern.sub(replacement, content)
    else:
        print("Varning: hittade inte CHART_DATA i HTML-filen.")
        return False

    if content == original:
        print("Ingen förändring.")
        return False

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"pellets.html uppdaterad: {chart_data['antal_leveranser']} leveranser, "
          f"{chart_data['totalt_ton']} ton totalt.")
    return True

def main():
    data = load_data()
    leveranser = data.get("leveranser", [])

    if not leveranser:
        print("Inga leveranser i pellets_data.json — hoppar över.")
        sys.exit(0)

    chart_data = build_chart_data(leveranser)
    update_html(chart_data)

if __name__ == "__main__":
    main()
