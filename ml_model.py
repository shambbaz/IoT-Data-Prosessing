import numpy as np
from sklearn.linear_model import LinearRegression
from data_storage import fetch_all_data  # Lisää tämä

def analyze_data(data):
    """
    Analysoi dataa yksinkertaisella koneoppimismallilla (lineaarinen regressio).
    :param data: Lista, jossa on [temperature, humidity, pressure]
    :return: Mallin ennuste seuraavalle datapisteelle
    """
    if not data or len(data) < 2:  # Lisätty: tarkistus, ettei data ole tyhjä
        print("Not enough data for analysis.")
        return None

    # Oletetaan, että data sisältää lämpötilan ja paineen
    X = np.array([row[0] for row in data]).reshape(-1, 1)  # Lämpötila
    y = np.array([row[2] for row in data])  # Paine

    model = LinearRegression().fit(X, y)

    # Ennustetaan seuraavan datapisteen arvo (oletetaan lämpötila 25)
    next_prediction = model.predict(np.array([[25]]))
    return next_prediction[0]

if __name__ == "__main__":
    data = fetch_all_data()
    prediction = analyze_data(data)
    if prediction:
        print(f"Predicted pressure for temperature 25°C: {prediction}")
