# PRAGMA.py Sprawdzenie struktury tabeli 'stations' w bazie danych
""" Sprawdzenie struktury tabeli 'stations' w bazie danych za pomocą PRAGMA table_info """
import sqlite3
# Połączenie z bazą danych
conn = sqlite3.connect('air_quality.db')
cursor = conn.cursor() # Utworzenie kursora

# Sprawdzenie informacji o kolumnach tabeli 'stations'
cursor.execute("PRAGMA table_info(stations)") # Pobranie informacji o kolumnach tabeli 'stations'
columns = cursor.fetchall() # Pobranie wszystkich wyników do zmiennej columns

print(f"{'Kolumna':<15} {'Typ danych':<10}") # Nagłówki tabeli z wyrównaniem
print("-" * 25) # Linia oddzielająca

for col in columns:
    name = col[1]   # nazwa kolumny
    dtype = col[2]  # typ danych
    print(f"{name:<15} {dtype:<10}") # Wyświetlenie nazwy kolumny i typu danych z wyrównaniem

# Zamknięcie połączenia z bazą danych
conn.close()
