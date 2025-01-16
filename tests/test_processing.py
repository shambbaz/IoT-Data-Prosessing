import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from data_generator import generate_sensor_data

def test_generate_sensor_data():
    """
    Testaa, että generate_sensor_data palauttaa oikeat avaimet ja arvot.
    """
    data = generate_sensor_data()
    assert "temperature" in data
    assert "humidity" in data
    assert "pressure" in data
    assert -10 <= data["temperature"] <= 35
    assert 20 <= data["humidity"] <= 80
    assert 950 <= data["pressure"] <= 1050

# Valinnainen ML/AI-testi (esimerkkimalli)
def test_ml_model_prediction():
    """
    Testaa yksinkertainen ML-malli datan käsittelyyn.
    """
    from sklearn.linear_model import LinearRegression
    import numpy as np

    # Esimerkkidata: lämpötila ja paine (yksinkertainen lineaarinen suhde)
    X = np.array([[10], [15], [20], [25], [30]])
    y = np.array([1010, 1012, 1015, 1018, 1020])  # Paine (hPa)

    # Mallin koulutus
    model = LinearRegression().fit(X, y)

    # Ennusta uusi arvo
    predicted = model.predict(np.array([[22]]))
    assert 1015 <= predicted[0] <= 1018  # Tarkista odotettu vaihteluväli
