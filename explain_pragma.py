"""
CO TO JEST PRAGMA W SQLITE?
Wyjaśnienie i praktyczne przykłady
"""

import sqlite3

# Połączenie z bazą
conn = sqlite3.connect('air_quality.db')
cursor = conn.cursor()

print("="*70)
print("CO TO JEST PRAGMA W SQLITE?")
print("="*70)

# ============================================================================
# 1. DEFINICJA
# ============================================================================

print("\n1️⃣ DEFINICJA")
print("-"*70)

print("""
PRAGMA to polecenie specjalne w SQLite, które:
  → Pobiera INFORMACJE o bazie danych
  → Zmienia USTAWIENIA bazy
  → Debuguje problemy
  → Sprawdza STRUKTURĘ tabel

PRAGMA to SKRÓT od: "PRAGmatic"
  → Oznacza: "praktyczne, pożyteczne polecenie"

Używasz go do POGLĄDANIA na dane META (dane o danych):
  → Jakie kolumny ma tabela?
  → Jakie są ich typy?
  → Jakie są ograniczenia?
""")

# ============================================================================
# 2. SKŁADNIA
# ============================================================================

print("\n2️⃣ SKŁADNIA")
print("-"*70)

print("""
PRAGMA polecenie
PRAGMA polecenie = wartość

Przykłady:
  PRAGMA table_info(nazwa_tabeli)     ← Informacje o kolumnach
  PRAGMA database_list                 ← Lista baz
  PRAGMA foreign_keys                  ← Sprawdź ustawienia
""")

# ============================================================================
# 3. NAJPOPULARNIEJSZE PRAGMA
# ============================================================================

print("\n3️⃣ NAJPOPULARNIEJSZE PRAGMA - table_info()")
print("-"*70)

print("""
PRAGMA table_info(nazwa_tabeli)

Co robi?
  → Pokazuje STRUKTURĘ tabeli
  → Zwraca informacje o każdej kolumnie
  → Pokazuje typ danych, ograniczenia itd.

Zwraca dla każdej kolumny:
  1. cid         - numer kolumny (0, 1, 2, ...)
  2. name        - nazwa kolumny
  3. type        - typ danych (TEXT, INTEGER, REAL itd.)
  4. notnull     - czy może być NULL (0=może, 1=nie może)
  5. dflt_value  - wartość domyślna
  6. pk          - czy jest PRIMARY KEY (0=nie, 1=tak)
""")

# PRAKTYCZNY PRZYKŁAD
print("\nPRZYKŁAD: Struktura tabeli 'stations'")
print("-"*70)

cursor.execute("PRAGMA table_info(stations)")
columns_info = cursor.fetchall()

print(f"{'Lp':<4} {'Nazwa':<20} {'Typ':<10} {'Not Null':<10} {'PK':<5}")
print("-"*70)

for cid, name, type_, notnull, dflt_value, pk in columns_info:
    notnull_str = "TAK" if notnull else "NIE"
    pk_str = "TAK" if pk else "NIE"
    print(f"{cid:<4} {name:<20} {type_:<10} {notnull_str:<10} {pk_str:<5}")

# ============================================================================
# 4. PRAKTYCZNE PRZYKŁADY - table_info()
# ============================================================================

print("\n\n4️⃣ PRAKTYCZNE UŻYCIE - table_info()")
print("-"*70)

# Przykład 1: Wydobyć nazwy kolumn
print("\nPRZYKŁAD 1: Wydobyć NAZWY WSZYSTKICH KOLUMN")
print("-"*70)

cursor.execute("PRAGMA table_info(stations)")
column_names = [row[1] for row in cursor.fetchall()]
print(f"Kolumny tabeli 'stations': {column_names}")

# Przykład 2: Wydobyć typy kolumn
print("\nPRZYKŁAD 2: Wydobyć TYPY KOLUMN")
print("-"*70)

cursor.execute("PRAGMA table_info(measurements)")
for cid, name, col_type, notnull, dflt, pk in cursor.fetchall():
    print(f"  {name}: {col_type}")

# Przykład 3: Znaleźć PRIMARY KEY
print("\nPRZYKŁAD 3: Znaleźć PRIMARY KEY")
print("-"*70)

cursor.execute("PRAGMA table_info(stations)")
for cid, name, col_type, notnull, dflt, pk in cursor.fetchall():
    if pk:
        print(f"  PRIMARY KEY: {name} (typ: {col_type})")

# ============================================================================
# 5. INNE POPULARNE PRAGMA
# ============================================================================

print("\n\n5️⃣ INNE POPULARNE PRAGMA")
print("-"*70)

# database_list
print("\nPRAGMA database_list - LISTA BAZ DANYCH")
print("-"*70)

cursor.execute("PRAGMA database_list")
databases = cursor.fetchall()

print(f"{'Seq':<5} {'Nazwa':<20} {'Ścieżka':<30}")
print("-"*70)
for seq, name, file in databases:
    print(f"{seq:<5} {name:<20} {file:<30}")

