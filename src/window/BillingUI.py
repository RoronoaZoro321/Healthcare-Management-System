from PySide6.QtWidgets import *
from PySide6.QtCore import *

from gui.python.Billing import Ui_Form as BillingPY

from database.db import *


class BillingUI(QMainWindow):
    def __init__(self, current_user):
        super(BillingUI, self).__init__()
        self.service_list = []
        self.current_user = current_user
        self.ui = BillingPY()
        self.ui.setupUi(self)
        self.setupTable()
        self.ui.pushButton.clicked.connect(self.add_new_row)
        self.ui.pushButton_2.clicked.connect(self.done)

    def setupTable(self):
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.setAlternatingRowColors(True)

    def add_new_row(self):
        row_count = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_count)
        for col in range(5):
            item = QTableWidgetItem()
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.ui.tableWidget.setItem(row_count, col, item)
    
    def done(self):
        for row in range(self.ui.tableWidget.rowCount()):
            row_data = []
            for col in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, col)
                if item is not None:
                    row_data.append(item.text())
            if len(row_data) == 5:
                name, price, discount_percentage, insurance_name, insurance_coverage = row_data
                service = add_service_db(name, price, discount_percentage, insurance_name, insurance_coverage)
                self.service_list.append(service)
        save_service_list(self.service_list)
        self.hide()
