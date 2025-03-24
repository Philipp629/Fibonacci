# Funktion zur Berechnung der Fibonacci-Folge ab einer bestimmten Zahl
def fibonacci_from_number(n, start_number):
    # Liste für die Fibonacci-Zahlen initialisieren
    fib_sequence = [0, 1]
    
    # Generiere die Folge, bis wir die Startzahl erreichen oder überschreiten
    while fib_sequence[-1] < start_number:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    # Prüfe, ob die Startzahl in der Folge ist
    if start_number not in fib_sequence:
        lower = fib_sequence[-2]  # Nächstniedrigere Zahl
        higher = fib_sequence[-1]  # Nächsthöhere Zahl
        return False, lower, higher, None
    
    # Berechne die nächsten n Zahlen ab der Startzahl
    start_index = fib_sequence.index(start_number)
    while len(fib_sequence) < start_index + n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return True, None, None, fib_sequence[start_index:start_index + n]

# Schritt 1: Die ersten 8 Fibonacci-Zahlen als Beispiel ausgeben
n_default = 8
is_valid, _, _, fib_numbers_default = fibonacci_from_number(n_default, 0)
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

# Startzahl abfragen mit Prüfung
while True:
    print("\nBei welcher Zahl soll die Fibonacci-Folge beginnen?")
    try:
        start_number = int(input("Gib die Startzahl ein (z. B. 0, 1, 2, 3, 5, ...): "))
        if start_number < 0:
            print("Bitte gib eine nicht-negative Zahl ein.")
            continue
        
        # Prüfe die Startzahl und berechne die Folge
        is_valid, lower, higher, fib_numbers_user = fibonacci_from_number(n_user, start_number)
        
        if not is_valid:
            print(f"\nHinweis: {start_number} ist keine Fibonacci-Zahl.")
            print(f"Stattdessen könntest du bei {lower} (nächstniedriger) oder {higher} (nächsthöher) beginnen.")
            continue
        else:
            break
    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine ganze Zahl ein.")

# Ausgabe der benutzerdefinierten Fibonacci-Folge
print(f"\nDie {n_user} Fibonacci-Zahlen ab {start_number} sind:")
print(fib_numbers_user)