"""
PRZYKŁAD 5: Zaawansowane - JOIN, GROUP BY
Łączenie tabel i grupowanie wyników
"""

import sqlite3

# Połączenie z bazą
conn = sqlite3.connect('air_quality.db')

print("="*70)
print("PRZYKŁAD 5: ZAAWANSOWANE ZAPYTANIA (JOIN, GROUP BY)")
print("="*70)

# ============================================================================
# ZAPYTANIE 1: JOIN - Łączenie stacji z pomiarami
# ============================================================================

print("\n1️⃣ POŁĄCZ DANE STACJI Z POMIARAMI")
print("-"*70)

result = conn.execute("""
    SELECT 
        s.name,
        m.date,
        m.precip,
        m.tobs
    FROM stations s
    JOIN measurements m ON s.station = m.station
    LIMIT 10
""").fetchall()

print(f"Liczba wyników: {len(result)}\n")

for name, date, precip, tobs in result:
    print(f"Stacja: {name}, Data: {date}, Opady: {precip}mm, Temperatura: {tobs}°C")

# ============================================================================
# ZAPYTANIE 2: GROUP BY - Liczba pomiarów na stację
# ============================================================================

print("\n2️⃣ LICZBA POMIARÓW NA KAŻDĄ STACJĘ (GROUP BY)")
print("-"*70)

result = conn.execute("""
    SELECT 
        s.name,
        COUNT(m.station) as liczba_pomiarow
    FROM stations s
    JOIN measurements m ON s.station = m.station
    GROUP BY s.station
    ORDER BY liczba_pomiarow DESC
""").fetchall()

print(f"Liczba stacji: {len(result)}\n")

for name, count in result:
    print(f"Stacja: {name}, Pomiarów: {count}")

# ============================================================================
# ZAPYTANIE 3: WHERE + JOIN
# ============================================================================

print("\n3️⃣ POMIARY TYLKO Z OPADAMI DLA KAŻDEJ STACJI")
print("-"*70)

result = conn.execute("""
    SELECT 
        s.name,
        COUNT(m.station) as pomiary_z_opadami
    FROM stations s
    JOIN measurements m ON s.station = m.station
    WHERE m.precip > '0'
    GROUP BY s.station
    ORDER BY pomiary_z_opadami DESC
""").fetchall()

print(f"Liczba stacji: {len(result)}\n")

for name, count in result:
    print(f"Stacja: {name}, Pomiary z opadami: {count}")

# ============================================================================
# ZAPYTANIE 4: Statystyka pomiarów dla każdej stacji
# ============================================================================

print("\n4️⃣ STATYSTYKA POMIARÓW NA STACJĘ")
print("-"*70)

result = conn.execute("""
    SELECT 
        s.station,
        s.name,
        COUNT(m.station) as razem_pomiarow,
        (SELECT COUNT(*) FROM measurements m2 
         WHERE m2.station = s.station AND m2.precip > '0') as pomiary_z_opadami,
        (SELECT COUNT(*) FROM measurements m3 
         WHERE m3.station = s.station AND m3.precip = '0') as pomiary_bez_opadow
    FROM stations s
    LEFT JOIN measurements m ON s.station = m.station
    GROUP BY s.station
""").fetchall()

print(f"Liczba stacji: {len(result)}\n")

for station_id, name, total, with_precip, without_precip in result:
    print(f"\nStacja: {name} ({station_id})")
    print(f"  Razem pomiarów: {total}")
    print(f"  Z opadami: {with_precip if with_precip else 0}")
    print(f"  Bez opadów: {without_precip if without_precip else 0}")

# ============================================================================
# ZAPYTANIE 5: Pomiary z datą zamiast surowych danych
# ============================================================================

print("\n5️⃣ POMIARY DLA KONKRETNEJ STACJI - SFORMATOWANE")
print("-"*70)

station_id = "USW00094728"
result = conn.execute("""
    SELECT 
        s.name,
        s.country,
        m.date,
        m.precip,
        m.tobs
    FROM stations s
    JOIN measurements m ON s.station = m.station
    WHERE s.station = ?
    ORDER BY m.date ASC
    LIMIT 10
""", (station_id,)).fetchall()

if result:
    station_name = result[0][0]
    country = result[0][1]
    
    print(f"Stacja: {station_name} ({country})")
    print(f"Pierwsze 10 pomiarów:\n")
    
    for name, country, date, precip, tobs in result:
        print(f"  Data: {date} | Opady: {precip}mm | Temperatura: {tobs}°C")
else:
    print(f"Brak pomiarów dla stacji {station_id}")

# ============================================================================
# ZAPYTANIE 6: HAVING - filtrowanie wyników GROUP BY
# ============================================================================

print("\n6️⃣ STACJE Z WIĘCEJ NIŻ 100 POMIARÓW")
print("-"*70)

result = conn.execute("""
    SELECT 
        s.name,
        COUNT(m.station) as liczba_pomiarow
    FROM stations s
    JOIN measurements m ON s.station = m.station
    GROUP BY s.station
    HAVING COUNT(m.station) > 100
    ORDER BY liczba_pomiarow DESC
""").fetchall()

print(f"Liczba stacji: {len(result)}\n")

for name, count in result:
    print(f"Stacja: {name}, Pomiarów: {count}")

# Zamknięcie połączenia
conn.close()

print("\n" + "="*70)
print("✓ Przykład 5 zakończony!")
print("="*70)
