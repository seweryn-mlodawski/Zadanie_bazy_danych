import sqlite3

# Połączenie z bazą
conn = sqlite3.connect('air_quality.db')

print("="*70)
print("PRZYKŁAD 1: PODSTAWOWE ZAPYTANIA SELECT")
print("="*70)

# ============================================================================
# ZAPYTANIE 1: SELECT * FROM stations LIMIT 5
# ============================================================================

print("\n1. WYBIERZ WSZYSTKIE KOLUMNY Z TABELI STATIONS (LIMIT 5)")
print("-"*70)

result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()

print(f"Liczba wyników: {len(result)}\n")

for i, row in enumerate(result, 1):
    print(f"Wiersz {i}: {row}")

# ============================================================================
# ZAPYTANIE 2: SELECT * FROM measurements LIMIT 5
# ============================================================================

print("\n2. WYBIERZ WSZYSTKIE KOLUMNY Z TABELI MEASUREMENTS (LIMIT 10)")
print("-"*70)

result = conn.execute("SELECT * FROM measurements LIMIT 10").fetchall()

print(f"Liczba wyników: {len(result)}\n")

for i, row in enumerate(result, 1):
    print(f"Wiersz {i}: {row}")

# ============================================================================
# ZAPYTANIE 3: SELECT z określonymi kolumnami
# ============================================================================

print("\n3️. WYBIERZ TYLKO NAZWY i KRAJE STACJI")
print("-"*70)

result = conn.execute("SELECT name, country FROM stations").fetchall()

print(f"Liczba wyników: {len(result)}\n")

for name, country in result:
    print(f"Kraj {country}, Stacja: {name}")

# ============================================================================
# ZAPYTANIE 4: COUNT - Liczenie wierszy
# ============================================================================

print("\n4. POLICZ ILE JEST STACJI")
print("-"*70)

count = conn.execute("SELECT COUNT(*) FROM stations").fetchone()[0]
print(f"Razem stacji w bazie: {count}")

# ============================================================================
# ZAPYTANIE 5: COUNT dla pomiarów
# ============================================================================

print("\n5. POLICZ ILE JEST POMIARÓW")
print("-"*70)

count = conn.execute("SELECT COUNT(*) FROM measurements").fetchone()[0]
print(f"Razem pomiarów w bazie: {count}")

# ============================================================================
# ZAPYTANIE 6: DISTINCT - Unikalne wartości
# ============================================================================

print("\n6. KTÓRE STACJE MAJĄ POMIARY?")
print("-"*70)

result = conn.execute("SELECT DISTINCT station FROM measurements").fetchall()

print(f"Liczba unikalnych stacji z pomiarami: {len(result)}\n")

for (station,) in result:
    print(f"Stacja: {station}")

# ============================================================================
#ZAPYTANIE 7: WHERE - Filtrowanie wyników, ile pomiarów dla konkretnej stacji
# ============================================================================
print("\n7. Dla stacji  które mają pomiary wypisz jaka jest ich liczba\n" \
"Podaj także sumę tych pomiarów dla sprawdzenia.")
print("-"*70)

for (station,) in conn.execute("SELECT DISTINCT station FROM measurements").fetchall():
    count = conn.execute(
        f"SELECT COUNT(*) FROM measurements WHERE station = '{station}'"
    ).fetchone()[0]
    print(f"Stacja: {station}, Liczba pomiarów: {count}")
    
    
# Zamknięcie połączenia
conn.close()

print("\n" + "="*70)
print("Przykład 1 zakończony!")
print("="*70)
