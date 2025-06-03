# main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from typing import Optional
import asyncio

app = FastAPI()

@app.post("/extract")
async def extract_data(file: UploadFile = File(...)):
    # Process file asynchronously
    result = await process_pdf_async(file)
    return JSONResponse(content=result, media_type="application/json")