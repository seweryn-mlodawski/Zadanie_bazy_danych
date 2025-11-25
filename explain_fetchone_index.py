"""
WYJAŚNIENIE: .fetchone()[0]
Rozbicie i praktyczne przykłady
"""

import sqlite3

# Połączenie z bazą
conn = sqlite3.connect('air_quality.db')
cursor = conn.cursor()

print("="*70)
print("WYJAŚNIENIE: .fetchone()[0]")
print("="*70)

# ============================================================================
# 1. ROZBICIE NA CZĘŚCI
# ============================================================================

print("\n1️⃣ ROZBICIE NA CZĘŚCI")
print("-"*70)

print("""
.fetchone()[0]
└──┬──┘└──┬──┘
  │       └─ Indeks 0 - PIERWSZY element krotki
  └─ Metoda pobierająca JEDEN wiersz

CO SIĘ DZIEJE:

.fetchone()     → Pobiera JEDEN wiersz z wyniku
                → Zwraca KROTKĘ (tuple) lub None jeśli brak danych
                
[0]             → Indeks - dostęp do PIERWSZEGO elementu
                → W Pythonie indeksowanie zaczyna się od 0
                
Razem:          → Pobierz JEDEN wiersz i weź PIERWSZY element
""")

# ============================================================================
# 2. PORÓWNANIE: fetchone() vs fetchone()[0]
# ============================================================================

print("\n2️⃣ PORÓWNANIE: fetchone() vs fetchone()[0]")
print("-"*70)

print("\nBEZ [0] - .fetchone()")
print("-"*70)

result_without = cursor.execute("SELECT COUNT(*) FROM stations").fetchone()
print(f"Typ: {type(result_without)}")
print(f"Wartość: {result_without}")
print(f"Wynik: KROTKA z jednym elementem")

print("\n\nZ [0] - .fetchone()[0]")
print("-"*70)

result_with = cursor.execute("SELECT COUNT(*) FROM stations").fetchone()[0]
print(f"Typ: {type(result_with)}")
print(f"Wartość: {result_with}")
print(f"Wynik: LICZBA (int)")

# ============================================================================
# 3. PRAKTYCZNE PRZYKŁADY
# ============================================================================

print("\n\n3️⃣ PRAKTYCZNE PRZYKŁADY")
print("-"*70)

# Przykład 1: Liczenie wierszy
print("\nPRZYKŁAD 1: Liczenie stacji")
print("-"*70)

# ❌ Źle - zwraca krotkę
count_wrong = cursor.execute("SELECT COUNT(*) FROM stations").fetchone()
print(f"❌ Bez [0]: {count_wrong}")
print(f"   Typ: {type(count_wrong)}")
print(f"   Problem: Nie mogę bezpośrednio użyć w print()")

# ✅ Dobrze - zwraca liczbę
count_right = cursor.execute("SELECT COUNT(*) FROM stations").fetchone()[0]
print(f"\n✅ Z [0]: {count_right}")
print(f"   Typ: {type(count_right)}")
print(f"   Mogę bezpośrednio użyć w operacjach")

# Przykład 2: Pobieranie jednej wartości
print("\n\nPRZYKŁAD 2: Pobieranie nazwy jednej stacji")
print("-"*70)

# Zapytanie zwracające jeden wiersz z dwoma kolumnami
query_result = cursor.execute("SELECT name, country FROM stations LIMIT 1").fetchone()
print(f"fetchone() bez indeksu: {query_result}")
print(f"Typ: {type(query_result)}")
print(f"To krotka z 2 elementami")

print(f"\nfetchone()[0]: {query_result[0]}")
print(f"To PIERWSZY element krotki (nazwa stacji)")

print(f"\nfetchone()[1]: {query_result[1]}")
print(f"To DRUGI element krotki (kraj)")

# Przykład 3: Pobieranie maksymalnej wartości
print("\n\nPRZYKŁAD 3: Pobieranie maksymalnej wysokości")
print("-"*70)

max_elevation_wrong = cursor.execute(
    "SELECT MAX(elevation) FROM stations"
).fetchone()
print(f"❌ Bez [0]: {max_elevation_wrong}")
print(f"   Typ: {type(max_elevation_wrong)}")

