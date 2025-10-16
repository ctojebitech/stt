from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

app = FastAPI(title="Speech-to-Text + Extraction API (Single Gemini Model)")

def get_gemini_model():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not set")
    genai.configure(api_key=api_key)
    # ✅ Use a multimodal model
    # return genai.GenerativeModel("gemini-1.5-pro")  
    return genai.GenerativeModel("models/gemini-2.0-flash")

@app.post("/process_audio")
async def process_audio(file: UploadFile = File(...)):
    try:
        data = await file.read()
        if not data:
            raise HTTPException(status_code=400, detail="File is empty")

        model = get_gemini_model()
        mime_type = file.content_type or "audio/wav"

        # ✅ Single call for both transcription + extraction
        prompt = (
            "Transcribe the audio, then extract and return the following fields as JSON:\n"
            "organization, unit_type, unit, title, task_type, template, description.\n"
            "If a field is missing, return it as null.\n\n"
            "Response format:\n"
            "{\n"
            "  'organization': '',\n"
            "  'unit_type': '',\n"
            "  'unit': '',\n"
            "  'title': '',\n"
            "  'task_type': '',\n"
            "  'template': '',\n"
            "  'description': ''\n"
            "}\n"
        )

        response = model.generate_content([
            {"text": prompt},
            {"mime_type": mime_type, "data": data}
        ])

        result_text = getattr(response, "text", "").strip()
        return JSONResponse({
            "result": result_text,
            "model": model.model_name,
            "filename": file.filename,
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
