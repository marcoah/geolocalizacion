# 🗺️ Ejemplo de Resolución de Geolocalización en Python

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![License](https://img.shields.io/badge/License-MIT-green)

Este proyecto es un **notebook interactivo** que demuestra cómo realizar **geolocalización** usando Python.  
Está pensado como ejemplo educativo y punto de partida para integrarlo en proyectos reales.

---

## 🚀 Funcionalidades

- Conversión de **direcciones → coordenadas** (geocodificación)
- Visualización en **mapa interactivo** con [`folium`](https://python-visualization.github.io/folium/)
- Se usa NominaTIM como API para resolver la geolocalización
- Manejo de **límites** de uso en APIs de NominaTIM (1 consulta por seg)

---

## 🛠️ Tecnologías utilizadas

- **[Python](https://www.python.org/)** (>=3.9)
- **[geopy](https://geopy.readthedocs.io/)**
- **[pandas](https://pandas.pydata.org/)**
- **[folium](https://python-visualization.github.io/folium/)**
- **[NominaTIM](https://nominatim.org/)**

---

## 📦 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/marcoah/geolocalizacion.git
cd geolocalizacion

# Instalar dependencias
pip install -r geopy pandas folium
```
