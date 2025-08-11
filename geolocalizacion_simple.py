import requests
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()
# Tu clave de Azure Maps
API_KEY = os.getenv("AZURE_MAPS_KEY")

direccion = "Av Corrientes 1234, Buenos Aires"
url = f"https://atlas.microsoft.com/search/address/json?api-version=1.0&subscription-key={API_KEY}&query={direccion}"

response = requests.get(url)
data = response.json()

if data["results"]:
    position = data["results"][0]["position"]
    lat, lon = position["lat"], position["lon"]
    print(f"Latitud: {lat}, Longitud: {lon}")
else:
    print("No se encontraron resultados.")
