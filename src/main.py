from ZODB import FileStorage, DB
import transaction
from persistent import Persistent
from persistent.list import PersistentList
import BTrees.OOBTree
from All_class.Patient import Patient
from All_class.Doctor import Doctor
from All_class.Admin import Admin
from All_class.Nurse import Nurse
from All_class.Appointment import Appointment

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from gui.python.Login import Ui_Form as Login
from gui.python.Signup import Ui_Form as Signup
from gui.python.Add_User import Ui_Form as Add_User
from gui.python.MainWindow2 import Ui_MainWindow as MainWindow
from gui.python.MainWindowAdmin import Ui_MainWindow as MainWindowAdmin

from datetime import datetime, timedelta
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
    root.employee_id_list = PersistentList()

print("has attr appointment", hasattr(root, "appointments"))
if not hasattr(root, 'appointments'):
    root.appointments = BTrees.OOBTree.BTree()

print("appointment id count", hasattr(root, "last_appointment_id"))
if not hasattr(root, 'last_appointment_id'):
    root.last_appointment_id = 0 
    
print("appointment id list: ", hasattr(root, "appointment_id_list"))
if not hasattr(root, "appointment_id_list"):
    root.appointment_id_list = PersistentList()
    
def printInfo():
    print("user id count: ", root.user_id_count)
    print("employee id list: ", root.employee_id_list)
    print("appointment list: ", root.appointment_id_list)
    for user in root.users.values():
        print(user.get_id(), user.__class__.__name__ ,user.fname, user.password)
        # if user.role == "Doctor":
        #     print(type(user.salary))

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
        self.ui.comboBox.setCurrentIndex(1)
        self.ui.textEdit.textChanged.connect(self.search_doctor)
        self.ui.comboBox.currentTextChanged.connect(self.search_doctor)
        self.ui.comboBox_2.currentTextChanged.connect(self.search_doctor)
        self.ui.comboBox_3.currentTextChanged.connect(self.search_doctor)
        self.search_doctor()
        
    def delete_user(self):
        print("delete user")
        # delete the row reated to the button clicked
        button = self.sender()
        index = self.ui.tableWidget.indexAt(button.pos())
        if index.isValid():
            row = index.row()
            user_id = int(self.ui.tableWidget.item(row, 0).text())
            print("user id: ", user_id)
            del root.users[user_id]
            root.employee_id_list.remove(user_id)
            root.employee_id_list._p_changed = True
            transaction.commit()
            self.showListDoctorPage()


    def search_doctor(self):
        self.ui.tableWidget.setRowCount(0)
        search_text = self.ui.textEdit.toPlainText().strip().lower()
        search_attribute = self.ui.comboBox.currentText()
        sort_attribute = self.ui.comboBox_2.currentText()
        sort_attribute_by = self.ui.comboBox_3.currentText()  # Ascending or Descending
        count = 0

        doctors_to_display = []

        for i in root.employee_id_list:
            if root.users[i].role == "Doctor" and search_text in str(getattr(root.users[i], search_attribute)).lower():
                count += 1
                doctors_to_display.append(root.users[i])

        # Sorting the doctors based on the chosen attribute
        if sort_attribute:
            reverse_sort = (sort_attribute_by == "Descending")
            if sort_attribute == "salary":
                doctors_to_display = sorted(doctors_to_display, key=lambda x: float(getattr(x, sort_attribute)), reverse=reverse_sort)
            else:
                doctors_to_display = sorted(doctors_to_display, key=lambda x: getattr(x, sort_attribute), reverse=reverse_sort)

        for doctor in doctors_to_display:
            row_position = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_position)

            self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(doctor.get_id())))
            self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(doctor.get_fname()))
            self.ui.tableWidget.setItem(row_position, 2, QTableWidgetItem(doctor.get_lname()))
            self.ui.tableWidget.setItem(row_position, 3, QTableWidgetItem(doctor.get_address()))
            self.ui.tableWidget.setItem(row_position, 4, QTableWidgetItem(doctor.get_phone_number()))
            self.ui.tableWidget.setItem(row_position, 5, QTableWidgetItem(doctor.department))
            self.ui.tableWidget.setItem(row_position, 6, QTableWidgetItem(doctor.qualifications))
            self.ui.tableWidget.setItem(row_position, 7, QTableWidgetItem(str(doctor.salary)))

            delete_button = QPushButton("Delete")
            delete_button.setStyleSheet("QPushButton{background-color: #b51919; color: white;} QPushButton:hover{background-color: #4f0c0c;}")
            delete_button.clicked.connect(self.delete_user)
            self.ui.tableWidget.setCellWidget(row_position, 8, delete_button)

            # Add Edit button for each row
            edit_button = QPushButton("Edit")
            edit_button.setStyleSheet("QPushButton{background-color: #1f8b4c; color: white;} QPushButton:hover{background-color: #0e3d21;}")
            edit_button.clicked.connect(self.edit_user)
            self.ui.tableWidget.setCellWidget(row_position, 9, edit_button)

        self.ui.label_2.setText(f"Total Doctors: {count}")

    def edit_user(self):
        button = self.sender()
        index = self.ui.tableWidget.indexAt(button.pos())
        if index.isValid():
            row = index.row()
            user_id = int(self.ui.tableWidget.item(row, 0).text())

            editable_columns = range(1, self.ui.tableWidget.columnCount() - 2)  # Exclude buttons

            # Store references to editable widgets for efficiency
            editable_widgets = []
            for column in editable_columns:
                item = self.ui.tableWidget.item(row, column)
                widget = None
                if isinstance(item, QTableWidgetItem):
                    widget = QLineEdit(item.text())
                elif isinstance(item, QComboBox):
                    widget = QComboBox()
                    widget.addItems(item.currentText())  # Copy existing options
                else:
                    # Handle other widget types if needed
                    pass

                if widget:
                    editable_widgets.append(widget)
                    self.ui.tableWidget.setCellWidget(row, column, widget)

            # Add a "Save" button
            save_button = QPushButton("Save")
            save_button.clicked.connect(lambda: self.save_edited_user(row, user_id, editable_widgets))
            self.ui.tableWidget.setCellWidget(row, self.ui.tableWidget.columnCount() - 1, save_button)

    def save_edited_user(self, row, user_id, editable_widgets):
        # Retrieve edited values from the widgets
        data = []
        for widget in editable_widgets:
            value = None
            if isinstance(widget, QLineEdit):
                value = widget.text()
            elif isinstance(widget, QComboBox):
                value = widget.currentText()
            data.append(value)

        # Update the user object and database
        print(data)
        root.users[user_id].update_attributes(data)  # Assuming a method to update attributes
        transaction.commit()

        # Refresh the table to reflect the changes
        self.showListDoctorPage()

        # change the save button back to edit
        edit_button = QPushButton("Edit")
        edit_button.setStyleSheet("QPushButton{background-color: #1f8b4c; color: white;} QPushButton:hover{background-color: #0e3d21;}")
        edit_button.clicked.connect(self.edit_user)
        self.ui.tableWidget.setCellWidget(row, self.ui.tableWidget.columnCount() - 1, edit_button)

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
        
        self.ui.Calendar.selectionChanged.connect(self.onDateChanged)
        self.ui.checkBox.stateChanged.connect(lambda: self.onCheckboxStateChanged(self.ui.checkBox))
        self.ui.checkBox_2.stateChanged.connect(lambda: self.onCheckboxStateChanged(self.ui.checkBox_2))
        self.ui.Submit.clicked.connect(self.handleSubmit)
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
        #Doctor
        self.ui.Speciality.currentIndexChanged.connect(self.updateDoctorList)
        self.updateDoctorList(self.ui.Speciality.currentIndex())
        self.populate_appointments_table()
        
        
    def updateDoctorList(self, index):
        print("triggered")
        self.ui.Doctor.clear()
        selected_specialty = self.ui.Speciality.currentText()

        for user_id, user in root.users.items():
            if isinstance(user, Doctor) and selected_specialty in user.specialty:
                self.ui.Doctor.addItem(f"{user.fname} {user.lname}", user_id)
    
    def onDateChanged(self):
        selected_date = self.ui.Calendar.selectedDate().toPython()
        today = datetime.now().date()
        tomorrow = today + timedelta(days=1)
        
        if selected_date < tomorrow:
            self.ui.checkBox.setEnabled(False)
            self.ui.checkBox_2.setEnabled(False)
        else:
            self.ui.checkBox.setEnabled(True)
            self.ui.checkBox_2.setEnabled(True)
            self.ui.checkBox.stateChanged.connect(lambda: self.onCheckboxStateChanged(self.ui.checkBox))
            self.ui.checkBox_2.stateChanged.connect(lambda: self.onCheckboxStateChanged(self.ui.checkBox_2))

    def onCheckboxStateChanged(self, changedCheckbox):
        if changedCheckbox.isChecked():
            if changedCheckbox == self.ui.checkBox:
                self.ui.checkBox_2.setChecked(False)
            elif changedCheckbox == self.ui.checkBox_2:
                self.ui.checkBox.setChecked(False)
                
    def handleSubmit(self):
        selected_date = self.ui.Calendar.selectedDate().toString(Qt.ISODate)
        start_time = "6:00 am" if self.ui.checkBox.isChecked() else "13:00 pm"
        end_time = "12:00 pm" if self.ui.checkBox.isChecked() else "18:00 pm"
        doctor_id = self.ui.Doctor.currentData()
        patient_id = current_user.get_id()

        if self.has_conflicting_appointment(patient_id, selected_date, start_time, end_time):
            QMessageBox.warning(self, "Appointment Conflict", "You already have an appointment at this time.")
            return

        appointment_id = self.create_and_store_appointment(selected_date, start_time, end_time, doctor_id, patient_id, False)
        print(f"Appointment {appointment_id} created successfully.")
   
    def create_and_store_appointment(self, date, start_time, end_time, doctor_id, patient_id, confirmation):
        print("create and store appointment")
        appointment_id = self.generate_new_appointment_id()
        new_appointment = Appointment(appointment_id, date, start_time, end_time, doctor_id, patient_id, confirmation)
        root.appointments[appointment_id] = new_appointment
        root.appointment_id_list.append(appointment_id)
        self.populate_appointments_table()
        transaction.commit()
        return appointment_id
    
    def has_conflicting_appointment(self, patient_id, date, start_time, end_time):
        for appointment_id, appointment in root.appointments.items():
            if (appointment.patient == patient_id and
                appointment.date == date and
                (appointment.start_time == start_time or appointment.end_time == end_time)):
                return True
        return False

    def populate_appointments_table(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setColumnCount(6)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Doctor', 'Date', 'Start Time', 'End Time', 'Confirmation'])
        patient_id = current_user.get_id()

        patient_appointments = [appointment for appointment_id, appointment in root.appointments.items() if appointment.patient == patient_id]

        self.ui.tableWidget.setRowCount(len(patient_appointments))

        for row, appointment in enumerate(patient_appointments):
            doctor_name = f"{root.users[appointment.doctor].fname} {root.users[appointment.doctor].lname}"
            confirmation = "Yes" if appointment.confirm else "No"
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(doctor_name))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(appointment.date))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(appointment.start_time))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(appointment.end_time))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(confirmation))

            cancel_btn = QPushButton('Cancel')
            cancel_btn.setStyleSheet("QPushButton {background-color: #ff4d4d; color: white;}")
            cancel_btn.clicked.connect(lambda _: self.cancel_appointment(appointment.id))
            self.ui.tableWidget.setCellWidget(row, 5, cancel_btn)
    
    def cancel_appointment(self, appointment_id):
        if appointment_id in root.appointments:
            del root.appointments[appointment_id]
            root.appointment_id_list.remove(appointment_id)
            transaction.commit()
            self.populate_appointments_table()
            QMessageBox.information(self, "Appointment Cancelled", "The appointment has been successfully cancelled.")
        else:
            QMessageBox.warning(self, "Error", "Could not find the appointment to cancel.")
    
    def generate_new_appointment_id(self):
        print("generate appointment id")
        root.last_appointment_id += 1
        transaction.commit()

        return root.last_appointment_id
            
    def showHistoryPage(self):
        self.ui.stackedWidget.setCurrentIndex(2)

