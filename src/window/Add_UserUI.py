from PySide6.QtWidgets import *
from PySide6.QtCore import *

from gui.python.Add_User import Ui_Form as Add_User

from window.MainWindowAdminUI import MainWindowAdminUI

from database.db import root, transaction

from All_class.Doctor import Doctor
from All_class.Admin import Admin
from All_class.Nurse import Nurse
from All_class.Patient import Patient


class Add_UserUI(QMainWindow):
    def __init__(self):
        super(Add_UserUI, self).__init__()
        self.ui = Add_User()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_user)
        self.ui.pushButton_2.clicked.connect(self.cancel)
        self.ui.comboBox.currentTextChanged.connect(self.show_fields)
        self.ui.lineEdit_6.hide()
        self.ui.lineEdit_7.hide()
        self.ui.lineEdit_8.hide()
        self.ui.lineEdit_9.hide()

    def show_fields(self):
        role = self.ui.comboBox.currentText()
        if role == "Doctor":
            self.ui.lineEdit_6.show()
            self.ui.lineEdit_7.show()
            self.ui.lineEdit_8.show()
            self.ui.lineEdit_9.show()
        elif role == "Nurse":
            self.ui.lineEdit_6.show()
            self.ui.lineEdit_7.placeholderText = "Assigned Wards"
            self.ui.lineEdit_7.show()
            self.ui.lineEdit_8.show()
            self.ui.lineEdit_9.show()
        elif role == "Admin":
            self.ui.lineEdit_6.show()
            self.ui.lineEdit_7.hide()
            self.ui.lineEdit_8.hide()
            self.ui.lineEdit_9.hide()
        else:
            self.ui.lineEdit_6.hide()
            self.ui.lineEdit_7.hide()
            self.ui.lineEdit_8.hide()
            self.ui.lineEdit_9.hide()

    def add_user(self):
        fname = self.ui.lineEdit.text()
        lname = self.ui.lineEdit_2.text()
        address = self.ui.lineEdit_3.text()
        phone_number = self.ui.lineEdit_4.text()
        password = self.ui.lineEdit_5.text()
        role = self.ui.comboBox.currentText()

        if role == "Doctor":
            department = self.ui.lineEdit_6.text()
            specialty = self.ui.lineEdit_7.text()
            degree = self.ui.lineEdit_8.text()
            salary = int(self.ui.lineEdit_9.text())
            root.user_id_count += 1
            specialty = specialty.split(",")
            doctor = Doctor(fname, lname, address, phone_number, password, root.user_id_count, department, role, specialty, degree, salary)
            root.users[root.user_id_count] = doctor
            root.employee_id_list.append(root.user_id_count)
            transaction.commit()
            print("doctor added")
        elif role == "Admin":
            department = self.ui.lineEdit_6.text()
            root.user_id_count += 1
            admin = Admin(fname, lname, address, phone_number, password, root.user_id_count, department, role)
            root.users[root.user_id_count] = admin
            root.employee_id_list.append(root.user_id_count)
            transaction.commit()
            print("admin added")
        elif role == "Nurse":
            department = self.ui.lineEdit_6.text()
            assigned_wards = self.ui.lineEdit_7.text()
            qualifications = self.ui.lineEdit_8.text()
            salary = int(self.ui.lineEdit_9.text())
            root.user_id_count += 1
            assigned_wards = assigned_wards.split(",")
            nurse = Nurse(fname, lname, address, phone_number, password, root.user_id_count, department, role, assigned_wards, qualifications, salary)
            root.users[root.user_id_count] = nurse
            root.employee_id_list.append(root.user_id_count)
            transaction.commit()
            print("nurse added")
        else:
            root.user_id_count += 1
            patient = Patient(fname, lname, address, phone_number, password, root.user_id_count)
            root.users[root.user_id_count] = patient
            transaction.commit()
            print("patient added")

        self.main_window = MainWindowAdminUI()
        self.main_window.show()
        self.hide()

    def cancel(self):
        self.main_window = MainWindowAdminUI()
        self.main_window.show()
        self.hide()
