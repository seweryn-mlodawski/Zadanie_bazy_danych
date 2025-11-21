import pandas as pd
import sqlite3
from pathlib import Path

# ============================================================================
# POBRANIE I WCZYTANIE DANYCH
# ============================================================================

# URL do plików CSV
url_stations = "https://uploads.kodilla.com/bootcamp/ds/06/clean_stations.csv"
url_measure = "https://uploads.kodilla.com/bootcamp/ds/06/clean_measure.csv"

# Wczytanie danych z URL
print("📥 Pobieranie plików...")
stations_df = pd.read_csv(url_stations)
measure_df = pd.read_csv(url_measure)

print(f"✓ Stacje: {stations_df.shape[0]} wierszy, {stations_df.shape[1]} kolumn")
print(f"✓ Pomiary: {measure_df.shape[0]} wierszy, {measure_df.shape[1]} kolumn")

# ============================================================================
# TWORZENIE BAZY DANYCH
# ============================================================================

# Ścieżka do bazy danych
db_path = "air_quality.db"

# Połączenie z bazą danych (zostanie utworzona jeśli nie istnieje)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print(f"\n✓ Baza danych '{db_path}' utworzona")

# ============================================================================
# TWORZENIE TABELI STACJI
# ============================================================================

# Usunięcie tabeli jeśli istnieje (opcjonalnie)
cursor.execute("DROP TABLE IF EXISTS stations")

# Pobranie informacji o typach kolumn z pandas
print("\n📋 Struktura tabeli STATIONS:")
for col in stations_df.columns:
    print(f"   - {col}: {stations_df[col].dtype}")

# Wpisanie danych stacji do bazy danych
stations_df.to_sql("stations", conn, if_exists="replace", index=False)

print("✓ Tabela 'stations' utworzona i wypełniona")

# ============================================================================
# TWORZENIE TABELI POMIARÓW
# ============================================================================

# Usunięcie tabeli jeśli istnieje (opcjonalnie)
cursor.execute("DROP TABLE IF EXISTS measurements")

print("\n📋 Struktura tabeli MEASUREMENTS:")
for col in measure_df.columns:
    print(f"   - {col}: {measure_df[col].dtype}")

# Wpisanie danych pomiarów do bazy danych
measure_df.to_sql("measurements", conn, if_exists="replace", index=False)

print("✓ Tabela 'measurements' utworzona i wypełniona")

# ============================================================================
# WERYFIKACJA
# ============================================================================

print("\n" + "="*70)
print("WERYFIKACJA - WYNIKI ZAPYTAŃ")
print("="*70)

# Test 1: SELECT * FROM stations LIMIT 5
print("\n🔍 Zapytanie: SELECT * FROM stations LIMIT 5")
print("-" * 70)
result_stations = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
column_names = [description[0] for description in conn.execute("SELECT * FROM stations LIMIT 1").description]
print(f"Kolumny: {column_names}")
print(f"Liczba wierszy: {len(result_stations)}")
for i, row in enumerate(result_stations, 1):
    print(f"Wiersz {i}: {row}")

# Test 2: SELECT * FROM measurements LIMIT 5
print("\n🔍 Zapytanie: SELECT * FROM measurements LIMIT 5")
print("-" * 70)
result_measurements = conn.execute("SELECT * FROM measurements LIMIT 5").fetchall()
column_names = [description[0] for description in conn.execute("SELECT * FROM measurements LIMIT 1").description]
print(f"Kolumny: {column_names}")
print(f"Liczba wierszy: {len(result_measurements)}")
for i, row in enumerate(result_measurements, 1):
    print(f"Wiersz {i}: {row}")

# Test 3: Liczba rekordów
print("\n🔍 Zapytanie: COUNT(*)")
print("-" * 70)
count_stations = conn.execute("SELECT COUNT(*) FROM stations").fetchone()[0]
count_measurements = conn.execute("SELECT COUNT(*) FROM measurements").fetchone()[0]
print(f"Stacje: {count_stations} rekordów")
print(f"Pomiary: {count_measurements} rekordów")

# ============================================================================
# ZATWIERDZENIE ZMIAN I ZAMKNIĘCIE
# ============================================================================

# Zatwierdzenie zmian
conn.commit()

print("\n" + "="*70)
print("✅ BAZA DANYCH ZOSTAŁ POMYŚLNIE UTWORZONA")
print("="*70)
print(f"📁 Lokalizacja: {Path(db_path).absolute()}")
print("\n💡 Możesz teraz użyć kodu do połączenia:")
print("""
import sqlite3

# Połączenie z bazą danych
conn = sqlite3.connect('air_quality.db')

# Pobranie danych ze stacji
result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
print(result)

# Pobranie danych z pomiarów
result = conn.execute("SELECT * FROM measurements LIMIT 5").fetchall()
print(result)

# Zamknięcie połączenia
conn.close()
""")

# Zamknięcie połączenia
conn.close()
