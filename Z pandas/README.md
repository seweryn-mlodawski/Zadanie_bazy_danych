# 📊 BAZA DANYCH JAKOŚCI POWIETRZA - DOKUMENTACJA

## 🚀 Szybki Start

### Krok 1: Uruchomienie skryptu inicjalizacyjnego

```bash
python database_setup.py
```

Lub użyj zaawansowanej wersji z klasą:

```bash
python database_advanced.py
```

### Krok 2: Użycie bazy w swoim kodzie

```python
import sqlite3

# Połączenie z bazą
conn = sqlite3.connect('air_quality.db')

# Zapytanie 1: Pobranie 5 stacji
result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
print(result)

# Zapytanie 2: Pobranie 5 pomiarów
result = conn.execute("SELECT * FROM measurements LIMIT 5").fetchall()
print(result)

# Zamknięcie
conn.close()
```

---

## 📁 STRUKTURA TABEL

### Tabela: `stations`
Zawiera informacje o stacjach pomiarowych

| Kolumna | Typ | Opis |
|---------|-----|------|
| id | INTEGER | Unikalny identyfikator stacji |
| station_name | TEXT | Nazwa stacji |
| gegrwx | REAL | Współrzędna geograficzna X |
| gegrwy | REAL | Współrzędna geograficzna Y |
| ... | ... | ... |

### Tabela: `measurements`
Zawiera wyniki pomiarów jakości powietrza

| Kolumna | Typ | Opis |
|---------|-----|------|
| id | INTEGER | Unikalny identyfikator pomiaru |
| stacja_id | INTEGER | Odniesienie do stacji |
| data_pomiaru | TEXT | Data pomiaru |
| wartość | REAL | Wartość zmierzona |
| ... | ... | ... |

---

## 📝 PRZYKŁADY ZAPYTAŃ

### Przykład 1: Pobieranie danych ze stacji
```python
import sqlite3

conn = sqlite3.connect('air_quality.db')

# Pobranie wszystkich stacji
result = conn.execute("SELECT * FROM stations").fetchall()

# Pobranie 5 stacji z nazwami
result = conn.execute("SELECT id, station_name FROM stations LIMIT 5").fetchall()

conn.close()
```

### Przykład 2: Pobieranie danych z pomiarów
```python
import sqlite3

conn = sqlite3.connect('air_quality.db')

# Pobranie wszystkich pomiarów
result = conn.execute("SELECT * FROM measurements").fetchall()

# Pobranie pomiarów dla określonej stacji
result = conn.execute("SELECT * FROM measurements WHERE stacja_id = 1").fetchall()

conn.close()
```

### Przykład 3: Użycie klasy AirQualityDatabase
```python
from database_advanced import AirQualityDatabase

# Inicjalizacja bazy (musi być utworzona wcześniej)
db = AirQualityDatabase("air_quality.db")
db.connect()

# Wykonanie zapytania
result = db.execute_query("SELECT * FROM stations LIMIT 5")
print(result)

# Zamknięcie
db.close()
```

### Przykład 4: Integracja z pandas
```python
import pandas as pd
import sqlite3

conn = sqlite3.connect('air_quality.db')

# Wczytanie tabeli do DataFrame
stations_df = pd.read_sql_query("SELECT * FROM stations", conn)
measurements_df = pd.read_sql_query("SELECT * FROM measurements", conn)

# Analiza danych
print(stations_df.head())
print(measurements_df.describe())

conn.close()
```

---

## 🔧 ZAAWANSOWANE OPERACJE

### Tworzenie indeksów
```python
import sqlite3

conn = sqlite3.connect('air_quality.db')
cursor = conn.cursor()

# Indeks dla stacji_id w pomiarach (przyspieszenie zapytań)
cursor.execute("CREATE INDEX IF NOT EXISTS idx_stacja_id ON measurements(stacja_id)")

conn.commit()
conn.close()
```

### Zapytania z JOINem
```python
import sqlite3

conn = sqlite3.connect('air_quality.db')

# Połączenie danych ze stacji i pomiarów
query = """
SELECT 
    s.station_name,
    m.data_pomiaru,
    m.wartość
FROM stations s
JOIN measurements m ON s.id = m.stacja_id
LIMIT 10
"""

result = conn.execute(query).fetchall()
print(result)

conn.close()
```

### Agregacja danych
```python
import sqlite3

conn = sqlite3.connect('air_quality.db')

# Średnia wartość na stację
query = """
SELECT 
    s.station_name,
    AVG(m.wartość) as średnia_wartość,
    COUNT(*) as liczba_pomiarów
FROM stations s
JOIN measurements m ON s.id = m.stacja_id
GROUP BY s.id, s.station_name
ORDER BY średnia_wartość DESC
"""

result = conn.execute(query).fetchall()
for row in result:
    print(row)

conn.close()
```

---

## 💡 PRZYDATNE KOMENDY

### Sprawdzenie struktury tabeli
```python
import sqlite3

conn = sqlite3.connect('air_quality.db')
cursor = conn.cursor()

# Szczegółowe informacje o kolumnach
cursor.execute("PRAGMA table_info(stations)")
print(cursor.fetchall())

conn.close()
```

### Liczba wierszy w tabelach
```python
import sqlite3

conn = sqlite3.connect('air_quality.db')

stations_count = conn.execute("SELECT COUNT(*) FROM stations").fetchone()[0]
measurements_count = conn.execute("SELECT COUNT(*) FROM measurements").fetchone()[0]

print(f"Stacje: {stations_count}")
print(f"Pomiary: {measurements_count}")

conn.close()
```

### Usunięcie bazy danych
```python
import os

if os.path.exists('air_quality.db'):
    os.remove('air_quality.db')
    print("Baza danych usunięta")
```

---

## ⚠️ ROZWIĄZYWANIE PROBLEMÓW

### Problem: "no such table: stations"
**Rozwiązanie:** Upewnij się, że uruchomiłeś skrypt inicjalizacyjny (`database_setup.py` lub `database_advanced.py`)

### Problem: "unable to open database file"
**Rozwiązanie:** Sprawdź uprawnienia do folderu i czy ścieżka jest poprawna

### Problem: "network error" przy pobieraniu plików CSV
**Rozwiązanie:** Sprawdź połączenie z internetem lub pobierz pliki ręcznie i załaduj je lokalnie

```python
# Zamiast:
df = pd.read_csv("https://...")

# Użyj:
df = pd.read_csv("/ścieżka/do/pliku.csv")
```

---

## 📚 DODATKOWE ZASOBY

- [Dokumentacja SQLite3 w Pythonie](https://docs.python.org/3/library/sqlite3.html)
- [Dokumentacja pandas io.sql](https://pandas.pydata.org/docs/user_guide/io.html#sql-queries)
- [SQL Tutorial](https://www.w3schools.com/sql/)

---

## 📝 NOTATKA

Pliki zawierają:
- **database_setup.py** - Prosty skrypt do inicjalizacji bazy
- **database_advanced.py** - Zaawansowana klasa `AirQualityDatabase` do zarządzania bazą
- **README.md** - Ta dokumentacja
