from pathlib import Path
from fastapi.responses import FileResponse
from fastapi import FastAPI, HTTPException
from patient_data import find_patient_by_id

app = FastAPI()


@app.get("/")
def home():
    page = Path(__file__).resolve().parent / "index.html"
    return FileResponse(page)


@app.get("/patients/{patient_id}")
def get_patient(patient_id: str):
    patient = find_patient_by_id(patient_id)

    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")

    return patient