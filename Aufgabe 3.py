def main():
    # Benutzereingabe
    user_input = input("Bitte geben Sie eine geeignete Zeichenkette ein: ")

    # Ausgabe als Unicode-String
    unicode_string = user_input
    print(f"Unicode-String: {unicode_string}")

    # Versuch, die Eingabe als Ganzzahl zu interpretieren
    try:
        integer_value = int(user_input)
        print(f"Ganzzahl: {integer_value}")
    except ValueError:
        print("Die Eingabe ist keine gültige Ganzzahl.")

    # Versuch, die Eingabe als Gleitpunktzahl zu interpretieren
    try:
        float_value = float(user_input)
        print(f"Gleitpunktzahl: {float_value}")
    except ValueError:
        print("Die Eingabe ist keine gültige Gleitpunktzahl.")

if __name__ == "__main__":
    main()
