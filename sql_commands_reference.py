"""
KOMPLETNY PRZEGLĄD POLECEŃ SQL I METOD SQLITE3
Wszystkie polecenia z praktycznymi przykładami
"""

import sqlite3

# Połączenie z bazą
conn = sqlite3.connect('air_quality.db')
cursor = conn.cursor()

print("="*70)
print("KOMPLETNY PRZEGLĄD POLECEŃ SQL I METOD SQLITE3")
print("="*70)

# ============================================================================
# 1. POLECENIA DO POBIERANIA DANYCH (SELECT)
# ============================================================================

print("\n1️⃣ POLECENIA DO POBIERANIA DANYCH (SELECT)")
print("="*70)

print("\n📌 SELECT * - WSZYSTKIE KOLUMNY")
print("-"*70)
print("SQL: SELECT * FROM stations LIMIT 3")
result = cursor.execute("SELECT * FROM stations LIMIT 3").fetchall()
for row in result:
    print(f"  {row}")

print("\n📌 SELECT kolumny - WYBRANE KOLUMNY")
print("-"*70)
print("SQL: SELECT name, country FROM stations LIMIT 3")
result = cursor.execute("SELECT name, country FROM stations LIMIT 3").fetchall()
for name, country in result:
    print(f"  {name} ({country})")

print("\n📌 WHERE - WARUNKI")
print("-"*70)
print("SQL: SELECT * FROM stations WHERE country = 'US' LIMIT 3")
result = cursor.execute("SELECT * FROM stations WHERE country = 'US' LIMIT 3").fetchall()
for row in result:
    print(f"  {row}")

print("\n📌 WHERE + OPERATORY - ZAAWANSOWANE WARUNKI")
print("-"*70)

print("\nOperatory porównania:")
print("  =  → równy")
print("  !=, <> → nierówny")
print("  >  → większy")
print("  <  → mniejszy")
print("  >= → większy lub równy")
print("  <= → mniejszy lub równy")

print("\nPrzykład: SELECT * FROM measurements WHERE precip > '5'")
result = cursor.execute("SELECT station, precip FROM measurements WHERE precip > '5' LIMIT 3").fetchall()
for station, precip in result:
    print(f"  Stacja: {station}, Opady: {precip}mm")

print("\n📌 BETWEEN - ZAKRES")
print("-"*70)
print("SQL: SELECT * FROM measurements WHERE date BETWEEN '2020-01-01' AND '2020-01-10'")
result = cursor.execute("SELECT date, precip FROM measurements WHERE date BETWEEN '2020-01-01' AND '2020-01-10' LIMIT 3").fetchall()
for date, precip in result:
    print(f"  Data: {date}, Opady: {precip}mm")

print("\n📌 LIKE - WYSZUKIWANIE WZORU")
print("-"*70)
print("""
LIKE - wyszukiwanie tekstowe
  %  → dowolny tekst (0 lub więcej znaków)
  _  → jeden znak
""")
print("SQL: SELECT name FROM stations WHERE name LIKE '%New%'")
result = cursor.execute("SELECT name FROM stations WHERE name LIKE '%New%'").fetchall()
for (name,) in result:
    print(f"  {name}")

print("\n📌 IN - WIELE WARTOŚCI")
print("-"*70)
print("SQL: SELECT * FROM stations WHERE country IN ('US', 'CA') LIMIT 3")
result = cursor.execute("SELECT name, country FROM stations WHERE country IN ('US', 'CA') LIMIT 3").fetchall()
for name, country in result:
    print(f"  {name} ({country})")

print("\n📌 ORDER BY - SORTOWANIE")
print("-"*70)
print("Sortowanie rosnące (ASC - ascending)")
print("SQL: SELECT name FROM stations ORDER BY name ASC LIMIT 3")
result = cursor.execute("SELECT name FROM stations ORDER BY name ASC LIMIT 3").fetchall()
for (name,) in result:
    print(f"  {name}")

print("\nSortowanie malejące (DESC - descending)")
print("SQL: SELECT name FROM stations ORDER BY name DESC LIMIT 3")
result = cursor.execute("SELECT name FROM stations ORDER BY name DESC LIMIT 3").fetchall()
for (name,) in result:
    print(f"  {name}")

print("\n📌 GROUP BY - GRUPOWANIE")
print("-"*70)
print("SQL: SELECT station, COUNT(*) FROM measurements GROUP BY station LIMIT 3")
result = cursor.execute("SELECT station, COUNT(*) FROM measurements GROUP BY station LIMIT 3").fetchall()
for station, count in result:
    print(f"  {station}: {count} pomiarów")

