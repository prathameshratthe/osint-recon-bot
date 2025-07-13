from fastapi import APIRouter, UploadFile, File
from utils.gemini import analyze_image
import base64

router = APIRouter()

@router.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    base64_img = base64.b64encode(image_bytes).decode("utf-8")

    result = await analyze_image(base64_img)
    return {"result": result}
