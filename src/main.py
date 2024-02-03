from ZODB import FileStorage, DB
import transaction
from persistent import Persistent
from persistent.list import PersistentList
import BTrees.OOBTree
from All_class.all import Patient

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from gui.python.Login import Login
from gui.python.Signup import Signup

storage = FileStorage.FileStorage('healthcare_management.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

print("has attr patients: ", hasattr(root, "patients"))
if not hasattr(root, "patients"):
    root.patients = BTrees.OOBTree.BTree()

print("patience id count: ", hasattr(root, "patient_id_count"))
if not hasattr(root, "patient_id_count"):
    root.patient_id_count = 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    Widget = QWidget()
    login.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec())
    transaction.commit()
    db.close()





















# def add_patient(name: str, address: str, phone_number: str, medical_history: str):
#     root.patient_id_count += 1
#     patient_id = root.patient_id_count
#     patient = Patient(name, address, phone_number, patient_id, medical_history)
#     root.patients[patient_id] = patient
#     transaction.commit()

# def get_patient_by_id(patient_id):
#     return root.patients[patient_id]
