"""
MENU INTERAKTYWNE - WYBIERZ I URUCHOM PRZYKŁADY
Wygodny sposób na uruchamianie przykładów bez pisania poleceń
"""

import subprocess
import sys
import os

# Mapa przykładów
EXAMPLES = {
    "1": {
        "nazwa": "Podstawowe zapytania SELECT",
        "plik": "example_1_basic_select.py",
        "opis": "SELECT *, LIMIT, COUNT, DISTINCT",
        "emoji": "📊"
    },
    "2": {
        "nazwa": "Filtrowanie danych WHERE",
        "plik": "example_2_where_filter.py",
        "opis": "WHERE, warunkowe pobieranie, porównania",
        "emoji": "🔍"
    },
    "3": {
        "nazwa": "Sortowanie danych ORDER BY",
        "plik": "example_3_order_by.py",
        "opis": "ORDER BY ASC/DESC, sortowanie alfabetyczne, chronologiczne",
        "emoji": "📈"
    },
    "4": {
        "nazwa": "Agregacja danych",
        "plik": "example_4_aggregation.py",
        "opis": "COUNT, MAX, MIN, GROUP BY, statystyka",
        "emoji": "🔢"
    },
    "5": {
        "nazwa": "Zaawansowane: JOIN, GROUP BY, HAVING",
        "plik": "example_5_advanced_join_groupby.py",
        "opis": "JOIN, GROUP BY, HAVING, parametryzowane zapytania",
        "emoji": "🚀"
    }
}

def clear_screen():
    """Wyczyść ekran (działa na Windows i Mac/Linux)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header():
    """Wyświetl nagłówek"""
    print("\n" + "="*70)
    print("🎯 MENU INTERAKTYWNE - PRZYKŁADY SQL")
    print("="*70)
    print()

def show_menu():
    """Wyświetl menu z wszystkimi przykładami"""
    show_header()
    
    print("Wybierz przykład do uruchomienia:\n")
    
    for key, data in EXAMPLES.items():
        print(f"  {data['emoji']} [{key}] {data['nazwa']}")
        print(f"      → {data['opis']}\n")
    
    print("  [6] Uruchom WSZYSTKIE przykłady po kolei")
    print("  [0] Wyjście\n")

def run_example(key):
    """Uruchom wybrany przykład"""
    if key not in EXAMPLES:
        print("❌ Niepoprawny wybór!\n")
        return False
    
    example = EXAMPLES[key]
    
    # Sprawdzenie czy plik istnieje
    if not os.path.exists(example["plik"]):
        print(f"❌ Plik '{example['plik']}' nie znaleziony!")
        print(f"   Upewnij się że plik jest w tym samym folderze co menu.py\n")
        return False
    
    print(f"\n{'='*70}")
    print(f"▶️  URUCHAMIANIE: {example['nazwa']}")
    print(f"{'='*70}\n")
    
    try:
        # Uruchom plik Pythona
        subprocess.run([sys.executable, example["plik"]], check=True)
        print(f"\n{'='*70}")
        print(f"✅ Przykład '{example['nazwa']}' zakończony!")
        print(f"{'='*70}\n")
        return True
    except subprocess.CalledProcessError:
        print(f"\n❌ Błąd podczas uruchamiania przykładu!")
        return False
    except Exception as e:
        print(f"\n❌ Nieoczekiwany błąd: {e}")
        return False

def run_all_examples():
    """Uruchom wszystkie przykłady po kolei"""
    print(f"\n{'='*70}")
    print("▶️  URUCHAMIANIE WSZYSTKICH PRZYKŁADÓW PO KOLEI")
    print(f"{'='*70}\n")
    
    input("Naciśnij ENTER aby zacząć...\n")
    
    for key in sorted(EXAMPLES.keys()):
        run_example(key)
        
        # Pytaj czy kontynuować (oprócz ostatniego)
        if key != "5":
            response = input("\nNaciśnij ENTER aby przejść do następnego przykładu (lub 'q' aby przerwać): ")
            if response.lower() == 'q':
                print("\n⏹️  Przerwano uruchamianie.")
                break
    
    print(f"\n{'='*70}")
    print("✅ Wszystkie przykłady zakończone!")
    print(f"{'='*70}\n")

def show_help():
    """Pokaż pomoc"""
    print(f"\n{'='*70}")
    print("ℹ️  PORADA")
    print(f"{'='*70}")
    print("""
Każdy plik .py zawiera kilka zapytań SQL:
- Każde zapytanie ma wyjaśnienie
- Wyniki są wyświetlane na ekranie
- Możesz zmienić zapytania i eksperymentować!

Polecane porządek nauki:
1️⃣  Przykład 1 - poznaj SELECT
2️⃣  Przykład 2 - naucz się filtrować (WHERE)
3️⃣  Przykład 3 - naucz się sortować (ORDER BY)
4️⃣  Przykład 4 - naucz się agregować (COUNT, GROUP BY)
5️⃣  Przykład 5 - zaawansowane (JOIN, HAVING)

Możesz jednak uruchamiać w dowolnej kolejności!
""")
    print(f"{'='*70}\n")

def main():
    """Główna pętla menu"""
    while True:
        show_menu()
        
        choice = input("Twój wybór: ").strip()
        
        if choice == "0":
            print("\n👋 Do widzenia!\n")
            break
        elif choice == "6":
            run_all_examples()
            input("\nNaciśnij ENTER aby wrócić do menu...")
            clear_screen()
        elif choice == "?":
            show_help()
            input("\nNaciśnij ENTER aby wrócić do menu...")
            clear_screen()
        elif choice in EXAMPLES:
            run_example(choice)
            input("\nNaciśnij ENTER aby wrócić do menu...")
            clear_screen()
        else:
            print("❌ Niepoprawny wybór! Spróbuj ponownie.\n")
            input("Naciśnij ENTER aby kontynuować...")
            clear_screen()

def check_prerequisites():
    """Sprawdź czy baza danych istnieje"""
    if not os.path.exists('air_quality.db'):
        print("\n⚠️  UWAGA!")
        print("="*70)
        print("Baza danych 'air_quality.db' nie istnieje!")
        print("\nMusisz najpierw uruchomić:")
        print("  python create_database.py")
        print("\nAby utworzyć bazę danych.\n")
        print("="*70 + "\n")
        
        response = input("Czy chcesz to zrobić teraz? (t/n): ").strip().lower()
        
        if response == 't':
            print("\nUruchamianie create_database.pyper_fixed_v2.py...\n")
            try:
                subprocess.run([sys.executable, "create_database.py"], check=True)
                print("\n✅ Baza danych została utworzona!")
                input("\nNaciśnij ENTER aby kontynuować...")
                clear_screen()
            except subprocess.CalledProcessError:
                print("\n❌ Błąd podczas tworzenia bazy danych!")
                print("Spróbuj uruchomić ręcznie: python create_database.py")
                sys.exit(1)
            except FileNotFoundError:
                print("\n❌ Nie znaleziono pliku 'create_database.py'")
                sys.exit(1)
        else:
            print("\nUpewnij się że baza istnieje przed uruchomieniem przykładów!")
            sys.exit(1)

if __name__ == "__main__":
    # Sprawdź warunki wstępne
    check_prerequisites()
    
    # Uruchom menu
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Menu przerwane przez użytkownika.\n")
        sys.exit(0)
