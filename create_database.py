import pandas as pd
from sqlalchemy import create_engine, text # Importujemy text do wykonywania zapytań SQL
import os # komunikacja z systemem plików

# Konfiguracja nazw plików
DB_FILE = 'air_quality.db'
STATIONS_FILE = 'clean_stations.csv'
MEASURE_FILE = 'clean_measure.csv'

def create_database():
    print(f"Rozpoczynam tworzenie bazy danych: {DB_FILE}")
    
    # 1. Tworzenie silnika SQLAlchemy
    
    db_url = f"sqlite:///{DB_FILE}" # sqlite:/// oznacza lokalny plik bazy danych
    engine = create_engine(db_url) # Tworzymy silnik bazy danych SQLite

    try:
        # --- KROK 2: Wczytanie stacji ---
        if os.path.exists(STATIONS_FILE):
            print(f"Wczytywanie pliku: {STATIONS_FILE}...")
            df_stations = pd.read_csv(STATIONS_FILE)
            
            # Zapis do bazy przy użyciu silnika SQLAlchemy con=engine - podłączenie silnika (patrz 2 linijka)
            # if_exists='replace' podmieni tabelę, jeśli już istnieje
            df_stations.to_sql('stations', con=engine, if_exists='replace', index=False)
            print("Tabela 'stations' utworzona.")
        else:
            print(f"BŁĄD: Nie znaleziono pliku {STATIONS_FILE}")

        # --- KROK 3: Wczytanie pomiarów ---
        if os.path.exists(MEASURE_FILE):
            print(f"Wczytywanie pliku: {MEASURE_FILE}...")
            df_measure = pd.read_csv(MEASURE_FILE)
            
            # Zapis do bazy
            df_measure.to_sql('measurements', con=engine, if_exists='replace', index=False)
            print("Tabela 'measurements' utworzona.")
        else:
            print(f"BŁĄD: Nie znaleziono pliku {MEASURE_FILE}")

        # --- KROK 4: Weryfikacja ---
        print("\nSPRAWDZENIE (za pomocą SELECT pobieramy kilka rekordów):")
        
        # Nawiązujemy połączenie z silnika, aby wykonać surowe zapytanie SQL
        with engine.connect() as conn:
            # Używamy text() do bezpiecznego przekazania zapytania SQL
            query = text("SELECT * FROM stations LIMIT 5")
            results = conn.execute(query).fetchall()
            
            for row in results:
                print(row)

    except Exception as e:
        print(f"\nBŁĄD: Wystąpił krytyczny błąd: {e}")
        print("Wskazówka: Upewnij się, że masz zainstalowane biblioteki:")
                
    finally:
        print(f"\nGotowe! Baza '{DB_FILE}' jest gotowa do użycia.")

if __name__ == "__main__":
    create_database()