print("\n📌 HAVING - FILTROWANIE PO GRUPOWANIU")
print("-"*70)
print("SQL: SELECT station, COUNT(*) FROM measurements GROUP BY station HAVING COUNT(*) > 100 LIMIT 3")
result = cursor.execute("SELECT station, COUNT(*) FROM measurements GROUP BY station HAVING COUNT(*) > 100 LIMIT 3").fetchall()
for station, count in result:
    print(f"  {station}: {count} pomiarów")

print("\n📌 LIMIT - OGRANICZENIE WIERSZY")
print("-"*70)
print("SQL: SELECT * FROM stations LIMIT 3")
result = cursor.execute("SELECT name FROM stations LIMIT 3").fetchall()
for (name,) in result:
    print(f"  {name}")

print("\n📌 OFFSET - POMINIĘCIE WIERSZY")
print("-"*70)
print("SQL: SELECT * FROM stations LIMIT 3 OFFSET 2")
result = cursor.execute("SELECT name FROM stations LIMIT 3 OFFSET 2").fetchall()
for (name,) in result:
    print(f"  {name}")

print("\n📌 DISTINCT - UNIKALNE WARTOŚCI")
print("-"*70)
print("SQL: SELECT DISTINCT country FROM stations")
result = cursor.execute("SELECT DISTINCT country FROM stations").fetchall()
for (country,) in result:
    print(f"  {country}")

# ============================================================================
# 2. FUNKCJE AGREGUJĄCE
# ============================================================================

print("\n\n2️⃣ FUNKCJE AGREGUJĄCE")
print("="*70)

print("\n📌 COUNT(*) - LICZENIE WIERSZY")
print("-"*70)
count = cursor.execute("SELECT COUNT(*) FROM stations").fetchone()[0]
print(f"Liczba stacji: {count}")

print("\n📌 COUNT(kolumna) - LICZENIE NIEPUSTYCH WARTOŚCI")
print("-"*70)
count = cursor.execute("SELECT COUNT(precip) FROM measurements WHERE precip > '0'").fetchone()[0]
print(f"Pomiary z opadami: {count}")

print("\n📌 SUM() - SUMA")
print("-"*70)
print("SQL: SELECT SUM(precip) FROM measurements")
result = cursor.execute("SELECT COUNT(*) FROM measurements WHERE precip > '0'").fetchone()[0]
print(f"Pomiary z opadami: {result}")

print("\n📌 AVG() - ŚREDNIA")
print("-"*70)
print("SQL: SELECT AVG(CAST(elevation AS REAL)) FROM stations")
avg = cursor.execute("SELECT AVG(CAST(elevation AS REAL)) FROM stations").fetchone()[0]
print(f"Średnia wysokość: {avg:.2f}m" if avg else "Brak danych")

print("\n📌 MIN() - MINIMUM")
print("-"*70)
min_val = cursor.execute("SELECT MIN(elevation) FROM stations").fetchone()[0]
print(f"Minimalna wysokość: {min_val}m")

print("\n📌 MAX() - MAKSIMUM")
print("-"*70)
max_val = cursor.execute("SELECT MAX(elevation) FROM stations").fetchone()[0]
print(f"Maksymalna wysokość: {max_val}m")

# ============================================================================
# 3. JOIN - ŁĄCZENIE TABEL
# ============================================================================

print("\n\n3️⃣ JOIN - ŁĄCZENIE TABEL")
print("="*70)

print("\n📌 INNER JOIN - TYLKO WSPÓLNE")
print("-"*70)
print("SQL: SELECT s.name, m.date FROM stations s JOIN measurements m ON s.station = m.station LIMIT 3")
result = cursor.execute("""
    SELECT s.name, m.date FROM stations s 
    JOIN measurements m ON s.station = m.station 
    LIMIT 3
""").fetchall()
for name, date in result:
    print(f"  Stacja: {name}, Data: {date}")

print("\n📌 LEFT JOIN - WSZYSTKO Z LEWEJ + WSPÓLNE")
print("-"*70)
print("SQL: SELECT s.name, COUNT(m.station) FROM stations s LEFT JOIN measurements m ON s.station = m.station GROUP BY s.station")
result = cursor.execute("""
    SELECT s.name, COUNT(m.station) FROM stations s 
    LEFT JOIN measurements m ON s.station = m.station 
    GROUP BY s.station
    LIMIT 3
""").fetchall()
for name, count in result:
    print(f"  {name}: {count} pomiarów")

# ============================================================================
# 4. OPERATORY LOGICZNE
# ============================================================================

print("\n\n4️⃣ OPERATORY LOGICZNE (AND, OR, NOT)")
print("="*70)