max_elevation_right = cursor.execute(
    "SELECT MAX(elevation) FROM stations"
).fetchone()[0]
print(f"\n✅ Z [0]: {max_elevation_right}")
print(f"   Typ: {type(max_elevation_right)}")

# ============================================================================
# 4. STRUKTURA KROTKI - JAK DZIAŁA INDEKSOWANIE
# ============================================================================

print("\n\n4️⃣ STRUKTURA KROTKI - JAK DZIAŁA INDEKSOWANIE")
print("-"*70)

print("""
Kiedy zapytanie zwraca JEDEN wiersz z N kolumnami:

Zapytanie: SELECT name, country, elevation FROM stations LIMIT 1

fetchone() zwraca:
  ('New York', 'US', '10')
   ↑          ↑     ↑
   [0]        [1]   [2]

.fetchone()[0]  → 'New York'
.fetchone()[1]  → 'US'
.fetchone()[2]  → '10'
""")

# Praktyka
result = cursor.execute("SELECT name, country, elevation FROM stations LIMIT 1").fetchone()
print(f"\nPraktyka:")
print(f"  result = {result}")
print(f"  result[0] = {result[0]}")
print(f"  result[1] = {result[1]}")
print(f"  result[2] = {result[2]}")

# ============================================================================
# 5. FETCHONE() vs FETCHALL() vs FETCHMANY()
# ============================================================================

print("\n\n5️⃣ PORÓWNANIE: fetchone() vs fetchall() vs fetchmany()")
print("-"*70)

print("""
.fetchone()      → Pobiera JEDEN wiersz
                 → Zwraca KROTKĘ (lub None)
                 → Zwraca (wartość1, wartość2, ...)
                 
.fetchall()      → Pobiera WSZYSTKIE wiersze
                 → Zwraca LISTĘ KROTEK
                 → Zwraca [(val1, val2), (val3, val4), ...]
                 
.fetchmany(n)    → Pobiera N wierszy
                 → Zwraca LISTĘ KROTEK
                 → Zwraca [(val1, val2), (val3, val4), ...]
""")

# Praktyka
print("\nPraktyka:")
print("-"*70)

one = cursor.execute("SELECT COUNT(*) FROM stations").fetchone()
print(f"fetchone():       {one}")
print(f"Typ:              {type(one)}")
print(f"Struktura:        Pojedyncza KROTKA\n")

all_data = cursor.execute("SELECT COUNT(*) FROM stations").fetchall()
print(f"fetchall():       {all_data}")
print(f"Typ:              {type(all_data)}")
print(f"Struktura:        LISTA krotek\n")

many = cursor.execute("SELECT station FROM measurements").fetchmany(3)
print(f"fetchmany(3):     {many}")
print(f"Typ:              {type(many)}")
print(f"Struktura:        LISTA krotek (do 3 wierszy)")

# ============================================================================
# 6. KIEDY UŻYWAĆ .fetchone()[0]
# ============================================================================

print("\n\n6️⃣ KIEDY UŻYWAĆ .fetchone()[0]")
print("-"*70)

print("""
✅ UŻYWAJ .fetchone()[0] KIEDY:

1. Chcesz JEDNĄ wartość
   count = cursor.execute("SELECT COUNT(*)...").fetchone()[0]
   
2. Chcesz LICZBĘ (COUNT, MAX, MIN, AVG)
   max_val = cursor.execute("SELECT MAX(...)...").fetchone()[0]
   
3. Chcesz JEDEN element z wyniku
   name = cursor.execute("SELECT name FROM stations LIMIT 1").fetchone()[0]

❌ NIE UŻYWAJ .fetchone()[0] KIEDY:

1. Chcesz WSZYSTKIE wiersze
   → Użyj fetchall()
   
2. Chcesz WIELE kolumn z jednego wiersza
   → Używaj fetchone() bez [0]
   → Lub rozpakuj: name, country = fetchone()
   
3. Chcesz wiedzieć czy wynik istnieje
   → Najpierw sprawdź: if result is not None
""")

# ============================================================================
# 7. BŁĘDY - KIEDY COŚ PÓJDZIE NIE TAK
# ============================================================================