def add_doctor(name):
    root.user_id_count += 1
    doctor = Doctor(name, "lname", "123 Main St", "123-456-7890", "password", root.user_id_count, "Surgery", "Doctor", ["Surgery"], "MD", 80000)
    root.users[root.user_id_count] = doctor
    root.employee_id_list.append(root.user_id_count)
    transaction.commit()

def add_admin():
    root.user_id_count += 1
    admin = Admin("admin", "admin", "123 Main St", "123-456-7890", "password", root.user_id_count, "System Management", "Admin")
    root.users[root.user_id_count] = admin
    root.employee_id_list.append(root.user_id_count)
    transaction.commit()

def add_nurse(name):
    root.user_id_count += 1
    nurse = Nurse(name,"lname","123 Main St", "123-456-7890", "password", root.user_id_count, "Surgery", "Nurse", ["Surgery"], "MD", 40000)
    root.users[root.user_id_count] = nurse
    root.employee_id_list.append(root.user_id_count)
    transaction.commit()
    
def print_appointment_info():
    for appointment_id, appointment in root.appointments.items():
        print(f"Appointment ID: {appointment_id}")
        print(f"Date: {appointment.date}")
        print(f"Start Time: {appointment.start_time}")
        print(f"End Time: {appointment.end_time}")
        print(f"Doctor ID: {appointment.doctor}")
        if appointment.doctor in root.users:
            doctor = root.users[appointment.doctor]
            print(f"Doctor Name: {doctor.fname} {doctor.lname}")
        else:
            print("Doctor ID not found in users")
        print(f"Confirmation: {appointment.confirm}")
        print(f"Patient ID: {appointment.patient} \n")
        
def delete_all_appointments():
    appointment_ids = list(root.appointments.keys())
    for appointment_id in appointment_ids:
        del root.appointments[appointment_id]
    transaction.commit()

    root.last_appointment_id = 0
    root.appointment_id_list = PersistentList()
    transaction.commit()
if __name__ == "__main__":

    # add_doctor("doctor1")
    # add_doctor("doctor2")
    # add_doctor("doctor3")
    # add_doctor("doggo")
    # add_doctor("cat")

    # add_admin()
    # add_nurse("nurse1")\
    # delete_all_appointments()
    print_appointment_info()
    printInfo()

    print("All appointments deleted successfully.")
    app = QApplication(sys.argv)
    window = LoginUI()
    window.show()

    # transaction.commit()
    # db.close()
    sys.exit(app.exec())



