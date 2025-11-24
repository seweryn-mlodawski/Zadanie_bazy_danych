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

print("\n - POMIARY DLA KONKRETNEJ STACJI")
print("-"*70)

#station_id = "USW00094728" #inna stacja
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

print("\n - INFORMACJE O KONKRETNEJ STACJI")
print("-"*70)

#station_id = "USW00094728" #inna stacja do sprawdzenia jak sie zmienia wynik i zachowuje kod jeśli w tym miejscu podamy stację
result = conn.execute(
    f"SELECT * FROM stations WHERE station = '{station_id}'"
).fetchone()

if result:
    print(f"\nStacja: {station_id}")
    print(f"Nazwa: {result[4]}") # indeksy kolumn zaczynają się od 0 :) !! Pamięcaj o tym
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

print("\n - WSZYSTKIE STACJE Z USA")
print("-"*70)

result = conn.execute(
    "SELECT name, state FROM stations WHERE country = 'US'"
).fetchall()

print(f"Liczba stacji: {len(result)}\n")

for name, state in result:
    print(f"Stacja: {name} ({state})")

# ===========================================================================
# ZAPYTANIE 4a: Liczba stacji spoza USA
# ============================================================================
print("\n - LICZBA STACJI SPOZA USA")
print("-"*70)
count = conn.execute(
    "SELECT COUNT(*) FROM stations WHERE country != 'US'"
).fetchone()[0]

print(f"Razem stacji spoza USA: {count}")

#==========================================================================
# ZAPYTANIE 4b: Stacje uszeregowane według położenia najwyżej do najniżej
#==========================================================================
print("\n - STACJE USZEREGOWANE WEDŁUG WYSOKOŚCI")
print("-"*70)

#PIerwotne zapytanie powodowało błędne sortowanie alfanumeryczne -
#result = conn.execute(
#    "SELECT name, country, elevation FROM stations ORDER BY elevation DESC"
#).fetchall()

#Kolumna elevation jest w bazie zapisana jako tekst
#ORDER BY domyślnie sortuje alfanumerycznie w takim wypadku
#CAST na typ liczbowy rozwiązuje problem

# Poprawione zapytanie, aby porównać wartości liczbowe jako REAL, 
# Tutaj CAST(elevation AS REAL) wymusza sortowanie według wartości liczbowej wysokości.

result = conn.execute(
    "SELECT name, country, elevation FROM stations ORDER BY CAST(elevation AS REAL) DESC"
).fetchall()

for name, country, elevation in result:
    print(f"Kraj: {country}, Stacja: {name}, Wysokość: {elevation}m")

# ============================================================================
# ZAPYTANIE 4: Pomiary z konkretnego dnia
# ============================================================================

print("\n - WSZYSTKIE POMIARY Z KONKRETNEGO DNIA")
print("-"*70)

date = "2011-01-13"
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

print("\n - POMIARY Z OPADAMI WIĘKSZYMI NIŻ 5MM")
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
