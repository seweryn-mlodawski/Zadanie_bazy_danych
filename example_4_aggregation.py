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

print("\n1️⃣ POLICZ WSZYSTKIE STACJE I POMIARY")
print("-"*70)

count_stations = conn.execute("SELECT COUNT(*) FROM stations").fetchone()[0]
count_measurements = conn.execute("SELECT COUNT(*) FROM measurements").fetchone()[0]

print(f"Razem stacji w bazie: {count_stations}")
print(f"Razem pomiarów w bazie: {count_measurements}")

# ============================================================================
# ZAPYTANIE 2: AVG - Średnia wartość
# ============================================================================

print("\n2️⃣ ŚREDNIA TEMPERATURA Z WSZYSTKICH POMIARÓW")
print("-"*70)

# Uwaga: dane są tekstowe, więc AVG może nie działać idealnie
# Pokazuję koncepcję
try:
    result = conn.execute(
        "SELECT COUNT(*) as liczba_pomiarow FROM measurements WHERE tobs != ''"
    ).fetchone()
    print(f"Liczba pomiarów z temperaturą: {result[0]}")
except Exception as e:
    print(f"Błąd: {e}")

# ============================================================================
# ZAPYTANIE 3: MAX i MIN - Maksimum i minimum
# ============================================================================

print("\n3️⃣ NAJWYŻSZA I NAJNIŻSZA STACJA")
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

print("\n4️⃣ ILE POMIARÓW DLA KAŻDEJ STACJI")
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

print("\n5️⃣ POMIARY Z OPADAMI (PRECIP > 0)")
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

print("\n6️⃣ STATYSTYKA DLA KONKRETNEJ STACJI")
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
print("✓ Przykład 4 zakończony!")
print("="*70)
