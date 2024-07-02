import math

def berechne_Zylinder():
    # Eingabe der Größen durch den Benutzer
    R = float(input("Gib den Radius R ein: "))
    H = float(input("Gib die Höhe H ein: "))

    # Berechnungen
    V = math.pi * R**2 * H
    M = 2 * math.pi * R * H
    O = 2 * math.pi * R * (R + H)

    # Ergebnisse anzeigen
    print(f"Volumen (V) = {V: .2f}") #das f ist ein Formatierter String
    print(f"Mantelfläche (M) = {M:.2f}")
    print(f"Oberfläche (O) = {O:.2f}")

# Funktion aufrufen

berechne_Zylinder()
