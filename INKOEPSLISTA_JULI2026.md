# Inköpslista — Österskär Fastighetsdashboard
## UPPDATERAD 2026-06-29 — Fase 1 & 2 Sensorer

### Fas 1: Raspberry Pi + Modbus + 1-Wire (Värmesystem)
**Målkostnad:** 1 475–1 850 kr | **Status:** Delvis beställd ✅

### Fas 1B: Tilläggsensorer (Musikstudio + Trädgård + Kallvatten)
**Målkostnad:** ~1 200 kr | **Status:** Aktuell utredning (delvis beställd)

### Fas 2: LoRa-sensorstation (Strandfastigheten)
**Målkostnad:** ~3 500 kr | **Status:** Framtida planering

---

## Raspberry Pi-hubb (Pannrum)

| Post | Specifikation | Målpris | Verklig kostnad | Status |
|------|--------------|---------|---------|--------|
| **Raspberry Pi 5 Starter Kit komplett** | db-tronic: Pi 5 4GB, SD 64GB, USB-C 27W, hölje, HDMI | ~800–1 000 kr | **2 000 kr** | ✅ **Beställd, levereras 2026-07-02** |
| **Delsumma** | | **~800–1 000 kr** | **2 000 kr** | |

---

## Modbus RTU-koppling (Danfoss ECL Comfort 110)

| Post | Specifikation | Målpris | Verklig kostnad | Status |
|------|--------------|---------|---------|--------|
| USB–RS485-adapter | Waveshare Industrial USB-RS485 Converter | ~150 kr | **219,99 kr** | ✅ **Beställd, levereras 2026-07-02** |
| 3-ledare kabel | Telefonkabel hemma eller RS485-kabel 3m | 0–40 kr | **0 kr** | ✅ Hemma |
| **Delsumma** | | **~150 kr** | **219,99 kr** | |

---

## 1-Wire Temperaturgivare (10 st DS18B20 — utökat system)

| Post | Specifikation | Målpris | Verklig kostnad | Status |
|------|--------------|---------|---------|--------|
| DS18B20 sensorer | Fasizi Waterproof DS18B20 (10 st) | ~250–300 kr | **275 kr** | ✅ **Beställda, levereras 2026-07-02** |
| 4,7 kΩ pull-up-resistor | 1/4 W eller större | ~5 kr | **45 kr** | ✅ **Beställd, levereras 2026-06-30** |
| 1-Wire-kabel | 3-ledare kabel från tank till Pi | 0–40 kr | **0 kr** | ✅ Hemma |
| **Delsumma givare** | | **~300 kr** | **320 kr** | |

---

## Montagematerial för givare på röret (6 st utanpå röret)

| Post | Specifikation | Mängd | Målpris | Verklig kostnad | Status |
|------|--------------|-------|---------|---------|--------|
| Rörisolering | Skumgummi eller mineralull, 24–32 mm tjock | 2–3m | ~30–50 kr | **0 kr** | ✅ **Finns hemma** |
| Rörklammer | Metallklammer för att fästa isolering på röret | 10–15 st | ~15–25 kr | **0 kr** | ✅ **Finns hemma** |
| Alu-tejp eller vattenfast tejp | För fuktsäkerhet runt isolering | 1–2 rullar | ~30–40 kr | **0 kr** | ✅ **Finns hemma** |
| Buntband (plastband) | För extra säkerhet | 100 st | ~15–20 kr | **0 kr** | ✅ **Finns hemma** |
| Givarbindare (optional) | Plastbindare för sensormontering | 10 st | ~50–100 kr | **0 kr** | ✅ Inte nödvändigt |
| **Delsumma montering** | | | **~200–350 kr** | **0 kr** | ✅ **ALLT FINNS HEMMA** |

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

## Sammanfattning — Totalkostnad Fase 1 (SLUTGILTIG — ALLA KOMPONENTER BESTÄLLDA)

| Kategori | Målpris | Verklig kostnad | Status |
|----------|---------|---------|--------|
| **Raspberry Pi 5 Starter Kit** (db-tronic, 4GB, 64GB, hölje, USB-C 27W) | ~800–1 000 kr | **2 000 kr** | ✅ **Beställd** |
| Modbus RTU (Waveshare USB-RS485) | ~150 kr | **219,99 kr** | ✅ Beställd |
| 1-Wire givare (10 st DS18B20) | ~250–300 kr | **275 kr** | ✅ Beställd |
| Pull-up resistor 4,7 kΩ | ~5 kr | **45 kr** | ✅ Beställd |
| Givarmontage (allt hemma) | ~200–350 kr | **0 kr** | ✅ Hemma |
| Lokala inköp (övriga) | ~0 kr | **0 kr** | ✅ Hemma |
| **Totalt Fas 1** | **~1 475–1 850 kr** | **2 539,99 kr** | ✅ **ALLA BESTÄLLDA** |

