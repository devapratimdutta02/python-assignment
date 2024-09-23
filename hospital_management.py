records = {}

def register_patient(patient_id, full_name, patient_age, illness):
    records[patient_id] = {
        "Full Name": full_name,
        "Age": patient_age,
        "Illness": illness
    }

def show_patient_info(patient_id):
    print(f"The details of the patient are: {records[patient_id]}")

count = int(input("Enter number of patients: "))

for i in range(count):
    patient_id = input("Enter patient ID: ")
    full_name = input("Enter patient's full name: ")
    patient_age = int(input("Enter patient's age: "))
    illness = input("Enter patient's illness: ")
    register_patient(patient_id, full_name, patient_age, illness)
    print()

patient_id_to_display = input("Enter patient ID to display details: ")
show_patient_info(patient_id_to_display)
