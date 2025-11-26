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

print("\nPOŁĄCZ DANE STACJI Z POMIARAMI")
print("-"*70)

# s - alias dla tabeli stations
# m - alias dla tabeli measurements
# JOIN złącz measurements nazwij ją m, 
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

print("\nLICZBA POMIARÓW NA KAŻDĄ STACJĘ (GROUP BY)")
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

print("\nPOMIARY TYLKO Z OPADAMI DLA KAŻDEJ STACJI")
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

print("\nSTATYSTYKA POMIARÓW NA STACJĘ")
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

print("\nPOMIARY DLA KONKRETNEJ STACJI - SFORMATOWANE")
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

print("\nSTACJE Z WIĘCEJ NIŻ 1000 POMIARÓW")
print("-"*70)

result = conn.execute("""
    SELECT 
        s.name,
        COUNT(m.station) as liczba_pomiarow
    FROM stations s
    JOIN measurements m ON s.station = m.station
    GROUP BY s.station
    HAVING COUNT(m.station) > 1000
    ORDER BY liczba_pomiarow DESC
""").fetchall()

print(f"Liczba stacji: {len(result)}\n")

for name, count in result:
    print(f"Stacja: {name}, Pomiarów: {count}")

# Zamknięcie połączenia
conn.close()

print("\n" + "="*70)
print("Przykład 5 zakończony!")
print("="*70)

# ============================================================================
# Zapytanie 6a - Podzapytania w SELECT
# ============================================================================
print("\nPODZAPYTANIA W SELECT")
print("-"*70)
conn = sqlite3.connect('air_quality.db')
result = conn.execute("""
    SELECT 
        s.station,
        s.name,
        (SELECT COUNT(*) FROM measurements m WHERE m.station = s.station) as total_measurements,
        (SELECT AVG(tobs) FROM measurements m2 WHERE m2.station = s.station AND m2.tobs != '') as avg_temp
    FROM stations s
    LIMIT 10
""").fetchall()
for station_id, name, total_measurements, avg_temp in result:
    print(f"Stacja: {name} ({station_id})")
    print(f"  Razem pomiarów: {total_measurements}")
    print(f"  Średnia temperatura: {avg_temp:.2f}°C" if avg_temp is not None else "  Brak danych o temperaturze")
# Zamknięcie połączenia
conn.close()
print("\n" + "="*70)
print("Przykład 5a zakończony!")
print("="*70)
# ============================================================================
# Zapytanie 6b - Zapytnie z przedziałem 
# ============================================================================
print("\nPOMIARY W PRZEDZIALE 1000-2000 MM OPADÓW")
print("-"*70)
conn = sqlite3.connect('air_quality.db')
result = conn.execute("""
    SELECT 
        s.name,
        COUNT(m.station) as liczba_pomiarow
    FROM stations s
    JOIN measurements m ON s.station = m.station
    GROUP BY s.station
    HAVING SUM(m.precip) BETWEEN 1000 AND 2000
    ORDER BY liczba_pomiarow ASC
    """).fetchall()
print(f"Liczba stacji: {len(result)}\n")
for name, count in result:
    print(f"Stacja: {name}, Pomiarów: {count}")
    for measurement in conn.execute("""
        SELECT 
            m.date,
            m.precip,
            s.name
        FROM stations s
        JOIN measurements m ON s.station = m.station
        WHERE s.name = ?
        ORDER BY m.precip ASC
        limit 20
        """, (name,)).fetchall():
        date, precip, station_name = measurement
        print(f"    Stacja: {station_name} Data: {date}, Opady: {precip}mm")
        
        # do poprawki


# wyświetlenie pomiarów w przedziale 1000-2000 mm opadów

    


# Zamknięcie połączenia
conn.close()
print("\n" + "="*70)
print("Przykład zakończony!")
print("="*70)