### Leveransöversikt:
- **Torsdag 2026-07-02:**
  - ✅ Raspberry Pi 5 Starter Kit (2 000 kr)
  - ✅ Waveshare USB-RS485 (219,99 kr)
  - ✅ Fasizi DS18B20 (10 st) — 275 kr
  
- **Imorgon 2026-06-30:**
  - ✅ 4,7 kΩ resistor (45 kr)

### Material från hemmet (0 kr kostnad):
- Rörisolering, rörklammer, alu-tejp, buntband: **Finns hemma** ✅

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

## Fase 1B: Tilläggsensorer (Musikstudio, Trädgård, Kallvatten)

### CO₂-sensor — Musikstudio (Gillestuga)
| Post | Specifikation | Pris | Status |
|------|--------------|------|--------|
| CO₂-sensor | Sensiron SCD41 (I2C, CO₂+temp+fukt) | ~400 kr | 🔄 Att beställa — Prioritet 1 |
| Monteringsmaterial | Kabelkonnektor, jumperledningar | ~20 kr | 🔄 Köp lokalt |
| **Delsumma CO₂** | | **~420 kr** | |

### Ljudnivå-sensor — Musikstudio (Gillestuga)
| Post | Specifikation | Pris | Status |
|------|--------------|------|--------|
| Mikrofon I2S | INMP441 digital I2S-mikrofon | ~100 kr | 🔄 Att beställa — Prioritet 3 |
| Jumperledningar | 4-pol kopplingsled för I2S | ~20 kr | 🔄 Köp lokalt |
| **Delsumma Ljud** | | **~120 kr** | |

### Kallvattensensor — Värmesystem
| Post | Specifikation | Pris | Status |
|------|--------------|------|--------|
| DS18B20 (redan beställd) | Waterproof probe (av 10 beställda) | **0 kr** | ✅ Beställd 2026-06-27 |
| Rörisolering | För monteringisolering på mätare | **0 kr** | ✅ **Finns hemma** |
| Rörklammer | För fäste på kallvattenmätare | **0 kr** | ✅ **Finns hemma** |
| **Delsumma Kallvatten** | | **0 kr** | ✅ **INGET ATT KÖPA** |

### Jordtemperatur-sensor — Trädgård (Bonus)
| Post | Specifikation | Pris | Status |
|------|--------------|------|--------|
| DS18B20 (redan beställd) | Waterproof probe (av 10 beställda) | **0 kr** | ✅ Beställd 2026-06-27 |
| Rörisolering (kort bit) | För jordmontage (~10 cm djup) | **0 kr** | ✅ **Finns hemma** |
| **Delsumma Mark** | | **0 kr** | ✅ **INGET ATT KÖPA** |

### Delsumma Fas 1B (UPPDATERAD)
| Kategori | Kostnad | Status |
|----------|---------|--------|
| CO₂-sensor (SCD41) | ~420 kr | 🔄 Att beställa |
| Ljud-sensor (INMP441) | ~120 kr | 🔄 Att beställa (senare) |
| Kallvattensensor montage | **0 kr** | ✅ **Allt hemma** |
| Jordtempsensor montage | **0 kr** | ✅ **Allt hemma** |
| **Totalt Fas 1B** | **~540 kr** | 🔄 **Sparades 55 kr** |

**Notering:** De två DS18B20-sensorerna för kallvatten och jordtemp var redan inkluderade i den ursprungliga beställningen av 10 sensorer. Monteringsmaterial finns redan hemma — ingen ytterligare köpning behövs.

---

## Fase 2: LoRa-sensorstation (Strandfastigheten — Hösten 2026)
Planera efter juli-fokus. Budget ~1 500 kr.

- RAK7268 LoRa Gateway (~700 kr)
- TTGO LoRa32 × 2 noder (~350 kr)
- RTL-SDR USB-dongel (~300 kr)
- Sensorer (pellets, vatten, el) (~300 kr)

---

## TOTALKOSTNAD — FAS 1 + FAS 1B (Före Hösten 2026) — SLUTGILTIG BESTÄLLD

| Fas | Kategori | Målpris | Verklig kostnad | Status | Notering |
|-----|----------|---------|---------|--------|----------|
| **Fas 1** | Raspberry Pi + Modbus + 1-Wire | ~1 475–1 850 kr | **2 539,99 kr** | ✅ **ALLA BESTÄLLDA** | Levereras 2026-06-30 + 2026-07-02 |
| **Fas 1B** | Sensorer (CO₂ + Ljud + Kallvatten + Mark) | ~540 kr | ~540 kr | 🔄 CO₂ + Ljud att beställa | Monteringsmaterial hemma |
| **Totalt Fas 1+1B** | **Värmesystem + Musikstudio + Trädgård** | **~2 070–2 445 kr** | **~3 080–3 280 kr** | ✅ Fas 1 klar | Väntar på Fas 1B sensorer |
| **Fas 2** | LoRa-sensorstation (framtid) | ~3 500 kr | ~3 500 kr | 📅 Hösten 2026 | Separat projekt |

