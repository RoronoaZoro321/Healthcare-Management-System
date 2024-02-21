from PySide6.QtWidgets import *
from PySide6.QtCore import *

from gui.python.MainWindowAdmin import Ui_MainWindow as MainWindowAdmin
from database.db import root, transaction

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
        # self.ui.pushButton_9.clicked.connect(self.showPaymentPage)
        self.ui.pushButton_4.clicked.connect(self.logout)


    def logout(self):
        from window.LoginUI import LoginUI
        self.login = LoginUI()
        self.login.show()
        self.hide()
    
    def showProfilePage(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        
        self.ui.profile_label.setText(f"Name:".ljust(20) + f"{self.current_user.get_fname()}")
        self.ui.profile_label_2.setText(f"Lastname:".ljust(20) + f"{self.current_user.get_lname()}")
        self.ui.profile_label_3.setText(f"Role:".ljust(20) + f"{self.current_user.__class__.__name__}")
        self.ui.profile_label_4.setText(f"Address:".ljust(20) + f"{self.current_user.get_address()}")
        self.ui.profile_label_5.setText(f"Phone:".ljust(20) + f"{self.current_user.get_phone_number()}")

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
    
    def delete_doctor(self):
        self.delete_user()
        print("delete doctor")
        self.showListDoctorPage()
        
    def delete_user(self):
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
            delete_button.clicked.connect(self.delete_doctor)
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
        from window.Add_UserUI import Add_UserUI
        self.add_user_ui = Add_UserUI(self.current_user)
        self.add_user_ui.show()
        self.hide()
