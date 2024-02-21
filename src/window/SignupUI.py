from PySide6.QtWidgets import *
from PySide6.QtCore import *
from gui.python.Signup import Ui_Form as Signup
from database.db import register_user_db

class SignupUI(QMainWindow):
    def __init__(self):
        super(SignupUI, self).__init__()
        self.ui = Signup()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.signup)
        self.ui.pushButton_2.clicked.connect(self.show_login)

    def signup(self):
        fname = self.ui.lineEdit.text()
        lname = self.ui.lineEdit_2.text()
        address = self.ui.lineEdit_3.text()
        phone_number = self.ui.lineEdit_4.text()
        password = self.ui.lineEdit_5.text()

        current_user = register_user_db(fname, lname, address, phone_number, password)
        if not current_user:
            QMessageBox.warning(self, "Signup Failed", "Username already exists")
        else:
            self.hide()
            from window.MainWindowUI import MainWindowUI
            self.main_window = MainWindowUI(current_user)
            self.main_window.show()
            self.hide()

    def show_login(self):
        self.hide()
        from window.LoginUI import LoginUI
        self.login_window = LoginUI()
        self.login_window.show()
    
