"""
TESTOWANIE BAZY DANYCH - SPRAWDZENIE DZIAŁANIA
Skrypt do weryfikacji poprawności działania bazy danych
"""

import sqlite3
import pandas as pd
from pathlib import Path


def test_database_exists():
    """Test 1: Sprawdzenie czy baza istnieje"""
    print("\n🧪 TEST 1: Sprawdzenie istnienia bazy danych")
    print("-" * 70)
    
    db_path = Path("air_quality.db")
    if db_path.exists():
        print(f"✅ PASS: Baza danych istnieje ({db_path.absolute()})")
        print(f"   Rozmiar: {db_path.stat().st_size / 1024:.2f} KB")
        return True
    else:
        print("❌ FAIL: Baza danych nie istnieje")
        print("   Uruchom najpierw skrypt: python database_setup.py")
        return False


def test_connection():
    """Test 2: Nawiązanie połączenia"""
    print("\n🧪 TEST 2: Nawiązanie połączenia z bazą")
    print("-" * 70)
    
    try:
        conn = sqlite3.connect("air_quality.db")
        cursor = conn.cursor()
        print("✅ PASS: Połączenie nawiązane pomyślnie")
        conn.close()
        return True
    except Exception as e:
        print(f"❌ FAIL: Błąd połączenia: {e}")
        return False


def test_tables_exist():
    """Test 3: Sprawdzenie istnienia tabel"""
    print("\n🧪 TEST 3: Sprawdzenie istnienia tabel")
    print("-" * 70)
    
    try:
        conn = sqlite3.connect("air_quality.db")
        cursor = conn.cursor()
        
        # Pobranie listy tabel
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]
        
        print(f"Znalezione tabele: {tables}")
        
        if "stations" in tables:
            print("✅ PASS: Tabela 'stations' istnieje")
        else:
            print("❌ FAIL: Tabela 'stations' nie istnieje")
            conn.close()
            return False
        
        if "measurements" in tables:
            print("✅ PASS: Tabela 'measurements' istnieje")
        else:
            print("❌ FAIL: Tabela 'measurements' nie istnieje")
            conn.close()
            return False
        
        conn.close()
        return True
    except Exception as e:
        print(f"❌ FAIL: Błąd: {e}")
        return False


def test_data_exists():
    """Test 4: Sprawdzenie czy dane się wczytały"""
    print("\n🧪 TEST 4: Sprawdzenie czy dane się wczytały")
    print("-" * 70)
    
    try:
        conn = sqlite3.connect("air_quality.db")
        
        # Liczba wierszy w stacjach
        stations_count = conn.execute("SELECT COUNT(*) FROM stations").fetchone()[0]
        print(f"Wierszy w 'stations': {stations_count}")
        
        if stations_count > 0:
            print("✅ PASS: Tabela 'stations' zawiera dane")
        else:
            print("❌ FAIL: Tabela 'stations' jest pusta")
            conn.close()
            return False
        
        # Liczba wierszy w pomiarach
        measurements_count = conn.execute("SELECT COUNT(*) FROM measurements").fetchone()[0]
        print(f"Wierszy w 'measurements': {measurements_count}")
        
        if measurements_count > 0:
            print("✅ PASS: Tabela 'measurements' zawiera dane")
        else:
            print("❌ FAIL: Tabela 'measurements' jest pusta")
            conn.close()
            return False
        
        conn.close()
        return True
    except Exception as e:
        print(f"❌ FAIL: Błąd: {e}")
        return False


def test_query_stations():
    """Test 5: Wykonanie zapytania SELECT * FROM stations"""
    print("\n🧪 TEST 5: Zapytanie SELECT * FROM stations LIMIT 5")
    print("-" * 70)
    
    try:
        conn = sqlite3.connect("air_quality.db")
        result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
        
        print(f"Pobranych wierszy: {len(result)}")
        
        if len(result) > 0:
            print("✅ PASS: Zapytanie wykonane pomyślnie")
            print("\nPierwsze 5 wierszy:")
            
            # Pobranie nazw kolumn
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM stations LIMIT 1")
            column_names = [description[0] for description in cursor.description]
            
            print(f"Kolumny: {column_names}")
            for i, row in enumerate(result, 1):
                print(f"Wiersz {i}: {row}")
        else:
            print("❌ FAIL: Brak wyników")
            conn.close()
            return False
        
        conn.close()
        return True
    except Exception as e:
        print(f"❌ FAIL: Błąd zapytania: {e}")
        return False


