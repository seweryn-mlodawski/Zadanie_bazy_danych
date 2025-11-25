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

print("\nSTACJE POSORTOWANE ALFABETYCZNIE")
print("-"*70)

result = conn.execute(
    "SELECT name, state FROM stations ORDER BY name ASC" #domyślnie rosnąco ASCending
).fetchall()

print(f"Liczba stacji: {len(result)}\n")

for name, state in result:
    print(f"Stacja: {name} ({state})")

# ============================================================================
# ZAPYTANIE 2: Sortowanie odwrotne (Z na A)
# ============================================================================

print("\nSTACJE W PORZĄDKU ODWROTNYM (Z-A)")
print("-"*70)

result = conn.execute(
    "SELECT name, state FROM stations ORDER BY name DESC" #malejąco DESCending
).fetchall()

print(f"Liczba stacji: {len(result)}\n")

for name, state in result:
    print(f"Stacja: {name} ({state})")

# ============================================================================
# ZAPYTANIE 3: Sortowanie według szerokości geograficznej
# ============================================================================

print("\nSTACJE POSORTOWANE WEDŁUG SZEROKOŚCI GEOGRAFICZNEJ")
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

print("\nPOMIARY DLA STACJI POSORTOWANE CHRONOLOGICZNIE")
print("-"*70)

station_id = "USC00519397"  # Przykładowa stacja
#station_id = "USW00094728" # Nie ma takiej stacji w example_2_where_filter.py" 
result = conn.execute(
    f"SELECT date, precip, tobs FROM measurements WHERE station = '{station_id}' ORDER BY date ASC LIMIT 10"
).fetchall()

print(f"Pomiary dla stacji {station_id} (10 najwcześniejszych):\n")

for date, precip, tobs in result:
    print(f"Data: {date}, Opady: {precip}mm, Temperatura: {tobs}°C")
if len(result) == 0:
    print("Brak wyników dla podanej stacji.")
        

# ============================================================================
# ZAPYTANIE 5: Sortowanie i liczenie
# ============================================================================

print("\nSTACJE POSORTOWANE WEDŁUG WYSOKOŚCI (OD NAJWYŻSZEJ)")
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
print("Przykład 3 zakończony!")
print("="*70)
