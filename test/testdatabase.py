from ZODB import FileStorage, DB
import transaction
from persistent import Persistent
from persistent.list import PersistentList
import BTrees.OOBTree

class Patient(Persistent):
    def __init__(self, name, address, phone_number, medical_history=None):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.medical_history = medical_history or PersistentList()

storage = FileStorage.FileStorage('healthcare_management.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

print("has attr patients: ", hasattr(root, "patients"))
if not hasattr(root, "patients"):
    root.patients = BTrees.OOBTree.BTree()

def add_patient():
    patient1 = Patient("John", "123 Main St", "555-1234")
    patient2 = Patient("Alice", "456 Elm St", "555-5678")

    root.patients[patient1.name] = patient1
    root.patients[patient2.name] = patient2

    transaction.commit()

def get_patient_by_name(name):
    return root.patients[name].name

# def add_medical_history(patient_name, medical_entry):
#     patient = get_patient_by_name(patient_name)
#     if patient:
#         patient.medical_history.append(medical_entry)
#         transaction.commit()
#         return {"message": "Medical history added successfully"}
#     else:
#         return {"error": "Patient not found"}

# add_medical_history("John Doe", "2023-01-15: Checked blood pressure.")
# add_medical_history("Alice Smith", "2023-01-20: Administered medication.")

# Close the database connection when the application stops


if __name__ == "__main__":
    # add_patient()
    print(get_patient_by_name("John"))
    transaction.commit()
    db.close()