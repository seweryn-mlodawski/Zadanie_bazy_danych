"""
PRZYKŁAD 4: Agregacja danych (COUNT, AVG, SUM, MAX, MIN)
Obliczanie statystyk na danych
"""

import sqlite3

# Połączenie z bazą
conn = sqlite3.connect('air_quality.db')

print("="*70)
print("PRZYKŁAD 4: AGREGACJA DANYCH")
print("="*70)

# ============================================================================
# ZAPYTANIE 1: COUNT - Liczenie wierszy
# ============================================================================

print("\nPOLICZ WSZYSTKIE STACJE I POMIARY")
print("-"*70)

count_stations = conn.execute("SELECT COUNT(*) FROM stations").fetchone()[0]
count_measurements = conn.execute("SELECT COUNT(*) FROM measurements").fetchone()[0]

print(f"Razem stacji w bazie: {count_stations}")
print(f"Razem pomiarów w bazie: {count_measurements}")

# ============================================================================
# ZAPYTANIE 2: AVG - Średnia wartość
# ============================================================================

print("\nŚREDNIA TEMPERATURA ZE WSZYSTKICH POMIARÓW")
print("-"*70)


# Obliczanie średniej temperatury CAST na REAL dla poprawności obliczeń
# != '' aby pominąć puste wartości

result = conn.execute(
    "SELECT AVG(CAST(tobs AS REAL)) FROM measurements WHERE tobs != ''"
).fetchone()[0]

print(f"Średnia temperatura: {result:.2f}K")



# Pokaż tylko wyniki z pustymi pomiarami
result_empty = conn.execute(
    "SELECT COUNT(*) FROM measurements WHERE tobs = ''"
).fetchone()[0]

print(f"Ilość pomiarów bez temperatury: {result_empty}")
print(f"Lista pomiarów bez temperatury (pierwsze 5):")

result_empty_list = conn.execute(
    "SELECT * FROM measurements WHERE tobs = '' LIMIT 5"
).fetchall()

if len(result_empty_list) == 0:
    print(">>Brak wyników z pustymi pomiarami<<")
else:
    for row in result_empty_list:
        print(row)

result = conn.execute("""
    SELECT 
        COUNT(*) as pomiary,
        AVG(CAST(tobs AS REAL)) as srednia,
        MIN(CAST(tobs AS REAL)) as minimum,
        MAX(CAST(tobs AS REAL)) as maksimum
    FROM measurements
    WHERE tobs != ''
""").fetchone()

count, avg, min_val, max_val = result
print(f"Minimum: {min_val}K")
print(f"Maksimum: {max_val}K")
print(f"Średnia: {avg:.2f}K")


# ============================================================================
# ZAPYTANIE 3: MAX i MIN - Maksimum i minimum
# ============================================================================

print("\nNAJWYŻSZA I NAJNIŻSZA STACJA")
print("-"*70)

# Znajdujemy ID stacji z najwyższą wysokością
result_max = conn.execute(
    "SELECT name, elevation FROM stations ORDER BY elevation DESC LIMIT 1"
).fetchone()

result_min = conn.execute(
    "SELECT name, elevation FROM stations ORDER BY elevation ASC LIMIT 1"
).fetchone()

if result_max:
    print(f"Najwyższa stacja: {result_max[0]} (wysokość: {result_max[1]}m)")

if result_min:
    print(f"Najniższa stacja: {result_min[0]} (wysokość: {result_min[1]}m)")

# ============================================================================
# ZAPYTANIE 4: Pomiary na stację - ile pomiarów dla każdej stacji
# ============================================================================

print("\nILE POMIARÓW DLA KAŻDEJ STACJI")
print("-"*70)

result = conn.execute(
    "SELECT station, COUNT(*) as liczba_pomiarow FROM measurements GROUP BY station"
).fetchall()

print(f"Liczba stacji z pomiarami: {len(result)}\n")

for station, count in result:
    print(f"Stacja: {station}, Pomiary: {count}")

# ============================================================================
# ZAPYTANIE 5: Pomiary z opadami - ile pomiarów ma opady > 0
# ============================================================================

print("\nPOMIARY Z OPADAMI (PRECIP > 0)")
print("-"*70)

result = conn.execute(
    "SELECT COUNT(*) FROM measurements WHERE precip > '0'"
).fetchone()

count_with_precip = result[0]
total_measurements = conn.execute("SELECT COUNT(*) FROM measurements").fetchone()[0]

print(f"Pomiary z opadami: {count_with_precip}")
print(f"Razem pomiarów: {total_measurements}")

percentage = (count_with_precip / total_measurements * 100) if total_measurements > 0 else 0
print(f"Procent pomiarów z opadami: {percentage:.2f}%")

# ============================================================================
# ZAPYTANIE 6: Statystyka dla konkretnej stacji
# ============================================================================

print("\nSTATYSTYKA DLA KONKRETNEJ STACJI")
print("-"*70)

station_id = "USW00094728"

# Liczba pomiarów
count = conn.execute(
    f"SELECT COUNT(*) FROM measurements WHERE station = '{station_id}'"
).fetchone()[0]

# Pomiary z opadami
precip_count = conn.execute(
    f"SELECT COUNT(*) FROM measurements WHERE station = '{station_id}' AND precip > '0'"
).fetchone()[0]

print(f"Stacja: {station_id}")
print(f"Razem pomiarów: {count}")
print(f"Pomiarów z opadami: {precip_count}")
print(f"Pomiarów bez opadów: {count - precip_count}")

# Zamknięcie połączenia
conn.close()

print("\n" + "="*70)
print("Przykład 4 zakończony!")
print("="*70)