print("\n\n7️⃣ BŁĘDY - KIEDY COŚ PÓJDZIE NIE TAK")
print("-"*70)

print("\nBŁĘD 1: TypeError: 'NoneType' object is not subscriptable")
print("-"*70)

print("""
Przyczyna: fetchone() zwróciło None (brak danych)

❌ Złe:
result = cursor.execute("SELECT * FROM stations WHERE station = 'BRAK'").fetchone()[0]
# Błąd! fetchone() zwróciło None, a None[0] nie działa

✅ Dobrze:
result = cursor.execute("SELECT * FROM stations WHERE station = 'BRAK'").fetchone()
if result is not None:
    value = result[0]
else:
    print("Nie znaleziono")
""")

print("\nBŁĘD 2: IndexError: tuple index out of range")
print("-"*70)

print("""
Przyczyna: Indeks [0] nie istnieje w krotce

❌ Złe:
result = cursor.execute("SELECT * FROM measurements").fetchone()
print(result[10])  # Tylko 4 kolumny, a Ty chcesz [10]
# Błąd! Indeks za wysoki

✅ Dobrze:
result = cursor.execute("SELECT * FROM measurements").fetchone()
print(f"Liczba kolumn: {len(result)}")  # Sprawdź ile ich jest
""")

# ============================================================================
# 8. PRAKTYCZNE WZORY
# ============================================================================

print("\n\n8️⃣ PRAKTYCZNE WZORY - KOPUJ-WKLEJ")
print("-"*70)

print("\nWZÓR 1: Liczenie rekordów")
print("-"*70)
print("""
count = conn.execute("SELECT COUNT(*) FROM stations").fetchone()[0]
print(f"Liczba stacji: {count}")
""")

print("\nWZÓR 2: Pobieranie maksymalnej wartości")
print("-"*70)
print("""
max_val = conn.execute("SELECT MAX(elevation) FROM stations").fetchone()[0]
print(f"Maksymalna wysokość: {max_val}")
""")

print("\nWZÓR 3: Pobieranie jednej wartości z warunku")
print("-"*70)
print("""
name = conn.execute(
    "SELECT name FROM stations WHERE station = 'USW00094728'"
).fetchone()[0]
print(f"Nazwa: {name}")
""")

print("\nWZÓR 4: Bezpieczne pobieranie (sprawdzenie czy istnieje)")
print("-"*70)
print("""
result = conn.execute("SELECT name FROM stations LIMIT 1").fetchone()
if result:
    name = result[0]
    print(f"Nazwa: {name}")
else:
    print("Brak wyników")
""")

print("\nWZÓR 5: Wiele kolumn z jednego wiersza")
print("-"*70)
print("""
result = conn.execute(
    "SELECT name, country FROM stations LIMIT 1"
).fetchone()

if result:
    name = result[0]
    country = result[1]
    print(f"Stacja: {name} ({country})")
    
# Lub rozpakowanie:
name, country = result
print(f"Stacja: {name} ({country})")
""")

# ============================================================================
# 9. PODSUMOWANIE
# ============================================================================

print("\n\n9️⃣ PODSUMOWANIE")
print("="*70)

print("""
.fetchone()[0]

CO TO:
  → Pobiera JEDEN wiersz z wyniku zapytania
  → Bierze PIERWSZY element (indeks 0)
  
JAK DZIAŁA:
  .fetchone()  → Zwraca krotkę: (val1, val2, ...)
  [0]          → Wybiera pierwszy element: val1
  
KIEDY UŻYWAĆ:
  ✅ Liczenie (COUNT)
  ✅ Maksimum/Minimum (MAX, MIN)
  ✅ Jedną wartość z warunku

ALTERNATYWY:
  fetchall()   → Wszystkie wiersze (zwraca listę)
  fetchone()   → Jeden wiersz bez [0] (zwraca krotkę)
  
BŁĘDY DO UNIKANIA:
  ❌ fetchone()[0] na brak danych (None)
  ❌ Indeks za wysoki
  ❌ Zapomnienie że zwraca PIERWSZY element
""")

conn.close()

print("\n" + "="*70)
print("✓ Wyjaśnienie .fetchone()[0] zakończone!")
print("="*70)