print("\n📌 AND - OBA WARUNKI MUSZĄ BYĆ SPEŁNIONE")
print("-"*70)
print("SQL: SELECT * FROM measurements WHERE precip > '5' AND tobs > '20' LIMIT 3")
result = cursor.execute("SELECT date, precip, tobs FROM measurements WHERE precip > '5' AND tobs > '20' LIMIT 3").fetchall()
for date, precip, tobs in result:
    print(f"  Data: {date}, Opady: {precip}mm, Temperatura: {tobs}°C")

print("\n📌 OR - JEDEN Z WARUNKÓW MUSI BYĆ SPEŁNIONY")
print("-"*70)
print("SQL: SELECT * FROM stations WHERE country = 'US' OR country = 'CA' LIMIT 3")
result = cursor.execute("SELECT name, country FROM stations WHERE country = 'US' OR country = 'CA' LIMIT 3").fetchall()
for name, country in result:
    print(f"  {name} ({country})")

print("\n📌 NOT - ZAPRZECZENIE")
print("-"*70)
print("SQL: SELECT * FROM measurements WHERE NOT precip = '0' LIMIT 3")
result = cursor.execute("SELECT date, precip FROM measurements WHERE NOT precip = '0' LIMIT 3").fetchall()
for date, precip in result:
    print(f"  Data: {date}, Opady: {precip}mm")

# ============================================================================
# 5. FUNKCJE SKALARNE
# ============================================================================

print("\n\n5️⃣ FUNKCJE SKALARNE")
print("="*70)

print("\n📌 CAST - KONWERSJA TYPU")
print("-"*70)
print("SQL: SELECT elevation, CAST(elevation AS REAL) FROM stations LIMIT 2")
result = cursor.execute("SELECT elevation, CAST(elevation AS REAL) FROM stations LIMIT 2").fetchall()
for text_val, num_val in result:
    print(f"  Tekst: {text_val}, Liczba: {num_val}")

print("\n📌 LENGTH - DŁUGOŚĆ TEKSTU")
print("-"*70)
print("SQL: SELECT name, LENGTH(name) FROM stations LIMIT 3")
result = cursor.execute("SELECT name, LENGTH(name) FROM stations LIMIT 3").fetchall()
for name, length in result:
    print(f"  {name} ({length} znaków)")

print("\n📌 UPPER/LOWER - WIELKIE/MAŁE LITERY")
print("-"*70)
print("SQL: SELECT UPPER(name), LOWER(name) FROM stations LIMIT 2")
result = cursor.execute("SELECT UPPER(name), LOWER(name) FROM stations LIMIT 2").fetchall()
for upper, lower in result:
    print(f"  Wielkie: {upper}, Małe: {lower}")

print("\n📌 SUBSTR - CZĘŚĆ TEKSTU")
print("-"*70)
print("SQL: SELECT name, SUBSTR(name, 1, 3) FROM stations LIMIT 3")
result = cursor.execute("SELECT name, SUBSTR(name, 1, 3) FROM stations LIMIT 3").fetchall()
for name, substr in result:
    print(f"  {name} → {substr}")

# ============================================================================
# 6. METODY PYTHON - sqlite3
# ============================================================================

print("\n\n6️⃣ METODY PYTHON - POBIERANIE WYNIKÓW")
print("="*70)

print("\n📌 .fetchone() - JEDEN WIERSZ")
print("-"*70)
result = cursor.execute("SELECT * FROM stations LIMIT 1").fetchone()
print(f"Typ: {type(result)}")
print(f"Wynik: {result}")

print("\n📌 .fetchone()[0] - PIERWSZY ELEMENT")
print("-"*70)
result = cursor.execute("SELECT COUNT(*) FROM stations").fetchone()[0]
print(f"Typ: {type(result)}")
print(f"Wynik: {result}")

print("\n📌 .fetchall() - WSZYSTKIE WIERSZE")
print("-"*70)
result = cursor.execute("SELECT name FROM stations LIMIT 3").fetchall()
print(f"Typ: {type(result)}")
print(f"Liczba wierszy: {len(result)}")
for row in result:
    print(f"  {row}")

print("\n📌 .fetchmany(n) - N WIERSZY")
print("-"*70)
result = cursor.execute("SELECT name FROM stations").fetchmany(3)
print(f"Typ: {type(result)}")
print(f"Liczba wierszy: {len(result)}")
for (name,) in result:
    print(f"  {name}")

# ============================================================================
# 7. METODY PYTHON - ZMIANY DANYCH
# ============================================================================

print("\n\n7️⃣ METODY PYTHON - ZMIANY DANYCH (INSERT/UPDATE/DELETE)")
print("="*70)

print("\n⚠️  UWAGA: Te operacje modyfikują bazę! Tutaj tylko pokazane.\n")

