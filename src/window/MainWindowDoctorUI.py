from PySide6.QtWidgets import *
from PySide6.QtCore import *

from gui.python.MainWindowDoctor import Ui_MainWindow as MainWindow

from database.db import *

from datetime import datetime, timedelta

class MainWindowDoctorUI(QMainWindow):
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
        self.ui.pushButton_9.clicked.connect(self.showWriteReportPage)

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
        self.ui.stackedWidget.setCurrentIndex(1)

            
    def showHistoryPage(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def showWriteReportPage(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.label_16.setText(self.current_user.get_fname())
        # self.ui.pushButton_10.clicked.connect(self.writeReport) 
        self.addPatientToComboBox()
        self.ui.comboBox.currentTextChanged.connect(self.showPatientInfo)
        self.ui.pushButton_6.clicked.connect(self.showMedicinePage)
    
    def addPatientToComboBox(self):
        self.ui.comboBox.clear()
        patients = get_all_patients()
        for patient in patients:
            self.ui.comboBox.addItem(patient.get_fname() + " " + patient.get_lname())
    
    def showPatientInfo(self):
        # print(self.ui.comboBox.currentText().split()[0])
        if self.ui.comboBox.currentText() == "":
            return
        patient = get_patient_by_name(self.ui.comboBox.currentText().split()[0])
        self.ui.label_17.setText(f"Name: {patient.get_fname()}")
        self.ui.label_18.setText(f"Lastname: {patient.get_lname()}")
        self.ui.label_19.setText(f"Address: {patient.get_address()}")
        self.ui.label_20.setText(f"Phone: {patient.get_phone_number()}")
    
    def showMedicinePage(self):
        from window.MedicineUI import MedicineUI
        self.medicine = MedicineUI(self.current_user)
        self.medicine.show()



    # def 
    