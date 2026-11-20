from clinical_ui_practice.patient_data import patients

def find_missing_asthma_history(records_patients):
    missing_ids = []

    for patient in records_patients:
        #print("check:", patient["id"], repr(patient["asthma_history"])) //function to check asthma_history_bug 
        if patient["asthma_history"] is None:
            missing_ids.append(patient["id"])

    return missing_ids


result = find_missing_asthma_history(patients)
print(result)
