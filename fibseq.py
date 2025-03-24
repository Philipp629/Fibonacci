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

# Die ersten 8 Fibonacci-Zahlen berechnen
n = 8
fib_numbers = fibonacci(n)

# Ausgabe der Ergebnisse
print(f"Die ersten {n} Fibonacci-Zahlen sind:")
print(fib_numbers)