print("📌 .execute() - WYSŁANIE ZAPYTANIA")
print("-"*70)
print("""
cursor.execute("SELECT * FROM stations LIMIT 1")
  → Wysyła zapytanie do bazy
  → Zwraca cursor
""")

print("\n📌 .executemany() - WIELE ZAPYTAŃ NARAZ")
print("-"*70)
print("""
data = [('val1', 'val2'), ('val3', 'val4')]
cursor.executemany("INSERT INTO table VALUES (?, ?)", data)
  → Wstawia wiele wierszy naraz
""")

print("\n📌 .commit() - ZATWIERDZENIE ZMIAN")
print("-"*70)
print("""
cursor.execute("UPDATE stations SET name = 'Nowa' WHERE id = 1")
conn.commit()
  → Zatwierdza zmiany w bazie
  → Bez commit() zmiany są tylko w pamięci
""")

print("\n📌 .rollback() - COFNIĘCIE ZMIAN")
print("-"*70)
print("""
cursor.execute("DELETE FROM stations WHERE id = 1")
conn.rollback()
  → Cofa ostatnie zmiany
  → Działa tylko jeśli nie było commit()
""")

print("\n📌 .close() - ZAMKNIĘCIE POŁĄCZENIA")
print("-"*70)
print("""
conn.close()
  → Zamyka połączenie z bazą
  → Zwalnia zasoby
  → Zawsze rób to na koniec!
""")

# ============================================================================
# 8. METODY PYTHON - INFORMACJE
# ============================================================================

print("\n\n8️⃣ METODY PYTHON - INFORMACJE O BAZIE")
print("="*70)

print("\n📌 cursor.description - NAZWY KOLUMN")
print("-"*70)
cursor.execute("SELECT name, country FROM stations LIMIT 1")
result = cursor.fetchone()
column_names = [description[0] for description in cursor.description]
print(f"Kolumny: {column_names}")

print("\n📌 cursor.rowcount - LICZBA WIERSZY (dla INSERT/UPDATE/DELETE)")
print("-"*70)
print("Po execute() na INSERT/UPDATE/DELETE zwraca liczbę zmienionych wierszy")

print("\n📌 conn.total_changes - RAZEM ZMIAN W SESJI")
print("-"*70)
print(f"Razem zmian w tej sesji: {conn.total_changes}")

# ============================================================================
# 9. POLECENIA PRAGMA (METADANE)
# ============================================================================

print("\n\n9️⃣ POLECENIA PRAGMA (METADANE)")
print("="*70)

print("\n📌 PRAGMA table_info() - STRUKTURA TABELI")
print("-"*70)
cursor.execute("PRAGMA table_info(stations)")
result = cursor.fetchall()
print("Kolumny:")
for col in result[:3]:
    cid, name, col_type, notnull, dflt, pk = col
    print(f"  {name}: {col_type} (PK: {pk})")

print("\n📌 PRAGMA database_list - LISTA BAZ")
print("-"*70)
cursor.execute("PRAGMA database_list")
result = cursor.fetchall()
for seq, name, file in result:
    print(f"  {name}: {file if file else '(in-memory)'}")

# ============================================================================
# 10. PODSUMOWANIE
# ============================================================================

print("\n\n🔟 PODSUMOWANIE - SZYBKA ŚCIĄGAWKA")
print("="*70)

print("""
POBIERANIE DANYCH:
  SELECT *              → Wszystkie kolumny
  SELECT kolumny        → Wybrane kolumny
  WHERE                 → Warunkowe pobieranie
  ORDER BY              → Sortowanie
  GROUP BY              → Grupowanie
  LIMIT                 → Ograniczenie wierszy
  DISTINCT              → Unikalne wartości

FUNKCJE:
  COUNT(*)              → Liczenie wierszy
  SUM/AVG/MIN/MAX       → Statystyka
  CAST                  → Konwersja typu
  LENGTH/UPPER/LOWER    → Funkcje tekstowe

ŁĄCZENIE:
  JOIN / LEFT JOIN      → Łączenie tabel

LOGIKA:
  AND / OR / NOT        → Operatory

PYTHON - POBIERANIE:
  .fetchone()           → Jeden wiersz
  .fetchall()           → Wszystkie wiersze
  .fetchmany(n)         → N wierszy
  [0]                   → Pierwszy element

PYTHON - ZMIANA:
  .execute()            → Wysłanie zapytania
  .commit()             → Zatwierdzenie
  .rollback()           → Cofnięcie
  .close()              → Zamknięcie

METADANE:
  PRAGMA table_info()   → Struktura
  PRAGMA database_list  → Lista baz
""")

conn.close()

print("\n" + "="*70)
print("✓ Przegląd poleceń zakończony!")
print("="*70)
