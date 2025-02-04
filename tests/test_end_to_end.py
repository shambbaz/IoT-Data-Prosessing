import sys
import os

# Lisää projektin juurihakemisto Pythonin hakupolulle
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import os
from data_storage import save_sensor_data, fetch_all_data
from data_generator import generate_sensor_data
from ml_model import analyze_data
from data_visualizer import visualize_data

def test_end_to_end():
    # Tyhjennä tietokanta testin alussa
    clear_database()

    # Vaihe 1: Generoi dataa
    data = [generate_sensor_data() for _ in range(10)]
    assert len(data) == 10  # Varmista, että dataa luotiin

    # Vaihe 2: Tallenna data tietokantaan
    for record in data:
        save_sensor_data(record["temperature"], record["humidity"], record["pressure"])

    # Vaihe 3: Hae ja analysoi data ML-mallilla
    stored_data = fetch_all_data()
    assert len(stored_data) == 10  # Varmista, että kaikki data tallennettiin

    analysis_result = analyze_data(stored_data)
    assert analysis_result is not None  # Varmista, että analyysi onnistui

    # Vaihe 4: Visualisoi data
    visualization = visualize_data(output_file="test_visualization.png")
    assert visualization is True
