# server/app.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from server.api_controller import router
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "images")

app = FastAPI()
app.mount("/images", StaticFiles(directory=IMAGE_DIR), name="images")
app.include_router(router)
