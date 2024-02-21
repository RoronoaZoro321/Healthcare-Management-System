from PySide6.QtWidgets import *
from PySide6.QtCore import *

from gui.python.MainWindow3 import Ui_MainWindow as MainWindow

from window.LoginUI import LoginUI

from database.db import root, transaction, current_user


class MainWindowUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = MainWindow()
        self.ui.setupUi(self)
        self.showProfilePage()
        self.ui.pushButton_2.clicked.connect(self.showProfilePage)
        self.ui.pushButton_3.clicked.connect(self.showAppointmentPage)
        self.ui.pushButton_4.clicked.connect(self.logout)
        self.ui.pushButton.clicked.connect(self.showHistoryPage)

    def logout(self):
        self.login = LoginUI()
        self.login.show()
        self.hide()
    
    def showProfilePage(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        
        self.ui.profile_label.setText(f"Name:".ljust(20) + f"{current_user.get_fname()}")
        self.ui.profile_label_2.setText(f"Lastname:".ljust(20) + f"{current_user.get_lname()}")
        self.ui.profile_label_3.setText(f"Role:".ljust(20) + f"{current_user.__class__.__name__}")
        self.ui.profile_label_4.setText(f"Address:".ljust(20) + f"{current_user.get_address()}")
        self.ui.profile_label_5.setText(f"Phone:".ljust(20) + f"{current_user.get_phone_number()}")

    def showAppointmentPage(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def showHistoryPage(self):
        self.ui.stackedWidget.setCurrentIndex(2)
