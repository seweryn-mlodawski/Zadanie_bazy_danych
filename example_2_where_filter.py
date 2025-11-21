"""
PRZYKŁAD 2: Filtrowanie danych z WHERE
Pobieranie danych spełniających określony warunek
"""

import sqlite3

# Połączenie z bazą
conn = sqlite3.connect('air_quality.db')

print("="*70)
print("PRZYKŁAD 2: FILTROWANIE DANYCH (WHERE)")
print("="*70)

# ============================================================================
# ZAPYTANIE 1: Pomiary dla konkretnej stacji
# ============================================================================

print("\n1️⃣ - POMIARY DLA KONKRETNEJ STACJI")
print("-"*70)

#station_id = "USW00094728"
station_id = "USC00519281"
result = conn.execute(
    f"SELECT * FROM measurements WHERE station = '{station_id}' LIMIT 5"
).fetchall()

print(f"Pomiary dla stacji {station_id}:")
print(f"Liczba wyników: {len(result)}\n")

for i, row in enumerate(result, 1):
    print(f"Pomiar {i}: {row}")

# ============================================================================
# ZAPYTANIE 2: Informacje o konkretnej stacji
# ============================================================================

print("\n2️⃣ - INFORMACJE O KONKRETNEJ STACJI")
print("-"*70)

#station_id = "USW00094728"
result = conn.execute(
    f"SELECT * FROM stations WHERE station = '{station_id}'"
).fetchone()

if result:
    print(f"\nStacja: {station_id}")
    print(f"Nazwa: {result[4]}")
    print(f"Kraj: {result[5]}")
    print(f"Stan: {result[6]}")
    print(f"Szerokość geograficzna: {result[1]}")
    print(f"Długość geograficzna: {result[2]}")
    print(f"Wysokość: {result[3]}")
else:
    print(f"Stacja {station_id} nie znaleziona")

# ============================================================================
# ZAPYTANIE 3: Stacje z konkretnego kraju
# ============================================================================

print("\n3️⃣ - WSZYSTKIE STACJE Z USA")
print("-"*70)

result = conn.execute(
    "SELECT name, state FROM stations WHERE country = 'US'"
).fetchall()

print(f"Liczba stacji: {len(result)}\n")

for name, state in result:
    print(f"Stacja: {name} ({state})")

# ============================================================================
# ZAPYTANIE 4: Pomiary z konkretnego dnia
# ============================================================================

print("\n4️⃣ - WSZYSTKIE POMIARY Z KONKRETNEGO DNIA")
print("-"*70)

date = "2020-01-01"
result = conn.execute(
    f"SELECT station, date, precip, tobs FROM measurements WHERE date = '{date}' LIMIT 5"
).fetchall()

print(f"Pomiary z dnia {date}:")
print(f"Liczba wyników: {len(result)}\n")

for station, date, precip, tobs in result:
    print(f"Stacja: {station}, Opady: {precip}mm, Temperatura: {tobs}°C")

# ============================================================================
# ZAPYTANIE 5: WHERE z operatorem >
# ============================================================================

print("\n5️⃣ - POMIARY Z OPADAMI WIĘKSZYMI NIŻ 5MM")
print("-"*70)

result = conn.execute(
    "SELECT station, date, precip FROM measurements WHERE precip > '5' LIMIT 10"
).fetchall()

print(f"Liczba wyników: {len(result)}\n")

for station, date, precip in result:
    print(f"Data: {date}, Stacja: {station}, Opady: {precip}mm")

# Zamknięcie połączenia
conn.close()

print("\n" + "="*70)
print("✓ Przykład 2 zakończony!")
print("="*70)
