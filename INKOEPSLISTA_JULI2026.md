# Inköpslista — Österskär Fastighetsdashboard
## Fase 1: Raspberry Pi + Modbus + 1-Wire
**Målkostnad:** 1 400–1 800 kr | **Tidplan:** Juli 2026

---

## Raspberry Pi-hubb (Pannrum)

| Post | Specifikation | Pris | Länk/Produkt | Status |
|------|--------------|------|------|--------|
| Raspberry Pi | Pi 4 eller 5, 2–4 GB RAM | ~500–700 kr | — | 🔄 Att beställa |
| SD-kort | 16–32 GB, Class 10 | ~100 kr | — | 🔄 Att beställa |
| Strömadapter | USB-C, 5V, minst 3A | ~100 kr | — | 🔄 Att beställa |
| Plasthölje | Aluminiumhölje för Pi 4/5 | ~100 kr | — | 🔄 Att beställa |
| **Delsumma** | | **~800–1 000 kr** | | |

---

## Modbus RTU-koppling (Danfoss ECL Comfort 110)

| Post | Specifikation | Pris | Länk/Produkt | Status |
|------|--------------|------|------|--------|
| USB–RS485-adapter | Waveshare Industrial USB-RS485 Converter | ~150 kr | Amazon.se | ✅ Godkänd |
| 3-ledare kabel | Telefonkabel hemma eller RS485-kabel 3m | 0–40 kr | Hemma/köp | ✅ Hemma |
| **Delsumma** | | **~150 kr** | | |

---

## 1-Wire Temperaturgivare (10 st DS18B20 — utökat system)

| Post | Specifikation | Pris | Länk/Produkt | Status |
|------|--------------|------|------|--------|
| DS18B20 sensorer | Fasizi Waterproof DS18B20 (2 paket = 10 st) | ~250–300 kr | Amazon.se B09Z29TKCV | ✅ Godkänd |
| 4,7 kΩ pull-up-resistor | 1/4 W eller större | ~5 kr | Electrokit eller lokal elektronikbutik | 🔄 Köp lokalt |
| 1-Wire-kabel | 3-ledare kabel från tank till Pi | 0–40 kr | Telefonkabel hemma eller köp | ✅ Hemma |
| **Delsumma givare** | | **~300 kr** | | |

---

## Montagematerial för givare på röret (6 st utanpå röret)

| Post | Specifikation | Mängd | Pris | Status |
|------|--------------|-------|------|--------|
| Rörisolering | Skumgummi eller mineralull, 24–32 mm tjock | 2–3m | ~50–100 kr | 🔄 Köp lokalt (VVS) |
| Rörklammer | Metallklammer för att fästa isolering på röret | 10–15 st | ~20–50 kr | 🔄 Köp lokalt (VVS) |
| Alu-tejp eller vattenfast tejp | För fuktsäkerhet runt isolering | 1–2 rullar | ~30–60 kr | 🔄 Köp lokalt (VVS) |
| Buntband (plastband) | För extra säkerhet | 100 st | ~20 kr | 🔄 Köp lokalt (butik) |
| Givarbindare (optional) | Plastbindare för sensormontering | 10 st | ~50–100 kr | ⚪ Optional |
| **Delsumma montering** | | | **~200–350 kr** | |

**Notering:** 4 givare (T3-T6) sitter redan INUTI ackumulatortanken i egna givarplatser — ingen köpning nödvändig.

---

## Utökat givarsystem (10 sensorer)

| T-nr | Placering | System | Typ | Status |
|------|-----------|--------|-----|--------|
| T1–T2 | Fram/retur panna | Pelletspanna | — | Ingår i paket |
| T3–T6 | Tank 4 höjder | Ackumulatortank | Givare | Ingår i paket |
| T7–T8 | Fram/retur sol | Solvärmekrets | Givare | Ingår i paket |
| T9–T10 | Värmekrets returer | Radiatorvärmekrets | Givare | Ingår i paket |
| *T11–T12* | *Pannrummet/framtid* | *Reserv* | *Extra givare* | Ingår i paket |

---

## Montage & installation (ej köp)

