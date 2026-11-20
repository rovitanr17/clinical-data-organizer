patients = [
    {"id":"P001" , "asthma_history":True},
    {"id":"P002" , "asthma_history":False},
    {"id":"P003" , "asthma_history":None},
    {"id":"P004" , "asthma_history":None},
]


#function to find patient by id
def find_patient_by_id(patient_id):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient
    return None