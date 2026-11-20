patients = [
    {"id":"P001" , "asthma_history":True},
    {"id":"P002" , "asthma_history":False},
    {"id":"P003" , "asthma_history":None},
    {"id":"P004" , "asthma_history":None},
]

def find_missing_asthma_history(records_patients):
    missing_ids = []

    for patient in records_patients:
        print("check:", patient["id"], repr(patient["asthma_history"]))
        if patient["asthma_history"] is None:
            missing_ids.append(patient["id"])

    return missing_ids


result = find_missing_asthma_history(patients)
print(result)