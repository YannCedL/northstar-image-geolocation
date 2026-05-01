# API FastAPI pour le moteur Northstar Image Geolocation
import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from genesis_core import ResultContract
from .geolocator import geolocate_image

app = FastAPI(
    title="Northstar Image Geolocation API",
    description="Moteur de Géolocalisation d'Images par Ombres & Calcul Solaire",
    version="1.0.0"
)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")

@app.get("/", response_class=HTMLResponse)
def index():
    # sert la page d'accueil avec boussole solaire et carte
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Northstar API - Interface non trouvee</h1>"

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Northstar", "version": "1.0.0"}

@app.get("/api/v1/geolocate", response_model=ResultContract)
def get_geolocate(image_path: str = Query("photo_inconnue.jpg")):
    return geolocate_image(image_path)
