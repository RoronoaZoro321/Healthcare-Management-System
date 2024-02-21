from PySide6.QtWidgets import *
from PySide6.QtCore import *

from gui.python.Signup import Ui_Form as Signup

from window.LoginUI import LoginUI
from MainWindowUI import MainWindowUI

from database.db import root, transaction

from All_class.Patient import Patient

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

        for i in root.users:
            if root.users[i].get_fname() == fname:
                QMessageBox.warning(self, "Signup Failed", "User already exists")
                return

        root.user_id_count += 1
        patient = Patient(fname, lname, address, phone_number, password, root.user_id_count)
        root.users[root.user_id_count] = patient
        transaction.commit()

        global current_user
        current_user = patient
        self.main_window = MainWindowUI()
        self.main_window.show()
        self.hide()