def test_query_measurements():
    """Test 6: Wykonanie zapytania SELECT * FROM measurements"""
    print("\n🧪 TEST 6: Zapytanie SELECT * FROM measurements LIMIT 5")
    print("-" * 70)
    
    try:
        conn = sqlite3.connect("air_quality.db")
        result = conn.execute("SELECT * FROM measurements LIMIT 5").fetchall()
        
        print(f"Pobranych wierszy: {len(result)}")
        
        if len(result) > 0:
            print("✅ PASS: Zapytanie wykonane pomyślnie")
            print("\nPierwsze 5 wierszy:")
            
            # Pobranie nazw kolumn
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM measurements LIMIT 1")
            column_names = [description[0] for description in cursor.description]
            
            print(f"Kolumny: {column_names}")
            for i, row in enumerate(result, 1):
                print(f"Wiersz {i}: {row}")
        else:
            print("❌ FAIL: Brak wyników")
            conn.close()
            return False
        
        conn.close()
        return True
    except Exception as e:
        print(f"❌ FAIL: Błąd zapytania: {e}")
        return False


def test_pandas_integration():
    """Test 7: Integracja z pandas"""
    print("\n🧪 TEST 7: Integracja z pandas")
    print("-" * 70)
    
    try:
        conn = sqlite3.connect("air_quality.db")
        
        # Wczytanie do DataFrame
        stations_df = pd.read_sql_query("SELECT * FROM stations", conn)
        measurements_df = pd.read_sql_query("SELECT * FROM measurements", conn)
        
        print("✅ PASS: Dane wczytane do pandas DataFrame")
        print(f"\nStacje DataFrame:")
        print(f"  Kształt: {stations_df.shape}")
        print(f"  Kolumny: {list(stations_df.columns)}")
        print(f"\nPomiary DataFrame:")
        print(f"  Kształt: {measurements_df.shape}")
        print(f"  Kolumny: {list(measurements_df.columns)}")
        
        conn.close()
        return True
    except Exception as e:
        print(f"❌ FAIL: Błąd: {e}")
        return False


def test_table_schema():
    """Test 8: Sprawdzenie schematu tabel"""
    print("\n🧪 TEST 8: Sprawdzenie schematu tabel")
    print("-" * 70)
    
    try:
        conn = sqlite3.connect("air_quality.db")
        cursor = conn.cursor()
        
        # Schema tabeli stations
        print("\nTabela: STATIONS")
        cursor.execute("PRAGMA table_info(stations)")
        schema = cursor.fetchall()
        for col in schema:
            print(f"  {col[1]:20} -> {col[2]}")
        
        # Schema tabeli measurements
        print("\nTabela: MEASUREMENTS")
        cursor.execute("PRAGMA table_info(measurements)")
        schema = cursor.fetchall()
        for col in schema:
            print(f"  {col[1]:20} -> {col[2]}")
        
        print("\n✅ PASS: Schemat tabel pobierany pomyślnie")
        
        conn.close()
        return True
    except Exception as e:
        print(f"❌ FAIL: Błąd: {e}")
        return False


def main():
    """Główna funkcja uruchamiająca testy"""
    print("\n" + "="*70)
    print("🧪 TESTY BAZY DANYCH JAKOŚCI POWIETRZA")
    print("="*70)
    
    tests = [
        test_database_exists,
        test_connection,
        test_tables_exist,
        test_data_exists,
        test_query_stations,
        test_query_measurements,
        test_pandas_integration,
        test_table_schema,
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ UNEXPECTED ERROR: {e}")
            results.append(False)
    
    # Podsumowanie
    print("\n" + "="*70)
    print("📊 PODSUMOWANIE TESTÓW")
    print("="*70)
    
    passed = sum(results)
    total = len(results)
    
    print(f"\nTest: {passed}/{total} pomyślnie")
    
    if passed == total:
        print("\n✅ WSZYSTKIE TESTY POMINIĘTE!")
        print("Baza danych jest gotowa do użytku.")
    else:
        print(f"\n⚠️  {total - passed} test(ów) nie powiodło się")
        print("Sprawdź błędy wyżej i uruchom skrypt inicjalizacyjny.")
    
    print("\n" + "="*70)


if __name__ == "__main__":
    main()
