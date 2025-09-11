# calibrate_vbat_cli.py
# Kalibracja: V_true = K * raw_mV + BmV
# Punkty odniesienia: 4.2 V (4200 mV) i 3.6 V (3600 mV)

V1_mV = 4200.0
V2_mV = 3600.0

def _parse_number(s: str) -> float:
    """Akceptuje kropkę/przecinek. Zwraca float."""
    s = s.strip().lower().replace(',', '.')
    # wyciągnij pierwszy token, który wygląda jak liczba
    import re
    m = re.search(r'[-+]?\d+(?:\.\d+)?', s)
    if not m:
        raise ValueError("Nie podano liczby.")
    return float(m.group(0))

def _read_raw(prompt: str) -> float:
    """Czyta surowy odczyt napięcia (mV). Jeśli wartość < 20, przyjmuje wolty i konwertuje."""
    v = _parse_number(input(prompt))
    if v < 20.0:  # wygląda na wolty
        v *= 1000.0
        print(f"(Wykryto jednostkę w V → przeliczone na {v:.1f} mV)")
    return v

def compute_calibration(raw1_mV: float, raw2_mV: float,
                        v1_mV: float = V1_mV, v2_mV: float = V2_mV):
    if abs(raw2_mV - raw1_mV) < 1e-9:
        raise ValueError("Surowe odczyty są identyczne — nie da się policzyć K.")
    K = (v2_mV - v1_mV) / (raw2_mV - raw1_mV)
    BmV = v1_mV - K * raw1_mV
    return K, BmV

def apply_calibration(raw_mV: float, K: float, BmV: float) -> float:
    return K * raw_mV + BmV

if __name__ == "__main__":
    try:
        r1 = _read_raw("Podaj surowy odczyt z urządzenia (mV/V) przy 4.2 V: ")
        r2 = _read_raw("Podaj surowy odczyt z urządzenia (mV/V) przy 3.6 V: ")

        K, BmV = compute_calibration(r1, r2)
        print("\nWYNIK KALIBRACJI:")
        print(f"  CAL_K   = {K:.8f}")
        print(f"  CAL_BmV = {BmV:.2f}  # mV")

        # Szybki self-check
        c1 = apply_calibration(r1, K, BmV)
        c2 = apply_calibration(r2, K, BmV)
        print("\nSelf-check (błąd względem ideału):")
        print(f"  przy 4.2 V → {c1:.2f} mV  (Δ={c1 - V1_mV:+.2f} mV)")
        print(f"  przy 3.6 V → {c2:.2f} mV  (Δ={c2 - V2_mV:+.2f} mV)")
    except Exception as e:
        print("Błąd:", e)
