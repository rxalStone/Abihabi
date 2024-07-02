#Schreiben Sie ein Python-Programm, das vom Benutzer eine Zeichenkette anfodert.
# Anschließend soll diese Zeichenkette zweifach ausgegeben werden:
# zunächst in Kleinbuchstaben und anschließend in Großbuchstaben

EingabeUser = input("Geben Sie eine Zeichenkette an: ")

Groß = EingabeUser.lower()
Klein = EingabeUser.upper()

# Ausgabe Konsole
print("Ergebnis Kleinbuchstaben: " + Klein)
print("Ergebnis Großbuchstaben " + Groß)

# Finish
