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
        self.ui.pushButton.clicked.connect(self.showMedicalRecordPage)
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
            
    def showMedicalRecordPage(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.tableWidget.setRowCount(0)
        reports = get_all_reports()
        for report in reports:
            patient_name = get_patient_by_id(report.patient_id).get_fname()
            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 0, QTableWidgetItem(str(patient_name)))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 1, QTableWidgetItem(str(report.medical_record.title)))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 2, QTableWidgetItem(str(report.date)))
            button = QPushButton("View")
            button.report = report
            button.clicked.connect(self.viewReport)
            self.ui.tableWidget.setCellWidget(self.ui.tableWidget.rowCount() - 1, 3, button)
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.setAlternatingRowColors(True)


    def viewReport(self):
        report = self.sender().report
        print(report.medical_record.title)
        # self.ui.stackedWidget.setCurrentIndex(3)
        # self.ui.label_16.setText(self.current_user.get_fname())
        # self.ui.label_17.setText(f"Name: {get_patient_by_id(report.patient_id).get_fname()}")
        # self.ui.label_18.setText(f"Lastname: {get_patient_by_id(report.patient_id).get_lname()}")
        # self.ui.label_19.setText(f"Address: {get_patient_by_id(report.patient_id).get_address()}")
        # self.ui.label_20.setText(f"Phone: {get_patient_by_id(report.patient_id).get_phone_number()}")
        # self.ui.label_21.setText(f"Height: {report.medical_record.height}")
        # self.ui.label_22.setText(f"Weight: {report.medical_record.weight}")
        # self.ui.label_23.setText

    def showWriteReportPage(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.label_16.setText(self.current_user.get_fname())
        # self.ui.pushButton_10.clicked.connect(self.writeReport) 
        self.addPatientToComboBox()
        self.ui.comboBox.currentTextChanged.connect(self.showPatientInfo)
        self.ui.pushButton_6.clicked.connect(self.showMedicinePage)
        self.ui.pushButton_5.clicked.connect(self.writeReport)
        self.ui.pushButton_7.clicked.connect(self.showBillPage)
        self.showListofBillingAndMedicine()
        self.ui.pushButton_8.clicked.connect(self.showListofBillingAndMedicine)
        self.ui.pushButton_10.clicked.connect(self.showListofBillingAndMedicine)

    def showListofBillingAndMedicine(self):
        self.ui.listWidget.clear()
        self.ui.listWidget_2.clear()
        list_of_medicine = get_list_of_medicine()
        for medicine in list_of_medicine:
            self.ui.listWidget.addItem(medicine.name)
        list_of_billing = get_list_of_service()
        for bill in list_of_billing:
            self.ui.listWidget_2.addItem(bill.name)
    
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

    def showBillPage(self):
        from window.BillingUI import BillingUI
        self.bill = BillingUI(self.current_user)
        self.bill.show()

    def writeReport(self):
        print("write report")
        height = self.ui.lineEdit.text()
        weight = self.ui.lineEdit_2.text()
        sex = self.ui.lineEdit_3.text()
        pulse_rate = self.ui.lineEdit_4.text()
        blood_pressure = self.ui.lineEdit_5.text()
        allegies = self.ui.lineEdit_6.text()
        title = self.ui.lineEdit_7.text()
        description = self.ui.lineEdit_8.text()
        details = self.ui.textEdit_2.toPlainText()

        medical_record = createMedicalRecord(height, weight, sex, pulse_rate, blood_pressure, allegies, title, description, details)

        overallDiscount = float(self.ui.lineEdit_9.text())
        bill = createBill(overallDiscount)

        patient_id = get_patient_by_name(self.ui.comboBox.currentText().split()[0]).get_id()

        report = add_report(patient_id, self.current_user, medical_record, bill)
        QMessageBox.about(self, "Success", "Report added successfully")
