import time
import random
from data_storage import save_sensor_data  # Lisää tämä

def generate_sensor_data():
    return {
        "temperature": round(random.uniform(-10, 35), 1),
        "humidity": round(random.uniform(20, 80), 1),
        "pressure": round(random.uniform(950, 1050), 1)
    }

# Simuloi dataa 10 sekunnin ajan ja tallentaa sen tietokantaan
if __name__ == "__main__":
    start_time = time.time()
    duration = 10  # sekuntia

    while time.time() - start_time < duration:
        data = generate_sensor_data()
        print(f"Tallennetaan data: {data}")  # Debuggausta varten
        save_sensor_data(data["temperature"], data["humidity"], data["pressure"])  # Tallennus tietokantaan
        time.sleep(1)  # Lisää pieni tauko simulaatioiden välillä

    print("Program ended after 10 seconds.")
