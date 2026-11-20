from fastapi import FastAPI, HTTPException
from patient_data import find_patient_by_id

app = FastAPI()

@app.get("/patients/{patient_id}")
def get_patient(patient_id: str):
        patient = find_patient_by_id(patient_id)
        if patient is None:
          raise HTTPException(status_code=404, detail="Patient not found")
        return patient
                