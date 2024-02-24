from PySide6.QtWidgets import *
from PySide6.QtCore import *

from gui.python.Add_User import Ui_Form as Add_User

from database.db import *


class Add_UserUI(QMainWindow):
    def __init__(self, current_user):
        super(Add_UserUI, self).__init__()
        self.current_user = current_user
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
            add_doctor(self.current_user, fname, lname, address, phone_number, password, department, specialty, degree, salary)
        
        elif role == "Admin":
            department = self.ui.lineEdit_6.text()
            add_admin(self.current_user, fname, lname, address, phone_number, password, department)
        
        elif role == "Nurse":
            department = self.ui.lineEdit_6.text()
            assigned_wards = self.ui.lineEdit_7.text()
            qualifications = self.ui.lineEdit_8.text()
            salary = int(self.ui.lineEdit_9.text())
            add_nurse(self.current_user, fname, lname, address, phone_number, password, department, assigned_wards, qualifications, salary)

        else:
            add_patient(self.current_user, fname, lname, address, phone_number, password)

        from window.MainWindowAdminUI import MainWindowAdminUI
        self.main_window = MainWindowAdminUI(self.current_user)
        self.main_window.show()
        self.hide()

    def cancel(self):
        from window.MainWindowAdminUI import MainWindowAdminUI
        self.main_window = MainWindowAdminUI(self.current_user)
        self.main_window.show()
        self.hide()