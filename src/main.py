from ZODB import FileStorage, DB
import transaction
from persistent import Persistent
from persistent.list import PersistentList
import BTrees.OOBTree
from All_class.Patient import Patient

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from gui.python.Login import Ui_Form as Login
from gui.python.Signup import Ui_Form as Signup
# from gui.python.Add_User import Ui_Form as Add_User
from gui.python.MainWindow import Ui_MainWindow as MainWindow

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

for patient in root.patients.values():
    print(patient.fname, patient.password)

class LoginUI(QMainWindow):
    def __init__(self):
        super(LoginUI, self).__init__()
        self.ui = Login()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.signup)

    def signup(self):
        self.signup = SignupUI()
        self.signup.show()
        self.hide()

    def login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        for i in root.patients:
            if root.patients[i].get_fname() == username and root.patients[i].get_password() == password:
                patient = root.patients[i]
                self.main_window = QMainWindow()
                self.ui = MainWindow()
                self.ui.setupUi(self.main_window)
                self.main_window.show()
                self.hide()
                return
        QMessageBox.warning(self, "Login Failed", "Invalid username or password")

class SignupUI(QMainWindow):
    def __init__(self):
        super(SignupUI, self).__init__()
        self.ui = Signup()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.signup)
        self.ui.pushButton_2.clicked.connect(self.login)
    
    def login(self):
        self.login = LoginUI()
        self.login.show()
        self.hide()

    def signup(self):
        fname = self.ui.lineEdit.text()
        lname = self.ui.lineEdit_2.text()
        address = self.ui.lineEdit_3.text()
        phone_number = self.ui.lineEdit_4.text()
        password = self.ui.lineEdit_5.text()

        root.patient_id_count += 1
        patient = Patient(fname, lname, address, phone_number, password, root.patient_id_count)
        root.patients[root.patient_id_count] = patient
        transaction.commit()
        
        self.main_window = QMainWindow()
        self.ui = MainWindow()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        self.hide()
        # print(root.patients)


class MainWindowUI(QMainWindow):
    def __init__(self):
        super(MainWindowUI, self).__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginUI()
    window.show()

    # transaction.commit()
    # db.close()
    sys.exit(app.exec())