# ============================================================================
# 6. PORÓWNANIE: Czytanie schematu VS PRAGMA
# ============================================================================

print("\n\n6️⃣ DWA SPOSOBY NA ODCZYT STRUKTURY TABELI")
print("-"*70)

print("\nSPOSOB 1: PRAGMA table_info() - PROSTY i WYGODNY")
print("-"*70)

cursor.execute("PRAGMA table_info(stations)")
result = cursor.fetchall()
print(f"Wynik: {result}")
print(f"Typ: {type(result)}")

print("\nSPOSOB 2: sqlite_master - ZAAWANSOWANY")
print("-"*70)

cursor.execute("""
    SELECT name, type, sql FROM sqlite_master 
    WHERE type='table' AND name='stations'
""")
result = cursor.fetchone()
print(f"Nazwa tabeli: {result[0]}")
print(f"Typ: {result[1]}")
print(f"SQL: {result[2]}")

# ============================================================================
# 7. PRAGMA DO ZMIAN USTAWIEŃ
# ============================================================================

print("\n\n7️⃣ PRAGMA DO ZMIAN USTAWIEŃ")
print("-"*70)

print("""
PRAGMA foreign_keys = ON/OFF
  → Włącza/wyłącza sprawdzanie kluczy obcych

PRAGMA synchronous = FULL/NORMAL/OFF
  → Zmienia szybkość zapisywania

PRAGMA journal_mode = DELETE/WAL/OFF
  → Zmienia sposób rejestrowania zmian
""")

# Przykład
print("\nSTAN CURRENT foreign_keys:")
cursor.execute("PRAGMA foreign_keys")
result = cursor.fetchone()
print(f"  foreign_keys = {result[0]} (0=OFF, 1=ON)")

# ============================================================================
# 8. PRZYPADKI UŻYCIA - KIEDY UŻYWAĆ PRAGMA
# ============================================================================

print("\n\n8️⃣ KIEDY UŻYWAĆ PRAGMA?")
print("-"*70)

print("""
✅ UŻYWAJ PRAGMA KIEDY:

1. Chcesz poznać STRUKTURĘ TABELI
   → Jakie kolumny?
   → Jakie typy?
   → Czy jest PRIMARY KEY?
   
2. Debugujesz PROBLEMY
   → Co jest nie tak?
   → Jaka jest struktura?
   
3. Piszesz DYNAMICZNY KOD
   → Musisz poznać kolumny w runtime
   → Nie znasz z góry struktury tabeli
   
4. Analizujesz ISTNIEJĄCĄ BAZĘ
   → Dostałeś bazę od kogoś
   → Chcesz wiedzieć co w niej jest

❌ NIE UŻYWAJ PRAGMA KIEDY:

1. Zwykłe pobieranie DANYCH
   → Użyj SELECT

2. Zmiana DANYCH
   → Użyj INSERT/UPDATE/DELETE

3. Tworzenie TABEL
   → Użyj CREATE TABLE (ale PRAGMA table_info sprawdza wynik)
""")

# ============================================================================
# 9. PRAKTYCZNY SKRYPT - ANALIZA BAZY
# ============================================================================

print("\n\n9️⃣ PRAKTYCZNY SKRYPT - ANALIZA CAŁEJ BAZY")
print("-"*70)

# Pobierz wszystkie tabele
cursor.execute("""
    SELECT name FROM sqlite_master 
    WHERE type='table' 
    ORDER BY name
""")
tables = [row[0] for row in cursor.fetchall()]

print(f"Liczba tabel: {len(tables)}\n")

for table_name in tables:
    print(f"📋 Tabela: {table_name}")
    print("-"*70)
    
    # Pobierz informacje o kolumnach
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    
    for cid, name, col_type, notnull, dflt, pk in columns:
        pk_mark = "🔑" if pk else "  "
        notnull_mark = "*" if notnull else " "
        print(f"  {pk_mark} {name:<20} {col_type:<10} {notnull_mark}")
    
    # Liczba wierszy
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    print(f"  Liczba wierszy: {count}\n")

# ============================================================================
# 10. PODSUMOWANIE
# ============================================================================

print("\n\n🔟 PODSUMOWANIE")
print("="*70)

print("""
CO TO JEST PRAGMA?
  → Specjalne polecenie SQLite
  → Pobiera/zmienia METADANE bazy
  → PRAGMA = PRAGmatic

NAJCZĘŚCIEJ UŻYWANE:
  → PRAGMA table_info(tabela) - struktura tabeli
  → PRAGMA database_list - lista baz

ZWRACA:
  → Informacje o kolumnach
  → Typy danych
  → Ograniczenia (PRIMARY KEY, NOT NULL)
  → Ustawienia bazy

KIEDY UŻYWAĆ:
  ✅ Analiza struktury bazy
  ✅ Debugging
  ✅ Dynamiczny kod
  ✅ Poznawanie istniejącej bazy
""")

conn.close()

print("\n" + "="*70)
print("✓ Wyjaśnienie PRAGMA zakończone!")
print("="*70)
