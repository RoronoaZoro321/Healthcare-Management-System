from PySide6.QtWidgets import *
from PySide6.QtCore import *

from gui.python.MainWindowAdmin import Ui_MainWindow as MainWindowAdmin
from database.db import *

class MainWindowAdminUI(QMainWindow):
    def __init__(self, current_user):
        QMainWindow.__init__(self, None)
        self.current_user = current_user
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
        self.ui.pushButton_9.clicked.connect(self.showPaymentPage)
        self.ui.pushButton_4.clicked.connect(self.logout)


    def logout(self):
        from window.LoginUI import LoginUI
        self.login = LoginUI()
        self.login.show()
        self.hide()
    
    def showProfilePage(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        
        self.ui.profile_label_11.setText(f"{self.current_user.get_fname()}")
        self.ui.profile_label_12.setText(f"{self.current_user.get_lname()}")
        self.ui.profile_label_13.setText(f"{self.current_user.__class__.__name__}")
        self.ui.profile_label_14.setText(f"{self.current_user.get_address()}")
        self.ui.profile_label_15.setText(f"{self.current_user.get_phone_number()}")
        
    def showAppointmentPage(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def showLogPage(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.tableWidget_2.setRowCount(0)
        # self.historyTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidget_2.setColumnWidth(0, 300)
        self.ui.tableWidget_2.setColumnWidth(1, 100)
        self.ui.tableWidget_2.setColumnWidth(2, 200)
        self.ui.tableWidget_2.setColumnWidth(3, 100)
        self.show_logs()
        self.ui.textEdit_logs.textChanged.connect(self.show_logs)
        self.ui.textEdit_logs_2.textChanged.connect(self.show_logs)
        self.ui.textEdit_logs_3.textChanged.connect(self.show_logs)
        self.ui.textEdit_logs_4.textChanged.connect(self.show_logs)

    def show_logs(self):
        # textEdit_logs
        logs = get_logs()
        self.ui.tableWidget_2.setRowCount(0)
        time_stamp = self.ui.textEdit_logs.toPlainText()
        actor = self.ui.textEdit_logs_2.toPlainText()
        action = self.ui.textEdit_logs_3.toPlainText()  
        target = self.ui.textEdit_logs_4.toPlainText()
        for log in logs:
            if time_stamp in log.get_time() and actor in log.get_actor_fname() and action in log.get_action() and target in log.get_target_fname():
                row_position = self.ui.tableWidget_2.rowCount()
                self.ui.tableWidget_2.insertRow(row_position)
                self.ui.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(log.get_time()))
                self.ui.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(log.get_actor_fname()))
                self.ui.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(log.get_action()))
                self.ui.tableWidget_2.setItem(row_position, 3, QTableWidgetItem(log.get_target_fname()))
        
        

    def showListDoctorPage(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.comboBox.setCurrentIndex(1)
        self.ui.textEdit.textChanged.connect(self.search_doctor)
        self.ui.comboBox.currentTextChanged.connect(self.search_doctor)
        self.ui.comboBox_2.currentTextChanged.connect(self.search_doctor)
        self.ui.comboBox_3.currentTextChanged.connect(self.search_doctor)
        self.search_doctor()
    
    def showListNursePage(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        self.ui.comboBox_7.setCurrentIndex(1)
        self.ui.textEdit_3.textChanged.connect(self.search_nurse)
        self.ui.comboBox_7.currentTextChanged.connect(self.search_nurse)
        self.ui.comboBox_8.currentTextChanged.connect(self.search_nurse)
        self.ui.comboBox_9.currentTextChanged.connect(self.search_nurse)
        self.search_nurse()

    def showListPatientPage(self):
        self.ui.stackedWidget.setCurrentIndex(6)
        self.ui.comboBox_10.setCurrentIndex(1)
        self.ui.textEdit_4.textChanged.connect(self.search_patient)
        self.ui.comboBox_10.currentTextChanged.connect(self.search_patient)
        self.ui.comboBox_11.currentTextChanged.connect(self.search_patient)
        self.ui.comboBox_12.currentTextChanged.connect(self.search_patient)
        self.search_patient()
    
    def search_user(self, role, search_text, search_attribute, sort_attribute, sort_attribute_by):
        users_to_display = getUserToDisplay(role, search_text, search_attribute)

        # Sorting the doctors based on the chosen attribute
        if sort_attribute:
            reverse_sort = (sort_attribute_by == "Descending")
            if sort_attribute == "salary":
                users_to_display = sorted(users_to_display, key=lambda x: float(getattr(x, sort_attribute)), reverse=reverse_sort)
            else:
                users_to_display = sorted(users_to_display, key=lambda x: getattr(x, sort_attribute), reverse=reverse_sort)

        return users_to_display
    
    def addDeleteandEditButton(self, tableWidget):
        # Add Delete button for each row
        delete_button = QPushButton("Delete")
        delete_button.setStyleSheet("QPushButton{background-color: #b51919; color: white;} QPushButton:hover{background-color: #4f0c0c;}")

        # Add Edit button for each row
        edit_button = QPushButton("Edit")
        edit_button.setStyleSheet("QPushButton{background-color: #1f8b4c; color: white;} QPushButton:hover{background-color: #0e3d21;}")
        return (delete_button, edit_button)


    def search_doctor(self):
        self.ui.tableWidget.setRowCount(0)
        search_text = self.ui.textEdit.toPlainText().strip().lower()
        search_attribute = self.ui.comboBox.currentText()
        sort_attribute = self.ui.comboBox_2.currentText()
        sort_attribute_by = self.ui.comboBox_3.currentText()  # Ascending or Descending
        
        doctors_to_display = self.search_user("Doctor",search_text, search_attribute, sort_attribute, sort_attribute_by)
        count = len(doctors_to_display)
        self.ui.label_2.setText(f"Total Doctors: {count}")

        for doctor in doctors_to_display:
            row_position = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_position)

            self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(doctor.get_id())))
            self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(doctor.get_fname()))
            self.ui.tableWidget.setItem(row_position, 2, QTableWidgetItem(doctor.get_lname()))
            self.ui.tableWidget.setItem(row_position, 3, QTableWidgetItem(doctor.get_address()))
            self.ui.tableWidget.setItem(row_position, 4, QTableWidgetItem(doctor.get_phone_number()))
            self.ui.tableWidget.setItem(row_position, 5, QTableWidgetItem(doctor.get_department()))
            self.ui.tableWidget.setItem(row_position, 6, QTableWidgetItem(doctor.get_qualifications()))
            self.ui.tableWidget.setItem(row_position, 7, QTableWidgetItem(str(doctor.get_salary())))
            self.ui.tableWidget.setItem(row_position, 8, QTableWidgetItem(str(doctor.get_working_time())))

            delete_button, edit_button = self.addDeleteandEditButton(self.ui.tableWidget)
            delete_button.clicked.connect(self.delete_doctor)
            self.ui.tableWidget.setCellWidget(row_position, 9, delete_button)
            edit_button.clicked.connect(self.edit_doctor)
            self.ui.tableWidget.setCellWidget(row_position, 10, edit_button)
    
    def search_nurse(self):
        self.ui.tableWidget_3.setRowCount(0)
        search_text = self.ui.textEdit_3.toPlainText().strip().lower()
        search_attribute = self.ui.comboBox_7.currentText()
        sort_attribute = self.ui.comboBox_9.currentText()
        sort_attribute_by = self.ui.comboBox_8.currentText()
    
        nurses_to_display = self.search_user("Nurse",search_text, search_attribute, sort_attribute, sort_attribute_by)
        count = len(nurses_to_display)
        self.ui.label_4.setText(f"Total Nurses: {count}")

        for nurse in nurses_to_display:
            row_position = self.ui.tableWidget_3.rowCount()
            self.ui.tableWidget_3.insertRow(row_position)

            self.ui.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(str(nurse.get_id())))
            self.ui.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(nurse.get_fname()))
            self.ui.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(nurse.get_lname()))
            self.ui.tableWidget_3.setItem(row_position, 3, QTableWidgetItem(nurse.get_address()))
            self.ui.tableWidget_3.setItem(row_position, 4, QTableWidgetItem(nurse.get_phone_number()))
            self.ui.tableWidget_3.setItem(row_position, 5, QTableWidgetItem(nurse.get_department()))
            self.ui.tableWidget_3.setItem(row_position, 6, QTableWidgetItem(nurse.get_qualifications()))
            self.ui.tableWidget_3.setItem(row_position, 7, QTableWidgetItem(str(nurse.get_salary())))
            self.ui.tableWidget_3.setItem(row_position, 8, QTableWidgetItem(str(nurse.get_working_time())))


            delete_button, edit_button = self.addDeleteandEditButton(self.ui.tableWidget_3)
            delete_button.clicked.connect(self.delete_nurse)
            edit_button.clicked.connect(self.edit_nurse)
            self.ui.tableWidget_3.setCellWidget(row_position, 9, delete_button)
            self.ui.tableWidget_3.setCellWidget(row_position, 10, edit_button)

    def search_patient(self):
        self.ui.tableWidget_4.setRowCount(0)
        search_text = self.ui.textEdit_4.toPlainText().strip().lower()
        search_attribute = self.ui.comboBox_10.currentText()
        sort_attribute = self.ui.comboBox_12.currentText()
        sort_attribute_by = self.ui.comboBox_11.currentText()
        
        patients_to_display = self.search_user("Patient",search_text, search_attribute, sort_attribute, sort_attribute_by)
        count = len(patients_to_display)
        self.ui.label_11.setText(f"Total Patients: {count}")

        for patient in patients_to_display:
            row_position = self.ui.tableWidget_4.rowCount()
            self.ui.tableWidget_4.insertRow(row_position)

            self.ui.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(str(patient.get_id())))
            self.ui.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(patient.get_fname()))
            self.ui.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(patient.get_lname()))
            self.ui.tableWidget_4.setItem(row_position, 3, QTableWidgetItem(patient.get_address()))
            self.ui.tableWidget_4.setItem(row_position, 4, QTableWidgetItem(patient.get_phone_number()))

            delete_button, edit_button = self.addDeleteandEditButton(self.ui.tableWidget_4)
            delete_button.clicked.connect(self.delete_patient)
            edit_button.clicked.connect(self.edit_patient)
            self.ui.tableWidget_4.setCellWidget(row_position, 5, delete_button)
            self.ui.tableWidget_4.setCellWidget(row_position, 6, edit_button)
        
    def delete_doctor(self):
        self.delete_user(self.ui.tableWidget)
        self.showListDoctorPage()

    def delete_nurse(self):
        self.delete_user(self.ui.tableWidget_3)
        self.showListNursePage()

    def delete_patient(self):
        self.delete_user(self.ui.tableWidget_4)
        self.showListPatientPage()
    

    def delete_user(self, tableWidget):
        # delete the row reated to the button clicked
        button = self.sender()
        index = tableWidget.indexAt(button.pos())
        if index.isValid():
            row = index.row()
            user_id = int(tableWidget.item(row, 0).text())
            delete_user_db_by_id(self.current_user, user_id)

    def edit_doctor(self):
        self.edit_user(self.ui.tableWidget, self.save_edited_doctor)
    

    def save_edited_doctor(self, row, user_id, editable_widgets):
        self.save_edited_user(row, user_id, editable_widgets, self.ui.tableWidget, self.showListDoctorPage, self.edit_doctor)

    def edit_nurse(self):
        self.edit_user(self.ui.tableWidget_3, self.save_edited_nurse)

    def save_edited_nurse(self, row, user_id, editable_widgets):
        self.save_edited_user(row, user_id, editable_widgets, self.ui.tableWidget_3, self.showListNursePage, self.edit_nurse)

    def edit_patient(self):
        self.edit_user(self.ui.tableWidget_4, self.save_edited_patient)
    
    def save_edited_patient(self, row, user_id, editable_widgets):
        self.save_edited_user(row, user_id, editable_widgets, self.ui.tableWidget_4, self.showListPatientPage, self.edit_patient)

    def edit_user(self, tableWidget, save_function):
        button = self.sender()
        index = tableWidget.indexAt(button.pos())
        if index.isValid():
            row = index.row()
            user_id = int(tableWidget.item(row, 0).text())

            editable_columns = range(1, tableWidget.columnCount() - 2)  # Exclude buttons

            # Store references to editable widgets for efficiency
            editable_widgets = []
            for column in editable_columns:
                item = tableWidget.item(row, column)
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
                    tableWidget.setCellWidget(row, column, widget)

            # Add a "Save" button
            save_button = QPushButton("Save")
            save_button.clicked.connect(lambda: save_function(row, user_id, editable_widgets))
            tableWidget.setCellWidget(row, tableWidget.columnCount() - 1, save_button)

    def save_edited_user(self, row, user_id, editable_widgets, tableWidget, refresh_function, edit_function):
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
        update_user_attributes(self.current_user, user_id, data)

        # Refresh the table to reflect the changes
        refresh_function()

        # change the save button back to edit
        edit_button = QPushButton("Edit")
        edit_button.setStyleSheet("QPushButton{background-color: #1f8b4c; color: white;} QPushButton:hover{background-color: #0e3d21;}")
        edit_button.clicked.connect(edit_function)
        tableWidget.setCellWidget(row, tableWidget.columnCount() - 1, edit_button)

    def showPaymentPage(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        staffs = get_all_doctor_and_nurse()
        self.ui.tableWidget_5.setRowCount(0)
        total_salary = 0
        for staff in staffs:
            self.ui.tableWidget_5.insertRow(self.ui.tableWidget_5.rowCount())
            self.ui.tableWidget_5.setItem(self.ui.tableWidget_5.rowCount() - 1, 0, QTableWidgetItem(staff.get_role()))
            self.ui.tableWidget_5.setItem(self.ui.tableWidget_5.rowCount() - 1, 1, QTableWidgetItem(staff.get_fname()))
            self.ui.tableWidget_5.setItem(self.ui.tableWidget_5.rowCount() - 1, 2, QTableWidgetItem(str(staff.get_salary())))
            total_salary += float(staff.get_salary())
        self.ui.label_17.setText(f"Total Salary: ${total_salary} / Month")


    def addUser(self):
        from window.Add_UserUI import Add_UserUI
        self.add_user_ui = Add_UserUI(self.current_user)
        self.add_user_ui.show()
        self.hide()
