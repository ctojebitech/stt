## Speech-to-Text API (FastAPI + Gemini)

### Setup
- Create a `.env` file with:
  - `GEMINI_API_KEY=your_api_key_here`

### Install
```bash
pip install -r requirements.txt
```

### Run
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Usage
```bash
curl -X POST "http://localhost:8000/transcribe" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/audio.wav"
```

Supported formats depend on Gemini, but common types like WAV, MP3, M4A, and MP4 generally work.



