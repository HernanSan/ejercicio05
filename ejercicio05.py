import pandas as pd
import requests

# Leer el archivo CSV que contiene las frases
df = pd.read_csv('frases.csv', header=None)  # No se especifica un encabezado

# Iterar sobre las frases en el DataFrame
for index, row in df.iterrows():
    frase = row[0]  
    url = f"http://127.0.0.1:5000/prediccion/{frase}"  # Se construye la URL con la frase
    response = requests.get(url)
    
    prediction = response.json()['prediction']
    
    print(f"Frase: {frase} - Predicción: {prediction}")