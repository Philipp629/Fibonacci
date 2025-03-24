# Funktion zur Berechnung der Fibonacci-Folge
def fibonacci(n):
    # Liste für die Fibonacci-Zahlen initialisieren
    fib_sequence = [0, 1]  # Start mit den ersten beiden Zahlen
    
    # Falls n kleiner oder gleich 2 ist, geben wir nur die ersten n Zahlen zurück
    if n <= 1:
        return fib_sequence[:n]
    
    # Berechnung der weiteren Fibonacci-Zahlen
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence

# Schritt 1: Die ersten 8 Fibonacci-Zahlen berechnen und ausgeben
n_default = 8
fib_numbers_default = fibonacci(n_default)
print(f"Die ersten {n_default} Fibonacci-Zahlen sind:")
print(fib_numbers_default)

# Schritt 2: Anwender nach der gewünschten Anzahl fragen
print("\nWie viele Fibonacci-Zahlen möchtest du ausgeben?")
while True:
    try:
        n_user = int(input("Gib eine Zahl ein: "))
        if n_user < 0:
            print("Bitte gib eine positive Zahl ein.")
        else:
            break
    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine ganze Zahl ein.")

# Berechnung und Ausgabe der benutzerdefinierten Anzahl
fib_numbers_user = fibonacci(n_user)
print(f"\nDie ersten {n_user} Fibonacci-Zahlen sind:")
print(fib_numbers_user)