| Arbetsuppgift | Beskrivning |
|----------------|------------|
| Givarmontage | Montera 10 givare parallellkopplade på 1-Wire-buss (GPIO4) |
| Kabelrörning | Dra 3-ledare kabel från tank → Pi:n (~3 m) |
| Modbus-koppling | Anslut Waveshare USB–RS485-adapter till Pi och Danfoss ECL |
| Konfiguration | Installera OS, Python-bibliotek (w1-gpio, w1-therm, pyModbus), skapa datainsamlingsskript |
| Pull-up resistor | Anslut 4,7 kΩ mellan GPIO4 och +3,3V |

---

## Sammanfattning — Totalkostnad Fase 1

| Kategori | Kostnad |
|----------|---------|
| Raspberry Pi-hubb | ~800–1 000 kr |
| Modbus RTU (Waveshare) | ~150 kr |
| 1-Wire givare (10 st) | ~300 kr |
| Givarmontage (rörisolering, klammer, tejp) | ~200–350 kr |
| Lokala inköp (resistor, buntband) | ~25–50 kr |
| **Totalt** | **~1 475–1 850 kr** |

**Rekommendation:** Budgetera ~1 900 kr för säkerhetsmarginal.

### Inköp från Amazon (redan godkänd):
- Waveshare USB-RS485: ~150 kr
- Fasizi DS18B20 (2 paket): ~250–300 kr
- **Summa Amazon:** ~400–450 kr

### Lokala inköp (VVS-butik, elektronikbutik, byggvaruhus):
- Rörisolering, klammer, tejp: ~200–350 kr
- 4,7 kΩ resistor: ~5 kr
- Buntband: ~20 kr
- **Summa lokalt:** ~225–375 kr

### Amazon/webbutik:
- Raspberry Pi, SD-kort, adapter, hölje: ~800–1 000 kr

---

## Produkter funna & godkända ✅

### Modbus RTU
- **Waveshare Industrial USB-RS485 Converter** (Amazon.se)
  - Pris: ~150 kr
  - FTDI-kompatibel, stödjer 9600 baud
  - Snabb leverans
  - ✅ GODKÄND

### 1-Wire Temperaturgivare
- **Fasizi Waterproof DS18B20 (2 paket = 10 sensorer)** (Amazon.se, B09Z29TKCV)
  - Pris: ~250–300 kr
  - Vattentäta, perfekt för värmesystem
  - 1-Wire protokoll, DS18B20-standard
  - Ger 2 extra sensorer för framtida bruk (pannrum/väderstation)
  - ✅ GODKÄND

### Givarmontage-material
- **Rörisolering** (skumgummi/mineralull 24–32 mm)
  - Pris: ~50–100 kr
  - För att omvikla givare monterade utanpå värmebärare-rör
  - Köp från VVS-butik
  
- **Rörklammer** (10–15 st metallklammer)
  - Pris: ~20–50 kr
  - För att fästa isolering på röret
  - Köp från VVS-butik

- **Alu-tejp eller vattenfast tejp** (1–2 rullar)
  - Pris: ~30–60 kr
  - För fuktsäkerhet runt isolering
  - Köp från VVS-butik

- **Buntband** (plastband, 100 st)
  - Pris: ~20 kr
  - Extra säkerhet för montage
  - Köp från byggvaruhus/butik

**Notering:** 4 givare (T3-T6) sitter redan INUTI ackumulatortanken i egna givarplatser — ingen extra monteringsmaterial nödvändigt.

---

## Parallella inköp & nästa steg

| Post | Status | Notering |
|------|--------|---------|
| Optisk IR-adapter (Watts P-3481) | ⚠ Kontakta Watts | För solfångare — pris/leverans okänt |
| VVS-service (Alarm Flöde) | ⚠ Boka omedelbar | Solfångaren behöver service innan full integration |
| Lokala inköp (resistor, T-kopplingar) | 🔄 Att köpa | VVS-butik eller elektronikbutik |

---

## Fase 2: LoRa + pelletsgivare (Hösten 2026)
Planera efter juli-fokus. Budget ~1 500 kr.

- RAK7268 LoRa Gateway (~700 kr)
- TTGO LoRa32 × 2 noder (~350 kr)
- RTL-SDR USB-dongel (~300 kr)
- Sensorer (pellets, vatten, el) (~300 kr)

---

**Skapad:** 2026-06-27 | **Projekt:** Österskär Fastighetsdashboard