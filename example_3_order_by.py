"""
PRZYKŁAD 3: Sortowanie danych
Porządkowanie wyników zapytań
"""

import sqlite3

# Połączenie z bazą
conn = sqlite3.connect('air_quality.db')

print("="*70)
print("PRZYKŁAD 3: SORTOWANIE DANYCH (ORDER BY)")
print("="*70)

# ============================================================================
# ZAPYTANIE 1: Sortowanie alfabetyczne stacji
# ============================================================================

print("\n1️⃣ STACJE POSORTOWANE ALFABETYCZNIE")
print("-"*70)

result = conn.execute(
    "SELECT name, state FROM stations ORDER BY name ASC"
).fetchall()

print(f"Liczba stacji: {len(result)}\n")

for name, state in result:
    print(f"Stacja: {name} ({state})")

# ============================================================================
# ZAPYTANIE 2: Sortowanie odwrotne (Z na A)
# ============================================================================

print("\n2️⃣ STACJE W PORZĄDKU ODWROTNYM (Z-A)")
print("-"*70)

result = conn.execute(
    "SELECT name, state FROM stations ORDER BY name DESC"
).fetchall()

print(f"Liczba stacji: {len(result)}\n")

for name, state in result:
    print(f"Stacja: {name} ({state})")

# ============================================================================
# ZAPYTANIE 3: Sortowanie według szerokości geograficznej
# ============================================================================

print("\n3️⃣ STACJE POSORTOWANE WEDŁUG SZEROKOŚCI GEOGRAFICZNEJ")
print("-"*70)

result = conn.execute(
    "SELECT name, latitude, longitude FROM stations ORDER BY latitude DESC"
).fetchall()

print(f"Liczba stacji: {len(result)}\n")

for name, lat, lon in result:
    print(f"Stacja: {name} (Szer: {lat}, Dł: {lon})")

# ============================================================================
# ZAPYTANIE 4: Sortowanie pomiarów według daty
# ============================================================================

print("\n4️⃣ POMIARY DLA STACJI POSORTOWANE CHRONOLOGICZNIE")
print("-"*70)

station_id = "USW00094728"
result = conn.execute(
    f"SELECT date, precip, tobs FROM measurements WHERE station = '{station_id}' ORDER BY date ASC LIMIT 10"
).fetchall()

print(f"Pomiary dla stacji {station_id} (10 najwcześniejszych):\n")

for date, precip, tobs in result:
    print(f"Data: {date}, Opady: {precip}mm, Temperatura: {tobs}°C")

# ============================================================================
# ZAPYTANIE 5: Sortowanie i liczenie
# ============================================================================

print("\n5️⃣ STACJE POSORTOWANE WEDŁUG WYSOKOŚCI (OD NAJWYŻSZEJ)")
print("-"*70)

result = conn.execute(
    "SELECT name, elevation FROM stations ORDER BY elevation DESC LIMIT 5"
).fetchall()

print(f"5 najwyższych stacji:\n")

for name, elevation in result:
    print(f"Stacja: {name}, Wysokość: {elevation}m")

# Zamknięcie połączenia
conn.close()

print("\n" + "="*70)
print("✓ Przykład 3 zakończony!")
print("="*70)
