from PySide6.QtWidgets import *
from PySide6.QtCore import *

from gui.python.Medicine import Ui_Form as MedicinePY

from database.db import *


class MedicineUI(QMainWindow):
    def __init__(self, current_user):
        super(MedicineUI, self).__init__()
        self.medicine_list = []
        self.current_user = current_user
        self.ui = MedicinePY()
        self.ui.setupUi(self)
        self.ui.lineEdit.textChanged.connect(self.search_medicine)
        self.ui.pushButton.clicked.connect(self.add_medicine)
        self.ui.pushButton_2.clicked.connect(self.select_this_medicine)
        self.ui.pushButton_3.clicked.connect(self.done)
        self.search_medicine()
    
    def add_medicine(self):
        id = self.ui.lineEdit_2.text()
        name = self.ui.lineEdit_3.text()
        description = self.ui.lineEdit_4.text()
        quantity = self.ui.lineEdit_5.text()
        duration = self.ui.lineEdit_6.text()
        when = self.ui.lineEdit_7.text()
        price_per_dose = self.ui.lineEdit_8.text()
        medicine = add_medicine_db(id, name, description, quantity, duration, when, price_per_dose)
        self.ui.lineEdit.setText("")
        # aleart added successfully
        # QMessageBox.about(self, "Success", "Medicine Added Successfully")
        self.search_medicine()
        return medicine

    def search_medicine(self):
        text = self.ui.lineEdit.text()
        self.ui.tableWidget.setRowCount(0)
        medicines = search_medicine_db(text)
        for medicine in medicines:
            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 0, QTableWidgetItem(str(medicine.medicine_id)))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 1, QTableWidgetItem(medicine.name))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 2, QTableWidgetItem(str(medicine.duration)))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 3, QTableWidgetItem(str(medicine.when_to_consume)))
            self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, 4, QTableWidgetItem(str(medicine.price_per_dose)))
            button = QPushButton("Select")
            button.row = self.ui.tableWidget.rowCount() - 1
            button.clicked.connect(self.select_medicine)
            self.ui.tableWidget.setCellWidget(self.ui.tableWidget.rowCount() - 1, 5, button)
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.setAlternatingRowColors(True)
        self.ui.tableWidget.setSortingEnabled(True)
    
    def select_medicine(self):
        row = self.sender().row
        id = self.ui.tableWidget.item(row, 0).text()
        medicine = get_medicine(id)
        self.ui.lineEdit_2.setText(str(medicine.medicine_id))
        self.ui.lineEdit_3.setText(medicine.name)
        self.ui.lineEdit_4.setText(medicine.description)
        self.ui.lineEdit_5.setText(str(medicine.quantity))
        self.ui.lineEdit_6.setText(str(medicine.duration))
        self.ui.lineEdit_7.setText(str(medicine.when_to_consume))
        self.ui.lineEdit_8.setText(str(medicine.price_per_dose))
    
    def select_this_medicine(self):
        medicine = self.add_medicine()
        name = medicine.name
        if medicine not in self.medicine_list and name != "":
            self.medicine_list.append(medicine)
            self.ui.listWidget.addItem(medicine.name)
    
    def done(self):
        save_list_of_medicine(self.medicine_list)
        self.hide()


        

    
       
