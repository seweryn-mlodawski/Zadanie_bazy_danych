"""
PEŁNY SCENARIUSZ TESTOWY - KOMPLETNY PRZYKŁAD UŻYCIA
Pokazuje wszystkie możliwości pracy z bazą danych
"""

import sqlite3
import pandas as pd
from datetime import datetime


def main():
    print("\n" + "="*80)
    print("🎯 KOMPLETNY SCENARIUSZ TESTOWY BAZY DANYCH")
    print("="*80)
    print(f"⏰ Data i czas: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # ====================================================================
        # ETAP 1: POŁĄCZENIE Z BAZĄ
        # ====================================================================
        print("\n" + "-"*80)
        print("ETAP 1: Nawiązanie połączenia z bazą danych")
        print("-"*80)
        
        conn = sqlite3.connect('air_quality.db')
        cursor = conn.cursor()
        print("✅ Połączenie nawiązane pomyślnie")
        
        # ====================================================================
        # ETAP 2: SPRAWDZENIE TABEL
        # ====================================================================
        print("\n" + "-"*80)
        print("ETAP 2: Sprawdzenie istniejących tabel")
        print("-"*80)
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]
        print(f"Tabele w bazie: {tables}")
        
        if "stations" not in tables or "measurements" not in tables:
            print("⚠️  UWAGA: Baza nie jest prawidłowo zainicjalizowana!")
            print("   Uruchom: python database_setup.py")
            return
        
        # ====================================================================
        # ETAP 3: INFORMACJE O TABELACH
        # ====================================================================
        print("\n" + "-"*80)
        print("ETAP 3: Szczegółowe informacje o tabelach")
        print("-"*80)
        
        # Tabela stations
        print("\n📋 TABELA: stations")
        cursor.execute("PRAGMA table_info(stations)")
        columns = cursor.fetchall()
        for col in columns:
            print(f"   {col[1]:20} : {col[2]}")
        
        stations_count = conn.execute("SELECT COUNT(*) FROM stations").fetchone()[0]
        print(f"   Liczba wierszy: {stations_count}")
        
        # Tabela measurements
        print("\n📋 TABELA: measurements")
        cursor.execute("PRAGMA table_info(measurements)")
        columns = cursor.fetchall()
        for col in columns:
            print(f"   {col[1]:20} : {col[2]}")
        
        measurements_count = conn.execute("SELECT COUNT(*) FROM measurements").fetchone()[0]
        print(f"   Liczba wierszy: {measurements_count}")
        
        # ====================================================================
        # ETAP 4: ZAPYTANIE 1 - PODSTAWOWY SELECT
        # ====================================================================
        print("\n" + "-"*80)
        print("ETAP 4: Zapytanie 1 - SELECT * FROM stations LIMIT 5")
        print("-"*80)
        
        result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
        cursor.execute("SELECT * FROM stations LIMIT 1")
        col_names = [description[0] for description in cursor.description]
        
        print(f"Kolumny: {col_names}")
        print(f"Liczba wierszy: {len(result)}\n")
        
        for i, row in enumerate(result, 1):
            print(f"Wiersz {i}:")
            for j, col in enumerate(col_names):
                print(f"  {col}: {row[j]}")
            print()
        
        # ====================================================================
        # ETAP 5: ZAPYTANIE 2 - MEASUREMENTS
        # ====================================================================
        print("-"*80)
        print("ETAP 5: Zapytanie 2 - SELECT * FROM measurements LIMIT 5")
        print("-"*80)
        
        result = conn.execute("SELECT * FROM measurements LIMIT 5").fetchall()
        cursor.execute("SELECT * FROM measurements LIMIT 1")
        col_names = [description[0] for description in cursor.description]
        
        print(f"Kolumny: {col_names}")
        print(f"Liczba wierszy: {len(result)}\n")
        
        for i, row in enumerate(result, 1):
            print(f"Wiersz {i}: {row}")
        
        # ====================================================================
        # ETAP 6: ZAPYTANIA AGREGUJĄCE
        # ====================================================================
        print("\n" + "-"*80)
        print("ETAP 6: Zapytania agregujące")
        print("-"*80)
        
        # COUNT
        total_stations = conn.execute("SELECT COUNT(*) FROM stations").fetchone()[0]
        print(f"\n✓ Liczba stacji: {total_stations}")
        
        # COUNT dla measurements
        total_measurements = conn.execute("SELECT COUNT(*) FROM measurements").fetchone()[0]
        print(f"✓ Liczba pomiarów: {total_measurements}")
        
        # Średnia wartość (jeśli istnieje kolumna wartości)
        try:
            result = conn.execute("SELECT AVG(wartość) FROM measurements").fetchone()
            if result[0] is not None:
                print(f"✓ Średnia wartość pomiarów: {result[0]:.2f}")
        except Exception as e:
            print(f"  (Kolumna 'wartość' niedostępna)")
        
        # ====================================================================
        # ETAP 7: PRACA Z PANDAS
        # ====================================================================
        print("\n" + "-"*80)
        print("ETAP 7: Wczytanie danych do pandas DataFrame")
        print("-"*80)
        
        # Wczytanie stacji
        stations_df = pd.read_sql_query("SELECT * FROM stations", conn)
        print(f"\n📊 DataFrame 'stations':")
        print(f"  Kształt: {stations_df.shape} (wiersze, kolumny)")
        print(f"  Kolumny: {list(stations_df.columns)}")
        print(f"  Typy danych:\n{stations_df.dtypes}")
        
        # Wczytanie pomiarów
        measurements_df = pd.read_sql_query("SELECT * FROM measurements", conn)
        print(f"\n📊 DataFrame 'measurements':")
        print(f"  Kształt: {measurements_df.shape} (wiersze, kolumny)")
        print(f"  Kolumny: {list(measurements_df.columns)}")
        print(f"  Typy danych:\n{measurements_df.dtypes}")
        
        # ====================================================================
        # ETAP 8: ANALIZA DANYCH
        # ====================================================================
        print("\n" + "-"*80)
        print("ETAP 8: Podstawowa analiza danych")
        print("-"*80)
        
        print("\n📈 Statystyka dla DataFrame 'stations':")
        print(stations_df.describe())
        
        print("\n📈 Statystyka dla DataFrame 'measurements':")
        try:
            print(measurements_df.describe())
        except Exception as e:
            print(f"  Niedostępne (brak kolumn numerycznych)")
        
        # ====================================================================
        # ETAP 9: ZAPYTANIA ZAAWANSOWANE
        # ====================================================================
        print("\n" + "-"*80)
        print("ETAP 9: Zaawansowane zapytania SQL")
        print("-"*80)
        
        # Zapytanie 1: Pierwsze 3 stacje z ID
        print("\n1️⃣ Pierwsze 3 stacje:")
        result = conn.execute("""
            SELECT * FROM stations 
            ORDER BY ROWID 
            LIMIT 3
        """).fetchall()
        for row in result:
            print(f"  {row}")
        
        # Zapytanie 2: Statystyka na stację (jeśli możliwe)
        print("\n2️⃣ Liczba pomiarów (jeśli dostępne):")
        try:
            result = conn.execute("""
                SELECT COUNT(*) as liczba_pomiarow
                FROM measurements
            """).fetchall()
            print(f"  Razem pomiarów: {result[0][0]}")
        except Exception as e:
            print(f"  Niedostępne")
        
        # ====================================================================
        # ETAP 10: EKSPORT DANYCH
        # ====================================================================
        print("\n" + "-"*80)
        print("ETAP 10: Eksport danych")
        print("-"*80)
        
        # Zapis do CSV
        stations_df.to_csv('stations_export.csv', index=False)
        print("\n✓ Dane 'stations' wyeksportowane do: stations_export.csv")
        
        measurements_df.to_csv('measurements_export.csv', index=False)
        print("✓ Dane 'measurements' wyeksportowane do: measurements_export.csv")
        
        # ====================================================================
        # ETAP 11: VERYFIKACJA
        # ====================================================================
        print("\n" + "-"*80)
        print("ETAP 11: Podsumowanie i weryfikacja")
        print("-"*80)
        
        print(f"""
✅ RAPORT KOŃCOWY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Tabela: stations
   • Liczba wierszy: {stations_count}
   • Liczba kolumn: {len(stations_df.columns)}
   • Kolumny: {', '.join(stations_df.columns)}

📊 Tabela: measurements
   • Liczba wierszy: {measurements_count}
   • Liczba kolumn: {len(measurements_df.columns)}
   • Kolumny: {', '.join(measurements_df.columns)}

💾 Pliki wyeksportowane:
   • stations_export.csv
   • measurements_export.csv

✨ STATUS: WSZYSTKO DZIAŁA PRAWIDŁOWO! ✨
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """)
        
        # ====================================================================
        # ZAMKNIĘCIE POŁĄCZENIA
        # ====================================================================
        conn.close()
        print("\n✓ Połączenie z bazą danych zamknięte")
        
    except sqlite3.Error as db_error:
        print(f"\n❌ BŁĄD BAZY DANYCH: {db_error}")
        print("   Uruchom skrypt inicjalizacyjny: python database_setup.py")
    except Exception as e:
        print(f"\n❌ BŁĄD: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("\n" + "="*80)
        print("🏁 KONIEC SCENARIUSZA TESTOWEGO")
        print("="*80 + "\n")


if __name__ == "__main__":
    main()
