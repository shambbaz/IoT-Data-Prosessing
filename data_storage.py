import sqlite3

DATABASE = "sensor_data.db"

# Funktio datan tallentamiseen SQLite-tietokantaan
def save_sensor_data(temperature, humidity, pressure):
    """
    Tallentaa sensoridatan SQLite-tietokantaan.
    :param temperature: Lämpötila (float)
    :param humidity: Kosteus (float)
    :param pressure: Paine (float)
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Luo taulu, jos sitä ei vielä ole
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL,
            humidity REAL,
            pressure REAL
        )
    """)

    # Lisää uusi rivi tauluun
    cursor.execute("INSERT INTO sensor_data (temperature, humidity, pressure) VALUES (?, ?, ?)",
                   (temperature, humidity, pressure))
    conn.commit()
    conn.close()

# Funktio kaikkien datarivien hakemiseen tietokannasta
def fetch_all_data():
    """
    Hakee kaikki tiedot sensor_data-taulusta.
    :return: Lista tallennetuista riveistä [(temperature, humidity, pressure), ...]
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Hae kaikki tiedot taulusta
    cursor.execute("SELECT temperature, humidity, pressure FROM sensor_data")
    data = cursor.fetchall()
    conn.close()
    return data

if __name__ == "__main__":
    # POISTETTU clear_database(), jotta data ei tyhjene

    # Lisää testidataa
    save_sensor_data(25.3, 60.2, 1010.5)
    save_sensor_data(22.1, 55.0, 1009.2)

    # Hae ja tulosta tallennettu data
    data = fetch_all_data()
    print("Tallennettu data:", data)
