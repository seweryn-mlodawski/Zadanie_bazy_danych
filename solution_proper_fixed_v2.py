# solution_proper.py
import csv
import sqlite3
from pathlib import Path

# ============================================================================
# KROK 1: Pobranie danych z pliku CSV
# ============================================================================

# Jeśli dane są już pobrane, wczytaj je z pliku lokalnego
csv_path_stations = "clean_stations.csv"
csv_path_measure = "clean_measure.csv"

# Sprawdzenie czy pliki istnieją, jeśli nie - trzeba je pobrać ręcznie
if not Path(csv_path_stations).exists():
    print(f"Plik {csv_path_stations} nie znaleziony!")
    print("Pobierz go z: https://uploads.kodilla.com/bootcamp/ds/06/clean_stations.csv")
    exit(1)

if not Path(csv_path_measure).exists():
    print(f"Plik {csv_path_measure} nie znaleziony!")
    print("Pobierz go z: https://uploads.kodilla.com/bootcamp/ds/06/clean_measure.csv")
    exit(1)

print("Pliki CSV znalezione")
# ============================================================================
# KROK 2: Odczyt pliku CSV i utworzenie struktury tabel
# ============================================================================

# Funkcja do czytania CSV i zwracania nagłówków oraz danych
def read_csv_file(filepath):
    """Wczytaj CSV i zwróć nagłówki oraz dane"""
    data = []
    headers = []
    
    with open(filepath, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        
        # Pierwszy wiersz to nagłówki
        headers = next(csv_reader)
        
        # Pozostałe wiersze to dane
        for row in csv_reader:
            data.append(row)
    
    return headers, data

# Wczytanie danych
stations_headers, stations_data = read_csv_file(csv_path_stations)
measure_headers, measure_data = read_csv_file(csv_path_measure)

print(f"Stacje: {len(stations_headers)} kolumn, {len(stations_data)} wierszy")
print(f"Pomiary: {len(measure_headers)} kolumn, {len(measure_data)} wierszy")
# ============================================================================
# KROK 3: Tworzenie bazy danych SQLite
# ============================================================================

# Połączenie z bazą (zostanie utworzona jeśli nie istnieje)
conn = sqlite3.connect("air_quality.db")
cursor = conn.cursor()

print("Baza danych utworzona")

# ============================================================================
# KROK 4: Tworzenie tabel
# ============================================================================

# Usunięcie starych tabel (jeśli istnieją)
cursor.execute("DROP TABLE IF EXISTS stations")
cursor.execute("DROP TABLE IF EXISTS measurements")

# Tworzenie tabeli STATIONS
print("\nTworzenie tabeli 'stations'...")
print(f"Kolumny: {stations_headers}")

# Budowanie komendy CREATE TABLE - wszystkie kolumny jako TEXT
# PRIMARY KEY tylko na 'station' (ma unikalne wartości)
create_stations_sql = "CREATE TABLE stations ("
for i, col_name in enumerate(stations_headers):
    if i == 0:
        # Pierwsza kolumna 'station' jako PRIMARY KEY
        create_stations_sql += f"{col_name} TEXT PRIMARY KEY"
    else:
        # Pozostałe kolumny jako TEXT
        create_stations_sql += f", {col_name} TEXT"
create_stations_sql += ")"

cursor.execute(create_stations_sql)
print("Tabela 'stations' utworzona")

# Tworzenie tabeli MEASUREMENTS
print("\nTworzenie tabeli 'measurements'...")
print(f"Kolumny: {measure_headers}")

# WAŻNE: NIE używamy PRIMARY KEY na 'station' bo ma duplikaty!
# Zamiast tego wszystkie kolumny są zwyczajnie TEXT
create_measure_sql = "CREATE TABLE measurements ("
for i, col_name in enumerate(measure_headers):
    # Wszystkie kolumny jako TEXT (bez PRIMARY KEY)
    if i == 0:
        create_measure_sql += f"{col_name} TEXT"
    else:
        create_measure_sql += f", {col_name} TEXT"
create_measure_sql += ")"

cursor.execute(create_measure_sql)
print("Tabela 'measurements' utworzona")
# ============================================================================
# KROK 5: Wstawianie danych do tabel
# ============================================================================

print("\nWstawianie danych...")

# Wstawianie danych STATIONS
placeholders = ", ".join(["?" for _ in stations_headers])
insert_stations_sql = f"INSERT INTO stations ({', '.join(stations_headers)}) VALUES ({placeholders})"

try:
    cursor.executemany(insert_stations_sql, stations_data)
    conn.commit()
    print(f"Wstawiono {len(stations_data)} wierszy do tabeli 'stations'")
except Exception as e:
    print(f"Błąd przy wstawianiu stacji: {e}")
    conn.close()
    exit(1)

# Wstawianie danych MEASUREMENTS
placeholders = ", ".join(["?" for _ in measure_headers])
insert_measure_sql = f"INSERT INTO measurements ({', '.join(measure_headers)}) VALUES ({placeholders})"

try:
    cursor.executemany(insert_measure_sql, measure_data)
    conn.commit()
    print(f"Wstawiono {len(measure_data)} wierszy do tabeli 'measurements'")
except Exception as e:
    print(f"Błąd przy wstawianiu pomiarów: {e}")
    conn.close()
    exit(1)

# ============================================================================
# KROK 6: WERYFIKACJA - ZAPYTANIA ZGODNE Z POLECENIEM
# ============================================================================

print("\n" + "="*70)
print("WERYFIKACJA - WYKONANIE ZAPYTAŃ")
print("="*70)

# ZAPYTANIE 1: SELECT * FROM stations LIMIT 5
print("\n🔍 Zapytanie: conn.execute(\"SELECT * FROM stations LIMIT 5\").fetchall()")
print("-"*70)

result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
print(f"Liczba wierszy: {len(result)}\n")

for i, row in enumerate(result, 1):
    print(f"Wiersz {i}: {row}")

# ZAPYTANIE 2: SELECT * FROM measurements LIMIT 5
print("\nZapytanie: conn.execute(\"SELECT * FROM measurements LIMIT 5\").fetchall()")
print("-"*70)

result = conn.execute("SELECT * FROM measurements LIMIT 5").fetchall()
print(f"Liczba wierszy: {len(result)}\n")

for i, row in enumerate(result, 1):
    print(f"Wiersz {i}: {row}")

# Dodatkowe statystyki
print("\n" + "="*70)
print("STATYSTYKI")
print("="*70)

count_stations = conn.execute("SELECT COUNT(*) FROM stations").fetchone()[0]
count_measurements = conn.execute("SELECT COUNT(*) FROM measurements").fetchone()[0]

print(f"Razem stacji: {count_stations}")
print(f"Razem pomiarów: {count_measurements}")

# ============================================================================
# KROK 7: UŻYCIE W KODZIE
# ============================================================================

print("\n" + "="*70)
print("GOTOWE DO UŻYCIA!")
print("="*70)

print("""
Teraz możesz używać bazy danych w swoim kodzie:

import sqlite3

# Połączenie z bazą
conn = sqlite3.connect('air_quality.db')

# PRZYKŁAD 1: Pobranie danych ze stacji
result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
print(result)

# PRZYKŁAD 2: Pobranie pomiarów
result = conn.execute("SELECT * FROM measurements LIMIT 5").fetchall()
print(result)

# PRZYKŁAD 3: Liczenie wierszy
count = conn.execute("SELECT COUNT(*) FROM stations").fetchone()[0]
print(f"Liczba stacji: {count}")

# PRZYKŁAD 4: Iteracja po wynikach
for row in conn.execute("SELECT * FROM stations LIMIT 3"):
    print(row)

# PRZYKŁAD 5: Pomiary dla konkretnej stacji
station_id = "USW00094728"
result = conn.execute(
    f"SELECT * FROM measurements WHERE station = '{station_id}' LIMIT 5"
).fetchall()
print(result)

# Zamknięcie połączenia
conn.close()
""")

# ============================================================================
# ZAMKNIĘCIE BAZY
# ============================================================================

conn.close()
print("Połączenie z bazą zamknięte")
print("Baza danych 'air_quality.db' jest gotowa do użytku!")