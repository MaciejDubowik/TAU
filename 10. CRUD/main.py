import sqlite3

def main():
    conn = sqlite3.connect('projekt.db')
    c = conn.cursor()

    c.execute('DROP TABLE IF EXISTS pracownicy')

    c.execute('''
        CREATE TABLE pracownicy (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            imie TEXT,
            nazwisko TEXT,
            stanowisko TEXT
        )
    ''')

    # CREATE
    c.execute("INSERT INTO pracownicy (imie, nazwisko, stanowisko) VALUES (?, ?, ?)",
              ('Jan', 'Kowalski', 'Inżynier'))
    conn.commit()
    
    c.execute("SELECT * FROM pracownicy WHERE imie = ?", ('Jan',))
    rows = c.fetchall()
    assert len(rows) == 1, "Test CREATE nie powiódł się"

    # READ
    c.execute("SELECT * FROM pracownicy")
    rows = c.fetchall()
    assert len(rows) == 1, "Test READ nie powiódł się"

    # UPDATE
    c.execute("UPDATE pracownicy SET stanowisko = ? WHERE imie = ?",
              ('Senior Inżynier', 'Jan'))
    conn.commit()

    c.execute("SELECT * FROM pracownicy WHERE imie = ?", ('Jan',))
    rows = c.fetchall()
    assert rows[0][3] == 'Senior Inżynier', "Test UPDATE nie powiódł się"

    # DELETE
    c.execute("DELETE FROM pracownicy WHERE imie = ?", ('Jan',))
    conn.commit()

    c.execute("SELECT * FROM pracownicy WHERE imie = ?", ('Jan',))
    rows = c.fetchall()
    assert len(rows) == 0, "Test DELETE nie powiódł się"

    conn.close()


if __name__ == "__main__":
    main()
