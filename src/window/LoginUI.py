from PySide6.QtWidgets import *
from PySide6.QtCore import *
from gui.python.Login import Ui_Form as Login
from database.db import *


class LoginUI(QMainWindow):
    def __init__(self):
        super(LoginUI, self).__init__()
        self.ui = Login()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.authenticate_user)
        self.ui.pushButton_2.clicked.connect(self.show_signup)

    def show_signup(self):
        self.hide()
        from window.SignupUI import SignupUI
        self.signup_window = SignupUI()
        self.signup_window.show()

    def authenticate_user(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        current_user = authenticate_user_db(username, password)

        if not current_user:
            QMessageBox.warning(self, "Authentication Failed", "Invalid username or password.")
        elif current_user.__class__.__name__ == "Admin":
            self.hide()
            from window.MainWindowAdminUI import MainWindowAdminUI
            self.main_window_admin = MainWindowAdminUI(current_user)
            self.main_window_admin.show()
        elif current_user.__class__.__name__ == "Doctor" or current_user.__class__.__name__ == "Nurse":
            self.hide()
            from window.MainWindowDoctorUI import MainWindowDoctorUI
            self.main_window = MainWindowDoctorUI(current_user)
            self.main_window.show()
        else:
            self.hide()
            from window.MainWindowUI import MainWindowUI
            self.main_window = MainWindowUI(current_user)
            self.main_window.show()

