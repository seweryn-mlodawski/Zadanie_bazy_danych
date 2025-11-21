# 🚀 SZYBKI PRZEWODNIK - BAZA DANYCH JAKOŚCI POWIETRZA

## 📋 Spis zawartości

1. [Instalacja](#instalacja)
2. [Szybki start](#szybki-start)
3. [Pierwsza baza](#pierwsza-baza)
4. [Podstawowe zapytania](#podstawowe-zapytania)
5. [Zaawansowane operacje](#zaawansowane-operacje)

---

## 🔧 Instalacja

### Wymagane biblioteki:

```bash
pip install pandas sqlite3
```

Lub wszystko na raz:

```bash
pip install pandas
```

> **Uwaga**: `sqlite3` jest wbudowany w Pythona, nie trzeba go instalować

---

## 🚀 Szybki Start

### Krok 1️⃣ - Utwórz bazę danych

```bash
python database_setup.py
```

Lub z zaawansowaną klasą:

```bash
python database_advanced.py
```

### Krok 2️⃣ - Testuj bazę

```bash
python test_database.py
```

### Krok 3️⃣ - Używaj w swoim kodzie

```python
import sqlite3

conn = sqlite3.connect('air_quality.db')
result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
print(result)
conn.close()
```

---

## 🗄️ Pierwsza baza

### Kod minimalny (3 linijki)

```python
import pandas as pd
import sqlite3

# Wczytanie danych z URL
stations = pd.read_csv("https://uploads.kodilla.com/bootcamp/ds/06/clean_stations.csv")
measurements = pd.read_csv("https://uploads.kodilla.com/bootcamp/ds/06/clean_measure.csv")

# Zapis do bazy
conn = sqlite3.connect('air_quality.db')
stations.to_sql('stations', conn, if_exists='replace', index=False)
measurements.to_sql('measurements', conn, if_exists='replace', index=False)
conn.close()

print("✅ Baza stworzona!")
```

---

## 📝 Podstawowe Zapytania

### ✅ 1. Pobranie wszystkich stacji

```python
import sqlite3

conn = sqlite3.connect('air_quality.db')
result = conn.execute("SELECT * FROM stations").fetchall()

for row in result:
    print(row)

conn.close()
```

### ✅ 2. Pobranie 5 stacji (z limitacją)

```python
conn = sqlite3.connect('air_quality.db')
result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
print(result)
conn.close()
```

### ✅ 3. Pobranie określonych kolumn

```python
conn = sqlite3.connect('air_quality.db')
result = conn.execute("SELECT station_name FROM stations").fetchall()
print(result)
conn.close()
```

### ✅ 4. Liczba wierszy w tabeli

```python
conn = sqlite3.connect('air_quality.db')
count = conn.execute("SELECT COUNT(*) FROM stations").fetchone()[0]
print(f"Liczba stacji: {count}")
conn.close()
```

### ✅ 5. Pobranie pomiarów (limit 10)

```python
conn = sqlite3.connect('air_quality.db')
result = conn.execute("SELECT * FROM measurements LIMIT 10").fetchall()
for row in result:
    print(row)
conn.close()
```

---

## 🎯 Zaawansowane Operacje

### 🔹 Używanie DataFrame (pandas)

```python
import pandas as pd
import sqlite3

conn = sqlite3.connect('air_quality.db')

# Wczytanie całej tabeli
df = pd.read_sql_query("SELECT * FROM stations", conn)

# Wyświetlenie informacji
print(df.head())           # Pierwsze 5 wierszy
print(df.info())           # Informacje o kolumnach
print(df.describe())       # Statystyka

conn.close()
```

### 🔹 Filtrowanie danych

```python
conn = sqlite3.connect('air_quality.db')

# WHERE - filtrowanie
result = conn.execute("""
    SELECT * FROM measurements 
    WHERE wartość > 100
    LIMIT 5
""").fetchall()

print(result)
conn.close()
```

### 🔹 Sortowanie danych

```python
conn = sqlite3.connect('air_quality.db')

# ORDER BY - sortowanie
result = conn.execute("""
    SELECT station_name FROM stations 
    ORDER BY station_name ASC
    LIMIT 5
""").fetchall()

print(result)
conn.close()
```

### 🔹 Agregacja (COUNT, AVG, SUM, MIN, MAX)

```python
conn = sqlite3.connect('air_quality.db')

# Średnia wartość
avg = conn.execute("""
    SELECT AVG(wartość) FROM measurements
""").fetchone()[0]

print(f"Średnia wartość: {avg}")

# Liczba pomiarów
count = conn.execute("""
    SELECT COUNT(*) FROM measurements
""").fetchone()[0]

print(f"Liczba pomiarów: {count}")

conn.close()
```

### 🔹 Grupowanie (GROUP BY)

```python
conn = sqlite3.connect('air_quality.db')

# Statystyka na stację
result = conn.execute("""
    SELECT 
        stacja_id,
        COUNT(*) as liczba_pomiarow,
        AVG(wartość) as srednia
    FROM measurements
    GROUP BY stacja_id
    ORDER BY liczba_pomiarow DESC
    LIMIT 10
""").fetchall()

for row in result:
    print(row)

conn.close()
```

### 🔹 JOIN - łączenie tabel

```python
conn = sqlite3.connect('air_quality.db')

result = conn.execute("""
    SELECT 
        s.station_name,
        m.wartość,
        m.data_pomiaru
    FROM stations s
    JOIN measurements m ON s.id = m.stacja_id
    LIMIT 10
""").fetchall()

for row in result:
    print(row)

conn.close()
```

---

## 💡 Szybkie Wzory

### Szablon: Prosty SELECT

```python
import sqlite3

conn = sqlite3.connect('air_quality.db')
result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
print(result)
conn.close()
```

### Szablon: SELECT z warunkiami

```python
import sqlite3

conn = sqlite3.connect('air_quality.db')
result = conn.execute("""
    SELECT * FROM measurements 
    WHERE stacja_id = 1
    LIMIT 5
""").fetchall()
print(result)
conn.close()
```

### Szablon: Pracą z DataFrame

```python
import pandas as pd
import sqlite3

conn = sqlite3.connect('air_quality.db')
df = pd.read_sql_query("SELECT * FROM stations", conn)
conn.close()

# Analiza
print(df.head(10))
print(df.describe())
```

### Szablon: Zaawansowane zapytanie

```python
import sqlite3

conn = sqlite3.connect('air_quality.db')
result = conn.execute("""
    SELECT 
        column1,
        COUNT(*) as count,
        AVG(column2) as average
    FROM table_name
    WHERE condition
    GROUP BY column1
    ORDER BY count DESC
    LIMIT 10
""").fetchall()

for row in result:
    print(row)

conn.close()
```

---

## 🐛 Rozwiązywanie Problemów

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|------------|
| `no such table` | Tabela nie istnieje | Uruchom `database_setup.py` |
| `unable to open database file` | Błędna ścieżka | Sprawdź lokalizację pliku |
| `network error` | Brak internetu | Pobierz CSV ręcznie |
| `memory error` | Zbyt wiele danych | Użyj `LIMIT` w zapytaniach |

---

## 📚 Przydatne Linki

- 📖 [Dokumentacja sqlite3](https://docs.python.org/3/library/sqlite3.html)
- 📊 [Dokumentacja pandas SQL](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html)
- 🗂️ [SQL Tutorial W3Schools](https://www.w3schools.com/sql/)

---

## ✨ Podsumowanie

| Co chcę | Komenda |
|---------|---------|
| **Stworzyć bazę** | `python database_setup.py` |
| **Przetestować** | `python test_database.py` |
| **Pobrać dane** | `conn.execute("SELECT * FROM stations").fetchall()` |
| **Wczytać do pandas** | `pd.read_sql_query("SELECT * FROM stations", conn)` |
| **Policzyć wiersze** | `conn.execute("SELECT COUNT(*) FROM table").fetchone()[0]` |
| **Filtrować** | Dodaj `WHERE` do zapytania |
| **Sortować** | Dodaj `ORDER BY` do zapytania |

---

**Happy coding! 🎉**
