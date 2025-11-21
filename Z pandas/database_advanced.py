"""
BAZA DANYCH JAKOŚCI POWIETRZA
Skrypt do zarządzania bazą SQLite zawierającą dane o stacjach i pomiarach
"""

import pandas as pd
import sqlite3
from pathlib import Path
from datetime import datetime


class AirQualityDatabase:
    """Klasa do zarządzania bazą danych jakości powietrza"""
    
    def __init__(self, db_path="air_quality.db"):
        """Inicjalizacja bazy danych"""
        self.db_path = db_path
        self.conn = None
        self.cursor = None
    
    def connect(self):
        """Nawiązanie połączenia z bazą danych"""
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        print(f"✓ Połączenie z bazą danych '{self.db_path}' ustanowione")
    
    def create_from_csv(self, stations_url, measurements_url):
        """
        Tworzenie bazy danych z plików CSV
        
        Args:
            stations_url: URL do pliku stacji
            measurements_url: URL do pliku pomiarów
        """
        print("\n" + "="*70)
        print("TWORZENIE BAZY DANYCH")
        print("="*70)
        
        # Pobranie danych
        print("\n📥 Pobieranie plików...")
        stations_df = pd.read_csv(stations_url)
        measurements_df = pd.read_csv(measurements_url)
        
        print(f"✓ Stacje: {stations_df.shape[0]} wierszy, {stations_df.shape[1]} kolumn")
        print(f"✓ Pomiary: {measurements_df.shape[0]} wierszy, {measurements_df.shape[1]} kolumn")
        
        # Połączenie z bazą
        self.connect()
        
        # Usunięcie starych tabel
        self.cursor.execute("DROP TABLE IF EXISTS stations")
        self.cursor.execute("DROP TABLE IF EXISTS measurements")
        
        # Wpisanie danych
        print("\n📝 Wpisywanie danych do bazy...")
        stations_df.to_sql("stations", self.conn, if_exists="replace", index=False)
        measurements_df.to_sql("measurements", self.conn, if_exists="replace", index=False)
        
        self.conn.commit()
        print("✓ Tabela 'stations' utworzona i wypełniona")
        print("✓ Tabela 'measurements' utworzona i wypełniona")
    
    def execute_query(self, query, fetch_one=False):
        """
        Wykonanie zapytania SQL
        
        Args:
            query: Zapytanie SQL
            fetch_one: Jeśli True, zwraca jeden wiersz; False zwraca wszystkie
        
        Returns:
            Wynik zapytania
        """
        result = self.cursor.execute(query)
        if fetch_one:
            return result.fetchone()
        return result.fetchall()
    
    def display_table_info(self):
        """Wyświetlenie informacji o tabelach"""
        print("\n" + "="*70)
        print("INFORMACJE O TABELACH")
        print("="*70)
        
        # Informacje o tabeli stations
        print("\n📋 TABELA: stations")
        print("-" * 70)
        schema = self.execute_query("PRAGMA table_info(stations)")
        for col in schema:
            print(f"  {col[1]:20} {col[2]}")
        count = self.execute_query("SELECT COUNT(*) FROM stations", fetch_one=True)[0]
        print(f"  Liczba rekordów: {count}")
        
        # Informacje o tabeli measurements
        print("\n📋 TABELA: measurements")
        print("-" * 70)
        schema = self.execute_query("PRAGMA table_info(measurements)")
        for col in schema:
            print(f"  {col[1]:20} {col[2]}")
        count = self.execute_query("SELECT COUNT(*) FROM measurements", fetch_one=True)[0]
        print(f"  Liczba rekordów: {count}")
    
    def preview_data(self, table, limit=5):
        """
        Wyświetlenie podglądu danych z tabeli
        
        Args:
            table: Nazwa tabeli (stations lub measurements)
            limit: Liczba wierszy do wyświetlenia
        """
        print(f"\n🔍 Zapytanie: SELECT * FROM {table} LIMIT {limit}")
        print("-" * 70)
        
        result = self.execute_query(f"SELECT * FROM {table} LIMIT {limit}")
        
        # Pobranie nazw kolumn
        self.cursor.execute(f"SELECT * FROM {table} LIMIT 1")
        column_names = [description[0] for description in self.cursor.description]
        
        print(f"Kolumny: {column_names}")
        print(f"Liczba wierszy w wyniku: {len(result)}\n")
        
        for i, row in enumerate(result, 1):
            print(f"Wiersz {i}: {row}")
    
    def verify_data(self):
        """Weryfikacja danych w bazie"""
        print("\n" + "="*70)
        print("WERYFIKACJA DANYCH")
        print("="*70)
        
        # Podsumowanie
        count_stations = self.execute_query("SELECT COUNT(*) FROM stations", fetch_one=True)[0]
        count_measurements = self.execute_query("SELECT COUNT(*) FROM measurements", fetch_one=True)[0]
        
        print(f"\n📊 Podsumowanie:")
        print(f"  Stacje: {count_stations} rekordów")
        print(f"  Pomiary: {count_measurements} rekordów")
        
        # Pierwsze 5 stacji
        self.preview_data("stations", 5)
        
        # Pierwsze 5 pomiarów
        self.preview_data("measurements", 5)
    
    def close(self):
        """Zamknięcie połączenia"""
        if self.conn:
            self.conn.close()
            print("\n✓ Połączenie zamknięte")


