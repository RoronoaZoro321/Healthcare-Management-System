from PySide6.QtWidgets import *
from PySide6.QtCore import *

from gui.python.Medicine import Ui_Form as Medicine

from database.db import *


class Medicine(QMainWindow):
    def __init__(self, current_user):
        super(Medicine, self).__init__()
        self.current_user = current_user
        self.ui = Medicine()
        self.ui.setupUi(self)
        # self.ui.pushButton.clicked.connect(self.add_user)
        self.ui.textEdit.onTextChanged.connect(self.search_medicine)
    
    def add_medicine(self):
        name = self.ui.lineEdit_2.text()
        description = self.ui.lineEdit_3.text()
        quantity = self.ui.lineEdit_4.text()
        duration = self.ui.lineEdit_5.text()
        when = self.ui.lineEdit_6.text()
        price_per_dose = self.ui.lineEdit_7.text()
        add_medicine_db(name, description, quantity, duration, when, price_per_dose)

    def search_medicine(self):
        text = self.ui.textEdit.toPlainText()
        self.ui.listWidget.clear()
        medicines = search_medicine_db(text)
        for medicine in medicines:
            self.ui.listWidget.addItem(medicine.name)
    
    
       
