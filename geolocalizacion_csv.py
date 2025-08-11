import pandas as pd
import requests
import time
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()
# Tu clave de Azure Maps
AZURE_MAPS_KEY = os.getenv("AZURE_MAPS_KEY")

# Cargar el CSV de entrada
df = pd.read_csv("direcciones_entrada.csv")

# Función para hacer geocodificación con Azure Maps
def geocode_address(address):
    url = "https://atlas.microsoft.com/search/address/json"
    params = {
        "subscription-key": AZURE_MAPS_KEY,
        "api-version": "1.0",
        "query": address
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data.get("results"):
        position = data["results"][0]["position"]
        return position["lat"], position["lon"]
    return None, None

# Aplicar geocodificación fila por fila
latitudes = []
longitudes = []

for address in df["Direccion"]:
    lat, lon = geocode_address(address)
    latitudes.append(lat)
    longitudes.append(lon)
    time.sleep(0.5)  # Evitar límite de peticiones por segundo

# Añadir coordenadas al DataFrame
df["Latitud"] = latitudes
df["Longitud"] = longitudes

# Guardar el resultado
df.to_csv("direcciones_geocodificadas.csv", index=False)

print("Archivo guardado con coordenadas.")
