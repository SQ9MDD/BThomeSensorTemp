# ESP32-C3 DS18B20 BTHome Sensor

Minimalistyczny firmware dla ESP32-C3, który:
- odczytuje temperaturę z czujnika DS18B20,
- mierzy napięcie baterii przez dzielnik rezystorowy (z kalibracją),
- szacuje poziom naładowania baterii Li-Ion/Li-Po,
- wysyła dane w formacie **BTHome v2** przez BLE (broadcast),
- wchodzi w tryb głębokiego uśpienia (deep sleep) na określony czas.

Zaprojektowany z myślą o niskim poborze mocy – idealny do zasilania bateryjnego.

## Wymagania

- ESP32-C3 (np. DevKitM-1)
- DS18B20
- Dzielnik napięcia (VBAT)
- Arduino IDE lub PlatformIO

## Licencja

MIT License  
(c) 2025 Rysiek Labus — [sq9mdd.qrz.pl](https://sq9mdd.qrz.pl)
