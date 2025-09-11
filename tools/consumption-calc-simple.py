def safe_float_input(prompt):
    """Pobiera input i zamienia przecinek na kropkę, usuwa spacje, zwraca float."""
    while True:
        try:
            val = input(prompt).strip().replace(",", ".").replace(" ", "")
            return float(val)
        except ValueError:
            print("⚠️  Błąd: podaj liczbę (np. 1234.56 lub 1234,56).")


def main():
    print("=== Kalkulator czasu pracy na 1S LiPo ===")

    current_mA = safe_float_input("Podaj średni prąd urządzenia [mA]: ")
    capacity_mAh = safe_float_input("Podaj pojemność ogniwa [mAh]: ")

    # Założenia napięciowe
    U_full = 4.2
    U_cutoff = 3.0
    U_safe = 3.3

    # Procent użytecznej pojemności
    usable_fraction = (U_full - U_safe) / (U_full - U_cutoff)

    usable_capacity_mAh = capacity_mAh * usable_fraction

    # Czas pracy w godzinach (float)
    time_h = usable_capacity_mAh / current_mA

    # Formatowanie do godzin i minut
    hours = int(time_h)
    minutes = int(round((time_h - hours) * 60))

    # Jeśli wyszło 60 minut -> podbij godzinę
    if minutes == 60:
        hours += 1
        minutes = 0

    # Dodatek w dniach, jeśli >24h
    days_info = ""
    if time_h >= 24:
        days = time_h / 24
        days_info = f" ({days:.2f} dni)"

    print(f"\nPrzy średnim prądzie {current_mA:.2f} mA i ogniwie {capacity_mAh:.2f} mAh")
    print(f"Użyteczna pojemność (do {U_safe} V): ~{usable_capacity_mAh:.2f} mAh")
    print(f"Maksymalny czas pracy: {hours} h {minutes} min (~{time_h:.2f} h){days_info}")


if __name__ == "__main__":
    main()
