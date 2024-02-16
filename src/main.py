from ZODB import FileStorage, DB
import transaction
from persistent import Persistent
from persistent.list import PersistentList
import BTrees.OOBTree
from All_class.Patient import Patient
from All_class.Doctor import Doctor

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from gui.python.Login import Ui_Form as Login
from gui.python.Signup import Ui_Form as Signup
# from gui.python.Add_User import Ui_Form as Add_User
from gui.python.MainWindow2 import Ui_MainWindow as MainWindow

storage = FileStorage.FileStorage('healthcare_management.fs')
db = DB(storage)
connection = db.open()
root = connection.root()


current_user = None

print("has attr users: ", hasattr(root, "users"))
if not hasattr(root, "users"):
    root.users = BTrees.OOBTree.BTree()

print("user id count: ", hasattr(root, "user_id_count"))
if not hasattr(root, "user_id_count"):
    root.user_id_count = 0

print("employee id list: ", hasattr(root, "employee_id_list"))
if not hasattr(root, "employee_id_list"):
    root.employee_id_list = []

for user in root.users.values():
    print(user.get_id(), user.fname, user.password)

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
                self.main_window = MainWindowUI()
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


class MainWindowUI(QMainWindow):
    def __init__(self):
        # super(QMainWindow, self).__init__()
        QMainWindow.__init__(self, None)
        self.ui = MainWindow()
        self.ui.setupUi(self)
        self.showProfilePage()
        # self.ui.pushButton_3.clicked.connect(self.display_username)
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
        
        self.ui.profile_label.setText(f"Name:{current_user.get_fname().rjust(20)}")
        self.ui.profile_label_2.setText(f"Lastname:{current_user.get_lname().rjust(20)}")
        self.ui.profile_label_3.setText(f"Role:{current_user.__class__.__name__.rjust(20)}")
        self.ui.profile_label_4.setText(f"Address:{current_user.get_address().rjust(20)}")
        self.ui.profile_label_5.setText(f"Phone:{current_user.get_phone_number().rjust(20)}")
        # if self.ui.__class__.__name__ == "Doctor":
        #     self.ui.profile_label_6.setText("Specialty: " + current_user.get_specialty())
        #     self.ui.profile_label_7.setText("Qualifications: " + current_user.get_qualifications())
        #     self.ui.profile_label_8.setText("Salary: " + current_user.get_salary())

    def showAppointmentPage(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def showHistoryPage(self):
        self.ui.stackedWidget.setCurrentIndex(2)

def add_doctor():
        root.user_id_count += 1
        doctor = Doctor("John", "Doe", "123 Main St", "123-456-7890", "password", root.user_id_count, "Cardiology", "Doctor", ["Cardiology"], "MD", 100000)
        root.users[root.user_id_count] = doctor
        root.employee_id_list.append(root.user_id_count)
        transaction.commit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginUI()
    window.show()
    # add_doctor()

    # transaction.commit()
    # db.close()
    sys.exit(app.exec())



