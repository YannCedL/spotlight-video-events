# API FastAPI pour le moteur Spotlight Video Events
import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from genesis_core import ResultContract
from .detector import detect_video_events

app = FastAPI(
    title="Spotlight Video Events API",
    description="Moteur de Détection d'Événements & Actions Vidéo",
    version="1.0.0"
)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")

@app.get("/", response_class=HTMLResponse)
def index():
    # sert la page d'accueil d'evenements video
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Spotlight API - Interface non trouvee</h1>"

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Spotlight", "version": "1.0.0"}

@app.get("/api/v1/detect", response_model=ResultContract)
def get_detect(video_path: str = Query("surveillance.mp4")):
    return detect_video_events(video_path)
