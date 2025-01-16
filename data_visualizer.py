import sqlite3
import matplotlib.pyplot as plt

DATABASE = "sensor_data.db"

def fetch_sensor_data():
    """
    Hakee kaiken datan tietokannasta.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT temperature, humidity, pressure FROM sensor_data")
    data = cursor.fetchall()
    conn.close()
    return data

def visualize_data(output_file="visualization.png"):
    """
    Visualisoi tallennetun datan graafeina ja tallentaa kuvan tiedostoon.
    :param output_file: Polku tiedostoon, johon visualisointi tallennetaan
    """
    data = fetch_sensor_data()

    if not data:
        print("No data to visualize.")
        return False

    # Erotellaan lämpötila, kosteus ja paine datasta
    temperatures = [row[0] for row in data]
    humidities = [row[1] for row in data]
    pressures = [row[2] for row in data]
    timestamps = range(1, len(data) + 1)  # Simuloidut aikaleimat (1, 2, 3...)

    # Luodaan kuvaajat
    plt.figure(figsize=(12, 6))

    # Lämpötilan kuvaaja
    plt.subplot(3, 1, 1)
    plt.plot(timestamps, temperatures, label="Temperature (°C)", color="red")
    plt.legend()

    # Kosteuden kuvaaja
    plt.subplot(3, 1, 2)
    plt.plot(timestamps, humidities, label="Humidity (%)", color="blue")
    plt.legend()

    # Paineen kuvaaja
    plt.subplot(3, 1, 3)
    plt.plot(timestamps, pressures, label="Pressure (hPa)", color="green")
    plt.legend()

    plt.tight_layout()

    # Tallenna kuva tiedostoon
    plt.savefig(output_file)
    plt.close()
    return True

if __name__ == "__main__":
    # Hakee datan tietokannasta ja visualisoi sen
    if visualize_data():
        print(f"Visualization saved to 'visualization.png'")
    else:
        print("Visualization failed.")
