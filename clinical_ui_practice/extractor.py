#extractor.py is step before the value from main.py list patients 
#extractor.py converts text into values, while main.py checks the existing values.

def extract_asthma_history(note):
    text = note.lower()

    if "no history of asthma" in text:
        return False

    if "history of asthma" in text:
        return True

    return None


hasil = extract_asthma_history("Patient reports a headache")
print(hasil)

hasil = extract_asthma_history("NO HISTORY OF ASTHMA.")
print(hasil)

hasil = extract_asthma_history("HISTORY OF ASTHMA.")
print(hasil)
