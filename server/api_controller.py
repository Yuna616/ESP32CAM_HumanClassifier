# server/api_controller.py

from fastapi import APIRouter, UploadFile, Form, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from server.result_storage import ResultStorage
import os
from datetime import datetime

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "..", "images")
RESULTS_PATH = os.path.join(BASE_DIR, "..", "results.json")
TEMPLATES_DIR = os.path.join(BASE_DIR, "..", "templates")

templates = Jinja2Templates(directory=TEMPLATES_DIR)
storage = ResultStorage(IMAGE_DIR, RESULTS_PATH)

@router.post("/save")
async def save_result(
    image: UploadFile,
    label: str = Form(...),
    confidence: float = Form(...),
    timestamp: str = Form(...)
):
    safe_filename = f"{timestamp.replace(':', '-')}_{image.filename}"
    storage.save(image.file, safe_filename, label, confidence, timestamp)
    return {"message": "저장 성공!"}

@router.delete("/delete-result")
async def delete_result(timestamp: str = Query(...)):
    success = storage.delete_by_timestamp(timestamp)
    return {"message": "삭제 완료" if success else "삭제할 데이터가 없습니다."}

@router.get("/results", response_class=HTMLResponse)
async def get_results(request: Request):
    data = storage.load_results()
    return templates.TemplateResponse("results.html", {
        "request": request,
        "results": data
    })
