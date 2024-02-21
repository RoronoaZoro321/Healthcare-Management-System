from PySide6.QtWidgets import *
from PySide6.QtCore import *

from gui.python.Login import Ui_Form as Login
from window.SignupUI import SignupUI

from window.MainWindowUI import MainWindowUI
from window.MainWindowAdminUI import MainWindowAdminUI

from database.db import root, transaction

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
        global current_user
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        for i in root.users:
            if root.users[i].get_fname() == username and root.users[i].get_password() == password:
                current_user = root.users[i]
                if current_user.__class__.__name__ == "Admin":
                    self.main_window = MainWindowAdminUI()
                else:
                    self.main_window = MainWindowUI()
                self.main_window.show()
                self.hide()
                return
        QMessageBox.warning(self, "Login Failed", "Invalid username or password")
