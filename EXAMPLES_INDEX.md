# 📚 INDEKS PRZYKŁADÓW - WSZYSTKIE PLIKI .PY

## 🎯 Struktura

Stworzono 5 plików .py z przykładami użycia bazy danych. Każdy plik można uruchomić niezależnie.

---

## 📋 Lista wszystkich plików

### 1️⃣ **example_1_basic_select.py**
**Temat:** Podstawowe zapytania SELECT

**Co zawiera:**
- SELECT * FROM stations LIMIT 5
- SELECT * FROM measurements LIMIT 5
- SELECT z wybranymi kolumnami
- COUNT(*) - liczenie wierszy
- DISTINCT - unikalne wartości

**Uruchomienie:**
```bash
python example_1_basic_select.py
```

---

### 2️⃣ **example_2_where_filter.py**
**Temat:** Filtrowanie danych WHERE

**Co zawiera:**
- WHERE - podstawowy warunek
- Pomiary dla konkretnej stacji
- Informacje o konkretnej stacji
- Stacje z konkretnego kraju
- Pomiary z konkretnego dnia
- WHERE z operatorem > (opardy > 5mm)

**Uruchomienie:**
```bash
python example_2_where_filter.py
```

---

### 3️⃣ **example_3_order_by.py**
**Temat:** Sortowanie danych ORDER BY

**Co zawiera:**
- ORDER BY ASC - sortowanie rosnące
- ORDER BY DESC - sortowanie malejące
- Sortowanie alfabetyczne
- Sortowanie numeryczne (wysokość)
- Sortowanie chronologiczne (daty)

**Uruchomienie:**
```bash
python example_3_order_by.py
```

---

### 4️⃣ **example_4_aggregation.py**
**Temat:** Agregacja danych (COUNT, MAX, MIN, GROUP BY)

**Co zawiera:**
- COUNT(*) - liczenie rekordów
- COUNT(...) WHERE - warunkowe liczenie
- MAX / MIN - maksimum i minimum
- GROUP BY - grupowanie wyników
- Statystyka dla konkretnej stacji

**Uruchomienie:**
```bash
python example_4_aggregation.py
```

---

### 5️⃣ **example_5_advanced_join_groupby.py**
**Temat:** Zaawansowane zapytania (JOIN, GROUP BY, HAVING)

**Co zawiera:**
- JOIN - łączenie dwóch tabel
- GROUP BY - grupowanie wyników
- WHERE + JOIN - warunki z łączeniami
- Statystyka na stację
- HAVING - filtrowanie wyników GROUP BY
- Parametryzowane zapytania

**Uruchomienie:**
```bash
python example_5_advanced_join_groupby.py
```

---

## 🚀 JAK URUCHOMIĆ

### Opcja 1: Uruchom jeden plik
```bash
python example_1_basic_select.py
```

### Opcja 2: Uruchom wszystkie po kolei
```bash
python example_1_basic_select.py
python example_2_where_filter.py
python example_3_order_by.py
python example_4_aggregation.py
python example_5_advanced_join_groupby.py
```

### Opcja 3: Skrypt do uruchomienia wszystkich (Windows)
Stwórz plik `run_all_examples.bat`:
```batch
@echo off
echo Uruchamianie wszystkich przykładów...
python example_1_basic_select.py
pause
python example_2_where_filter.py
pause
python example_3_order_by.py
pause
python example_4_aggregation.py
pause
python example_5_advanced_join_groupby.py
pause
echo Wszystkie przykłady zakończone!
```

Potem uruchom:
```bash
run_all_examples.bat
```

### Opcja 4: Skrypt do uruchomienia wszystkich (Mac/Linux)
Stwórz plik `run_all_examples.sh`:
```bash
#!/bin/bash
echo "Uruchamianie wszystkich przykładów..."
python example_1_basic_select.py
python example_2_where_filter.py
python example_3_order_by.py
python example_4_aggregation.py
python example_5_advanced_join_groupby.py
echo "Wszystkie przykłady zakończone!"
```

Potem:
```bash
chmod +x run_all_examples.sh
./run_all_examples.sh
```

---

## 📊 PODSUMOWANIE FUNKCJI SQL

| Funkcja | Plik | Opis |
|---------|------|------|
| SELECT * | example_1 | Wybierz wszystkie kolumny |
| SELECT kolumny | example_1 | Wybierz określone kolumny |
| WHERE | example_2 | Filtrowanie wierszy |
| ORDER BY | example_3 | Sortowanie wyników |
| LIMIT | example_1 | Ograniczenie liczby wyników |
| COUNT | example_4 | Liczenie wierszy |
| MAX/MIN | example_4 | Maksimum/Minimum |
| GROUP BY | example_4 | Grupowanie wyników |
| JOIN | example_5 | Łączenie tabel |
| HAVING | example_5 | Filtrowanie wyników GROUP BY |

---

## 💡 NAUKA PROGRESYWNA

**Jeśli dopiero zaczynasz:**
1. Zacznij od `example_1_basic_select.py`
2. Potem przejdź do `example_2_where_filter.py`
3. Następnie `example_3_order_by.py`
4. Potem `example_4_aggregation.py`
5. Na koniec `example_5_advanced_join_groupby.py`

**Jeśli już masz doświadczenie:**
- Możesz uruchomić dowolny plik w dowolnej kolejności
- Każdy plik jest niezależny

---

## 📁 STRUKTURA FOLDERÓW

```
mój_projekt/
├── solution_proper_fixed_v2.py     ← Główny skrypt (tworzy bazę)
├── example_1_basic_select.py       ← Przykład 1
├── example_2_where_filter.py       ← Przykład 2
├── example_3_order_by.py           ← Przykład 3
├── example_4_aggregation.py        ← Przykład 4
├── example_5_advanced_join_groupby.py ← Przykład 5
├── clean_stations.csv              ← Dane
├── clean_measure.csv               ← Dane
└── air_quality.db                  ← Baza (zostanie utworzona)
```

---

## ✅ KROKI DO STARTU

1. **Utwórz bazę:**
   ```bash
   python solution_proper_fixed_v2.py
   ```

2. **Uruchom przykład 1:**
   ```bash
   python example_1_basic_select.py
   ```

3. **Uruchom pozostałe przykłady** w dowolnej kolejności

---

## 🎓 CO NAUCZYSZ SIĘ

Z tych przykładów nauczysz się:
- ✅ Łączenia z bazą danych SQLite
- ✅ Pisania zapytań SQL
- ✅ Filtrowania i sortowania danych
- ✅ Liczenia i agregacji
- ✅ Łączenia tabel (JOIN)
- ✅ Grupowania wyników

---

**Happy learning! 🚀**