---

## BESTÄLLNINGSSTATUS — 2026-06-29 (SLUTGILTIG)

### ✅ REDAN BESTÄLLDA OCH BEKRÄFTADE (Verkliga priser)

**Levereras Torsdag 2026-07-02:**
- **Raspberry Pi 5 Starter Kit** (db-tronic, 4 GB, 64 GB SD, USB-C 27W, hölje med fläkt, Micro HDMI 4K) — **2 000 kr** ✅
- **DS18B20 Waterproof × 10 st** (Fasizi, Amazon B09Z29TKCV) — **275 kr** ✅
- **Waveshare USB-RS485** (Modbus RTU) — **219,99 kr** ✅

**Levereras Imorgon 2026-06-30:**
- **4,7 kΩ Pull-up resistor** (Electrokit) — **45 kr** ✅

**Total redan köpt/beställt:** **2 539,99 kr** ✅

**Material från hemmet (0 kr):**
- Rörisolering, rörklammer, alu-tejp, buntband — **Allt finns hemma** ✅

### 🔄 ATT BESTÄLLA (Fas 1B — Prioritering)
1. **SCD41 CO₂-sensor** (~400 kr) — Musikstudio — **HÖGSTA PRIORITET (Fas 1B)**
2. **INMP441 Ljud-sensor** (~100 kr) — Musikstudio — **Prioritet 3 (Fas 1B, senare)**

---

## ⏰ NÄSTA STEG — HANDLINGSLISTA (2026-06-29)

**Imorgon 2026-06-30:**
- [ ] Mottagning: 4,7 kΩ resistor från Electrokit (leverans)
- [ ] Lagring: Placera resistorn i komponentkasse för GPIO-test

**Torsdag 2026-07-02:**
- [ ] Mottagning: Raspberry Pi 5 Starter Kit (db-tronic)
- [ ] Mottagning: DS18B20 sensorer × 10 st
- [ ] Mottagning: Waveshare USB-RS485 adapter
- [ ] Inspektioner: Kontrollera att alla komponenter är intakta
- [ ] **STARTA:** Raspberry Pi OS-installation på SD-kortet
  - Hämta Raspberry Pi Imager från raspberrypi.com
  - Installera Raspberry Pi OS (64-bit Bookworm eller liknande)
  - Första boot: WiFi-setup, SSH-aktivering, GPIO-setup
- [ ] **TEST:** I2C-bus test (`i2cdetect -y 1`) — förberedelse för CO₂-sensor (Fas 1B)
- [ ] **TEST:** 1-Wire GPIO4 test med DS18B20 (`vcgencmd measure_temp` och 1-Wire adresshämtning)

**Nästa vecka:**
- [ ] Beställ **SCD41 CO₂-sensor** (högsta prioritet)
- [ ] Montering: Kallvattensensor på kallvattenmätare (med hemmavarande material)
- [ ] Montering: Jordtempsensor 8–10 cm djup i trädgården

**Senare Fas 1B:**
- [ ] Beställ INMP441 Ljud-sensor
- [ ] Integration: CO₂ + Ljud på musikstudio via I2C + I2S

### 📅 FRAMTIDA (Hösten 2026)
- LoRa-sensorstation (Arduino/STM32, RFM95W, solcell, sensorer) — ~3 500 kr — **Fas 2**
- Solfångare IR-adapter (Watts P-3481) — Pris okänt — **Parallell**

---

## NÄSTA STEG — HANDLINGSLISTA

1. ✅ **Bekräfta leverans 2026-07-02** (Pi, SD, adapter, DS18B20)
2. 🔄 **Beställ SCD41 CO₂-sensor** (musikstudio) — från Amazon/Electrokit
3. 🔄 **Köp monteringsmaterial lokalt** (VVS-butik):
   - Rörisolering 24–32 mm (2–3 m)
   - Rörklammer × 10–15 st
   - Alu-tejp/vattenfast tejp
   - Buntband × 100 st
4. 🔄 **Köp elektronik lokalt** (elektronikbutik):
   - 4,7 kΩ resistor (1/4 W)
5. 📅 **Planera LoRa-sensorstation** — hösten 2026
6. ⚠️ **Boka VVS-service** — solfångare "Alarm Flöde"

---

**Skapad:** 2026-06-27 | **Uppdaterad:** 2026-06-29 | **Projekt:** Österskär Fastighetsdashboard