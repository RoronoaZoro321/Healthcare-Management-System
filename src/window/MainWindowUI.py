from PySide6.QtWidgets import *
from PySide6.QtCore import *

from gui.python.MainWindow2 import Ui_MainWindow as MainWindow

from database.db import *

from datetime import datetime, timedelta

from All_class.Appointment import Appointment
from All_class.Doctor import Doctor
from All_class.Patient import Patient

class MainWindowUI(QMainWindow):
    def __init__(self, current_user):
        QMainWindow.__init__(self, None)
        self.current_user = current_user
        self.ui = MainWindow()
        self.ui.setupUi(self)
        self.showProfilePage()
        self.ui.pushButton_2.clicked.connect(self.showProfilePage)
        self.ui.pushButton_3.clicked.connect(self.showAppointmentPage)
        self.ui.pushButton_4.clicked.connect(self.logout)
        self.ui.pushButton.clicked.connect(self.showHistoryPage)
        self.ui.Doctor.currentIndexChanged.connect(self.updateSpeciality)
        
        self.ui.Calendar.selectionChanged.connect(self.onDateChanged)
        self.ui.checkBox.stateChanged.connect(lambda: self.onCheckboxStateChanged(self.ui.checkBox))
        self.ui.checkBox_2.stateChanged.connect(lambda: self.onCheckboxStateChanged(self.ui.checkBox_2))
        self.ui.Submit.clicked.connect(self.handleSubmit)

    def logout(self):
        from window.LoginUI import LoginUI
        self.login = LoginUI()
        self.login.show()
        self.hide()
        
    def showProfilePage(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        
        self.ui.profile_label.setText(f"{self.current_user.get_fname()}")
        self.ui.profile_label_2.setText(f"{self.current_user.get_lname()}")
        self.ui.profile_label_3.setText(f"{self.current_user.__class__.__name__}")
        self.ui.profile_label_4.setText(f"{self.current_user.get_address()}")
        self.ui.profile_label_5.setText(f"{self.current_user.get_phone_number()}")

    def showAppointmentPage(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        #Doctor
        self.ui.Department.currentIndexChanged.connect(self.updateDoctorList)
        self.updateDoctorList(self.ui.Department.currentIndex())
        self.populate_appointments_table()
        
    def updateDoctorList(self, index):
        print("Update Doctor List triggered")
        self.ui.Doctor.clear()
        selected_department = self.ui.Department.currentText()
        print(f"Selected Specialty: {selected_department}")
        for user_id, user in root.users.items():
            if isinstance(user, Doctor):
                print(f"Checking Doctor: {user.fname} with specialties {user.department}")
                if selected_department in user.department:
                    print(f"Adding Doctor: {user.fname}")
                    self.ui.Doctor.addItem(f"{user.fname} {user.lname}", user_id)

    def updateSpeciality(self, index):
        self.ui.Speciality.clear()
        doctor_id = self.ui.Doctor.itemData(index)
        if doctor_id is not None:
            doctor = root.users.get(doctor_id)
            if doctor and isinstance(doctor, Doctor):
                for specialty in doctor.get_specialty():
                    self.ui.Speciality.addItem(specialty)
                self.updateCheckboxLabelsForDoctor(doctor.working_time)

    def updateCheckboxLabelsForDoctor(self, working_time):
        lunch_start = datetime.strptime("12:00", '%H:%M')
        lunch_end = datetime.strptime("13:00", '%H:%M')

        start_end = working_time.split('-')
        start_time = datetime.strptime(start_end[0].strip(), '%H:%M')
        end_time = datetime.strptime(start_end[1].strip(), '%H:%M')

        if start_time < lunch_start and end_time > lunch_end:
            total_working_seconds = (lunch_start - start_time).total_seconds() + (end_time - lunch_end).total_seconds()
            midpoint_seconds = total_working_seconds / 2

            if midpoint_seconds <= (lunch_start - start_time).total_seconds():
                midpoint = start_time + timedelta(seconds=midpoint_seconds)
                second_half_start = lunch_end
            else:
                midpoint_seconds -= (lunch_end - lunch_start).total_seconds()
                midpoint = lunch_end
                second_half_start = lunch_end + timedelta(seconds=midpoint_seconds - (lunch_start - start_time).total_seconds())
                
            first_half_label = f"{start_time.strftime('%H:%M')} - {midpoint.strftime('%H:%M')}"
            second_half_label = f"{second_half_start.strftime('%H:%M')} - {end_time.strftime('%H:%M')}"
        else:
            midpoint = start_time + (end_time - start_time) / 2
            first_half_label = f"{start_time.strftime('%H:%M')} - {midpoint.strftime('%H:%M')}"
            second_half_label = f"{midpoint.strftime('%H:%M')} - {end_time.strftime('%H:%M')}"

        self.ui.checkBox.setText(first_half_label)
        self.ui.checkBox_2.setText(second_half_label)


                    
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

        if self.ui.checkBox.isChecked():
            time_range = self.ui.checkBox.text().split('-')
        elif self.ui.checkBox_2.isChecked():
            time_range = self.ui.checkBox_2.text().split('-')
        else:
            QMessageBox.warning(self, "No Time Slot Selected", "Please select a time slot for the appointment.")
            return

        start_time = time_range[0].strip()
        end_time = time_range[1].strip()

        doctor_id = self.ui.Doctor.currentData()
        doctor_speciality_selected = self.ui.Speciality.currentText()
        patient_id = self.current_user.get_id()

        if self.has_conflicting_appointment(patient_id, selected_date, start_time, end_time):
            QMessageBox.warning(self, "Appointment Conflict", "You already have an appointment at this time.")
            return

        appointment_id = self.create_and_store_appointment(selected_date, start_time, end_time, doctor_id, doctor_speciality_selected, patient_id, False)
        
        if appointment_id:
            QMessageBox.information(self, "Appointment Scheduled", f"Appointment {appointment_id} created successfully.")
        else:
            QMessageBox.warning(self, "Appointment Error", "There was an error scheduling the appointment.")

   
    def create_and_store_appointment(self, date, start_time, end_time, doctor_id, doctor_speciality_selected, patient_id, confirmation):
        print("create and store appointment")
        appointment_id = self.generate_new_appointment_id()
        new_appointment = Appointment(appointment_id, date, start_time, end_time, doctor_id, doctor_speciality_selected, patient_id, confirmation)
        root.appointments[appointment_id] = new_appointment
        root.appointment_id_list.append(appointment_id)
        
        patient = root.users.get(patient_id)
        doctor = root.users.get(doctor_id)

        if patient and isinstance(patient, Patient) and doctor and isinstance(doctor, Doctor):
            patient.add_appointment(appointment_id)
            doctor.add_appointment(appointment_id)
            
            transaction.commit()
            self.populate_appointments_table()
            
            return appointment_id
        else:
            print("Error: Could not find the patient or doctor, or they were of the wrong type.")
            return None
        
    def has_conflicting_appointment(self, patient_id, date, start_time, end_time):
        for appointment_id, appointment in root.appointments.items():
            if (appointment.patient == patient_id and
                appointment.date == date and
                (appointment.start_time == start_time or appointment.end_time == end_time)):
                return True
        return False

    def populate_appointments_table(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Doctor', 'Speciality Selected', 'Date', 'Start Time', 'End Time', 'Confirmation', 'Cancle'])
        patient_id = self.current_user.get_id()

        patient_appointments = [appointment for appointment_id, appointment in root.appointments.items() if appointment.patient == patient_id]

        self.ui.tableWidget.setRowCount(len(patient_appointments))

        for row, appointment in enumerate(patient_appointments):
            doctor_name = f"{root.users[appointment.doctor].fname} {root.users[appointment.doctor].lname}"
            doctor_speciality = appointment.speciality
            confirmation = "Yes" if appointment.confirm else "No"
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(doctor_name))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(doctor_speciality))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(appointment.date))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(appointment.start_time))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(appointment.end_time))
            self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(confirmation))

            cancel_btn = QPushButton('Cancel')
            cancel_btn.setStyleSheet("QPushButton {background-color: #ff4d4d; color: white;}")
            cancel_btn.clicked.connect(lambda _: self.cancel_appointment(appointment.id))
            self.ui.tableWidget.setCellWidget(row, 6, cancel_btn)
    
    def cancel_appointment(self, appointment_id):
        if appointment_id in root.appointments:
            appointment = root.appointments[appointment_id]

            patient = root.users.get(appointment.patient, None)
            doctor = root.users.get(appointment.doctor, None)

            if patient and isinstance(patient, Patient):
                if appointment_id in patient.appointments:
                    patient.appointments.remove(appointment_id)

            if doctor and isinstance(doctor, Doctor):
                if appointment_id in doctor.appointments:
                    doctor.appointments.remove(appointment_id)

            del root.appointments[appointment_id]

            if appointment_id in root.appointment_id_list:
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
