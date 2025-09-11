# ESP32-C3 DS18B20 BTHome Sensor

## 🇵🇱 Opis

Minimalistyczny firmware dla ESP32-C3, który:
- odczytuje temperaturę z czujnika DS18B20,
- mierzy napięcie baterii przez dzielnik rezystorowy (z kalibracją),
- szacuje poziom naładowania baterii Li-Ion/Li-Po,
- wysyła dane w formacie **BTHome v2** przez BLE (broadcast),
- wchodzi w tryb głębokiego uśpienia (deep sleep) na określony czas.

✅ Średni pobór prądu: **ok. 240 µA** (zależnie od długości reklamy BLE i czasu aktywności).

Zaprojektowany z myślą o niskim poborze mocy – idealny do zasilania bateryjnego.

## 🇬🇧 Description

Minimalistic firmware for ESP32-C3 that:
- reads temperature from DS18B20 sensor,
- measures battery voltage via resistor divider (with calibration),
- estimates Li-Ion/Li-Po battery state of charge,
- broadcasts data using **BTHome v2** format over BLE,
- enters deep sleep mode for a defined period.

✅ Average current consumption: **~240 µA** (depends on BLE advertising and active time).

Designed for low power consumption – perfect for battery-powered applications.

---

## Wymagania / Requirements

- ESP32-C3 (e.g. DevKitM-1)
- DS18B20 sensor
- Voltage divider on VBAT
- Arduino IDE or PlatformIO

---

## Licencja / License

MIT License  
(c) 2025 Rysiek Labus — [https://sq9mdd.qrz.pl](https://sq9mdd.qrz.pl)