# ============================================================================
# GŁÓWNA CZĘŚĆ PROGRAMU
# ============================================================================

if __name__ == "__main__":
    # URL do plików
    stations_url = "https://uploads.kodilla.com/bootcamp/ds/06/clean_stations.csv"
    measurements_url = "https://uploads.kodilla.com/bootcamp/ds/06/clean_measure.csv"
    
    # Tworzenie bazy danych
    db = AirQualityDatabase("air_quality.db")
    db.create_from_csv(stations_url, measurements_url)
    
    # Wyświetlenie informacji
    db.display_table_info()
    
    # Weryfikacja danych
    db.verify_data()
    
    # Dodatkowe przykłady zapytań
    print("\n" + "="*70)
    print("DODATKOWE PRZYKŁADY ZAPYTAŃ")
    print("="*70)
    
    # Przykład 1: Liczba pomiarów na stację
    print("\n1️⃣ Liczba pomiarów na stację:")
    result = db.execute_query("""
        SELECT COUNT(*) as liczba_pomiarow 
        FROM measurements
    """, fetch_one=True)
    print(f"   Razem pomiarów: {result[0]}")
    
    # Przykład 2: Średnia wartość z pomiarów
    print("\n2️⃣ Przykład zapytania ze statistics:")
    schema = db.execute_query("PRAGMA table_info(measurements)")
    numeric_cols = [col[1] for col in schema if col[2] in ['INTEGER', 'REAL']]
    if numeric_cols:
        print(f"   Kolumny numeryczne: {numeric_cols}")
    
    # Zamknięcie bazy danych
    print("\n" + "="*70)
    print("✅ BAZA DANYCH PRZYGOTOWANA DO UŻYTKU")
    print("="*70)
    print("\n💡 Przykład użycia w kodzie:")
    print("""
# Manualne łączenie się z bazą
import sqlite3

conn = sqlite3.connect('air_quality.db')

# Pobieranie danych ze stacji
result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
print(result)

# Pobieranie danych z pomiarów  
result = conn.execute("SELECT * FROM measurements LIMIT 5").fetchall()
print(result)

conn.close()

# Lub przy użyciu naszej klasy:
from database_advanced import AirQualityDatabase

db = AirQualityDatabase()
db.connect()
result = db.execute_query("SELECT * FROM stations LIMIT 5")
print(result)
db.close()
    """)
    
    db.close()
