from ZODB import FileStorage, DB
import transaction
from persistent import Persistent
from persistent.list import PersistentList
import BTrees.OOBTree
from All_class.Patient import Patient
from All_class.Doctor import Doctor
from All_class.Admin import Admin
from All_class.Nurse import Nurse

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from gui.python.Login import Ui_Form as Login
from gui.python.Signup import Ui_Form as Signup
from gui.python.Add_User import Ui_Form as Add_User
from gui.python.MainWindow2 import Ui_MainWindow as MainWindow
from gui.python.MainWindowAdmin import Ui_MainWindow as MainWindowAdmin

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
    print(user.get_id(), user.__class__.__name__ ,user.fname, user.password)

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
            salary = self.ui.lineEdit_9.text()
            root.user_id_count += 1
            specialty = specialty.split(",")
            doctor = Doctor(fname, lname, address, phone_number, password, root.user_id_count, department, role, specialty, degree, salary)
            root.users[root.user_id_count] = doctor
            root.employee_id_list.append(root.user_id_count)
            transaction.commit()
        elif role == "Admin":
            department = self.ui.lineEdit_6.text()
            root.user_id_count += 1
            admin = Admin(fname, lname, address, phone_number, password, root.user_id_count, department, role)
            root.users[root.user_id_count] = admin
            root.employee_id_list.append(root.user_id_count)
            transaction.commit()
        elif role == "Nurse":
            department = self.ui.lineEdit_6.text()
            assigned_wards = self.ui.lineEdit_7.text()
            qualifications = self.ui.lineEdit_8.text()
            salary = self.ui.lineEdit_9.text()
            root.user_id_count += 1
            assigned_wards = assigned_wards.split(",")
            nurse = Nurse(fname, lname, address, phone_number, password, root.user_id_count, department, role, assigned_wards, qualifications, salary)
            root.users[root.user_id_count] = nurse
            root.employee_id_list.append(root.user_id_count)
            transaction.commit()
        else:
            root.user_id_count += 1
            patient = Patient(fname, lname, address, phone_number, password, root.user_id_count)
            root.users[root.user_id_count] = patient
            transaction.commit()

        self.main_window = MainWindowAdminUI()
        self.main_window.show()
        self.hide()

    def cancel(self):
        self.main_window = MainWindowAdminUI()
        self.main_window.show()
        self.hide()

class MainWindowAdminUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = MainWindowAdmin()
        self.ui.setupUi(self)
        self.showProfilePage()
        self.ui.pushButton_2.clicked.connect(self.showProfilePage)
        self.ui.pushButton_3.clicked.connect(self.showAppointmentPage)
        self.ui.pushButton.clicked.connect(self.showLogPage)
        self.ui.pushButton_5.clicked.connect(self.showListDoctorPage)
        self.ui.pushButton_6.clicked.connect(self.showListNursePage)
        self.ui.pushButton_7.clicked.connect(self.showListPatientPage)
        self.ui.pushButton_8.clicked.connect(self.addUser)
        # self.ui.pushButton_9.clicked.connect(self.showPaymentPage)
        self.ui.pushButton_4.clicked.connect(self.logout)


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
        self.ui.stackedWidget.setCurrentIndex(2)

    def showLogPage(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def showListDoctorPage(self):
        self.ui.stackedWidget.setCurrentIndex(1)

        for i in root.employee_id_list:
            if root.users[i].role == "Doctor":
                self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
                self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1, 1, QTableWidgetItem(root.users[i].get_id()))
                self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1, 1, QTableWidgetItem(root.users[i].get_fname()))
                self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1, 2, QTableWidgetItem(root.users[i].get_lname()))
                self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1, 3, QTableWidgetItem(root.users[i].get_address()))
                self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1, 4, QTableWidgetItem(root.users[i].get_phone_number()))
                self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1, 5, QTableWidgetItem(root.users[i].department))
                self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1, 6, QTableWidgetItem(root.users[i].qualifications))
                self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1, 7, QTableWidgetItem(root.users[i].salary))    
                self.delete_button = QPushButton("Delete")
                self.delete_button.clicked.connect(self.delete_user)
                self.ui.tableWidget.setCellWidget(self.ui.tableWidget.rowCount()-1, 8, self.delete_button)
                # self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount()-1, 7, QTableWidgetItem())    
                      
    def delete_user(self):
        print("delete user")

    def showListNursePage(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def showListPatientPage(self):
        self.ui.stackedWidget.setCurrentIndex(5)
    
    # def showPaymentPage(self):
    #     self.ui.stackedWidget.setCurrentIndex(6)
        
    def addUser(self):
        self.add_user = Add_UserUI()
        self.add_user.show()
        self.hide()


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

def add_doctor():
    root.user_id_count += 1
    doctor = Doctor("John", "Doe", "123 Main St", "123-456-7890", "password", root.user_id_count, "Cardiology", "Doctor", ["Cardiology"], "MD", 100000)
    root.users[root.user_id_count] = doctor
    root.employee_id_list.append(root.user_id_count)
    transaction.commit()

def add_admin():
    root.user_id_count += 1
    admin = Admin("admin", "admin", "123 Main St", "123-456-7890", "password", root.user_id_count, "System Management", "Admin")
    root.users[root.user_id_count] = admin
    root.employee_id_list.append(root.user_id_count)
    transaction.commit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginUI()
    window.show()
    # add_doctor()
    # add_admin()

    # transaction.commit()
    # db.close()
    sys.exit(app.exec())



