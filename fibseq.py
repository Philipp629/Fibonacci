# Funktion zur Berechnung der Fibonacci-Folge ab einer bestimmten Zahl
def fibonacci_from_number(n, start_number):
    # Liste für die natürliche Fibonacci-Folge zur Überprüfung
    fib_natural = [0, 1]
    while fib_natural[-1] < start_number:
        fib_natural.append(fib_natural[-1] + fib_natural[-2])
    
    # Prüfe, ob die Startzahl in der natürlichen Folge ist
    if start_number not in fib_natural:
        print(f"\nHinweis: {start_number} ist keine natürliche Fibonacci-Zahl.")
        print(f"Nächstniedrigere: {fib_natural[-2]}, nächsthöhere: {fib_natural[-1]}")
    
    # Finde die vorherige Zahl für eine korrekte Fibonacci-Folge
    fib_sequence = [fib_natural[-2], start_number]  # Start mit der vorherigen natürlichen Zahl und der eingegebenen Zahl
    for i in range(n - 2):  # Berechne die restlichen n-2 Zahlen
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    # Wenn n=1, geben wir nur die Startzahl zurück
    if n == 1:
        return [start_number]
    
    return fib_sequence[-n:]  # Rückgabe der letzten n Zahlen

# Schritt 1: Die ersten 8 Fibonacci-Zahlen als Beispiel ausgeben
n_default = 8
fib_numbers_default = fibonacci_from_number(n_default, 0)
print(f"Beispiel: Die ersten {n_default} Fibonacci-Zahlen sind:")
print(fib_numbers_default)

# Schritt 3: Anwender nach Anzahl und Startzahl fragen
print("\nWie viele Fibonacci-Zahlen möchtest du ausgeben?")
while True:
    try:
        n_user = int(input("Gib die Anzahl ein: "))
        if n_user <= 0:
            print("Bitte gib eine positive Zahl ein.")
        else:
            break
    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine ganze Zahl ein.")

print("\nBei welcher Zahl soll die Fibonacci-Folge beginnen?")
while True:
    try:
        start_number = int(input("Gib die Startzahl ein: "))
        if start_number < 0:
            print("Bitte gib eine nicht-negative Zahl ein.")
        else:
            break
    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine ganze Zahl ein.")

# Berechnung und Ausgabe der benutzerdefinierten Fibonacci-Folge
fib_numbers_user = fibonacci_from_number(n_user, start_number)
print(f"\nDie {n_user} Fibonacci-Zahlen ab {start_number} sind:")
print(fib_numbers_user)