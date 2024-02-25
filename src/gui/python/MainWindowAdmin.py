# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowAdmin.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
from . import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"font: 13pt \"Osaka\";")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(230, 0, 1051, 721))
        self.widget_2.setStyleSheet(u"background-color: #F8FAFC;\n"
"color: #353535;")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_3 = QWidget(self.page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"")
        self.profile_widget = QWidget(self.widget_3)
        self.profile_widget.setObjectName(u"profile_widget")
        self.profile_widget.setGeometry(QRect(100, 90, 781, 461))
        self.profile_widget.setStyleSheet(u"QWidget {\n"
"	border: 3px solid #353535;\n"
"	border-radius: 15px;\n"
"	font: 18px;\n"
"	padding: 20px;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.profile_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.profile_label = QLabel(self.profile_widget)
        self.profile_label.setObjectName(u"profile_label")
        self.profile_label.setStyleSheet(u"border-style: none;")

        self.verticalLayout.addWidget(self.profile_label)

        self.profile_label_2 = QLabel(self.profile_widget)
        self.profile_label_2.setObjectName(u"profile_label_2")
        self.profile_label_2.setStyleSheet(u"border-style: none;")

        self.verticalLayout.addWidget(self.profile_label_2)

        self.profile_label_3 = QLabel(self.profile_widget)
        self.profile_label_3.setObjectName(u"profile_label_3")
        self.profile_label_3.setStyleSheet(u"border-style: none;")

        self.verticalLayout.addWidget(self.profile_label_3)

        self.profile_label_4 = QLabel(self.profile_widget)
        self.profile_label_4.setObjectName(u"profile_label_4")
        self.profile_label_4.setStyleSheet(u"border-style: none;")

        self.verticalLayout.addWidget(self.profile_label_4)

        self.profile_label_5 = QLabel(self.profile_widget)
        self.profile_label_5.setObjectName(u"profile_label_5")
        self.profile_label_5.setStyleSheet(u"border-style: none;")

        self.verticalLayout.addWidget(self.profile_label_5)


        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.widget_list_doctor = QWidget(self.page_4)
        self.widget_list_doctor.setObjectName(u"widget_list_doctor")
        self.widget_list_doctor.setGeometry(QRect(-10, -10, 1061, 721))
        self.tableWidget = QTableWidget(self.widget_list_doctor)
        if (self.tableWidget.columnCount() < 11):
            self.tableWidget.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(100, 170, 871, 521))
        self.tableWidget.setStyleSheet(u"            QTableWidget {\n"
"                background-color: #f8f9fa;\n"
"                border: 2px solid #dee2e6;\n"
"                border-radius: 8px;\n"
"                selection-background-color: #007bff;\n"
"            }\n"
"\n"
"            QTableWidget::item {\n"
"                color: #495057;\n"
"                border-bottom: 1px solid #dee2e6;\n"
"            }\n"
"\n"
"            QTableWidget::item:selected {\n"
"                background-color: #007bff;\n"
"                color: #ffffff;\n"
"            }\n"
"\n"
"            QTableWidget::item:hover {\n"
"                background-color: #e0e0e0;\n"
"            }\n"
"\n"
"            QHeaderView::section {\n"
"                background-color: #343a40;\n"
"                color: #ffffff;\n"
"                border: 1px solid #343a40;\n"
"                border-radius: 4px;\n"
"                padding: 8px;\n"
"            }\n"
"\n"
"            QHeaderView::section:hover {\n"
"                background-color: #495057;\n"
"       "
                        "     }")
        self.label_2 = QLabel(self.widget_list_doctor)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(680, 80, 181, 31))
        self.widget_5 = QWidget(self.widget_list_doctor)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(110, 30, 411, 121))
        self.gridLayout_3 = QGridLayout(self.widget_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.widget_5)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_3.addWidget(self.comboBox, 0, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.widget_5)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_3.addWidget(self.comboBox_3, 2, 2, 1, 1)

        self.textEdit = QTextEdit(self.widget_5)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_3.addWidget(self.textEdit, 1, 0, 1, 3)

        self.comboBox_2 = QComboBox(self.widget_5)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_3.addWidget(self.comboBox_2, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.appointment_page = QLabel(self.page_2)
        self.appointment_page.setObjectName(u"appointment_page")
        self.appointment_page.setGeometry(QRect(7, 35, 1011, 611))
        self.appointment_page.setStyleSheet(u"color: black;")
        self.appointment_page.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.log_page = QWidget(self.page_3)
        self.log_page.setObjectName(u"log_page")
        self.log_page.setGeometry(QRect(-10, -10, 1051, 721))
        self.tableWidget_2 = QTableWidget(self.log_page)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(80, 200, 791, 461))
        self.tableWidget_2.setStyleSheet(u"")
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.widget_9 = QWidget(self.log_page)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(80, 10, 331, 171))
        self.verticalLayout_3 = QVBoxLayout(self.widget_9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textEdit_logs = QTextEdit(self.widget_9)
        self.textEdit_logs.setObjectName(u"textEdit_logs")

        self.verticalLayout_3.addWidget(self.textEdit_logs)

        self.textEdit_logs_2 = QTextEdit(self.widget_9)
        self.textEdit_logs_2.setObjectName(u"textEdit_logs_2")

        self.verticalLayout_3.addWidget(self.textEdit_logs_2)

        self.textEdit_logs_3 = QTextEdit(self.widget_9)
        self.textEdit_logs_3.setObjectName(u"textEdit_logs_3")

        self.verticalLayout_3.addWidget(self.textEdit_logs_3)

        self.textEdit_logs_4 = QTextEdit(self.widget_9)
        self.textEdit_logs_4.setObjectName(u"textEdit_logs_4")

        self.verticalLayout_3.addWidget(self.textEdit_logs_4)

        self.stackedWidget.addWidget(self.page_3)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.widget_list_nurse = QWidget(self.page_5)
        self.widget_list_nurse.setObjectName(u"widget_list_nurse")
        self.widget_list_nurse.setGeometry(QRect(-10, -10, 1061, 721))
        self.widget_6 = QWidget(self.widget_list_nurse)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(70, 100, 921, 571))
        self.widget_6.setStyleSheet(u"font: 13pt \"Arial\";")
        self.tableWidget_3 = QTableWidget(self.widget_6)
        if (self.tableWidget_3.columnCount() < 11):
            self.tableWidget_3.setColumnCount(11)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(9, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(10, __qtablewidgetitem25)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(10, 100, 881, 421))
        self.tableWidget_3.setStyleSheet(u"            QTableWidget {\n"
"                background-color: #blue;\n"
"                border: 2px solid #dee2e6;\n"
"                border-radius: 8px;\n"
"                selection-background-color: #007bff;\n"
"            }\n"
"\n"
"            QTableWidget::item {\n"
"                color: #green;\n"
"                border-bottom: 1px solid #dee2e6;\n"
"            }\n"
"\n"
"            QTableWidget::item:selected {\n"
"                background-color: #red;\n"
"                color: #ffffff;\n"
"            }\n"
"\n"
"            QTableWidget::item:hover {\n"
"                background-color: #orange;\n"
"            }\n"
"\n"
"            QHeaderView::section {\n"
"                background-color: #343a40;\n"
"                color: #ffffff;\n"
"                border: 1px solid #343a40;\n"
"                border-radius: 4px;\n"
"                padding: 8px;\n"
"            }\n"
"\n"
"            QHeaderView::section:hover {\n"
"                background-color: #495057;\n"
"            }")
        self.tableWidget_3.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(False)
        self.label_9 = QLabel(self.widget_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(390, 20, 122, 17))
        self.comboBox_8 = QComboBox(self.widget_6)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setGeometry(QRect(600, 50, 221, 25))
        self.comboBox_7 = QComboBox(self.widget_6)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setGeometry(QRect(200, 10, 121, 31))
        self.comboBox_7.setStyleSheet(u"background: #E0E0E0;\n"
"")
        self.comboBox_9 = QComboBox(self.widget_6)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setGeometry(QRect(390, 50, 195, 25))
        self.textEdit_3 = QTextEdit(self.widget_6)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(10, 50, 311, 31))
        self.textEdit_3.setStyleSheet(u"border: 1px solid black;\n"
"border-radius: 15px;")
        self.label_10 = QLabel(self.widget_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 60, 15, 15))
        self.label_10.setMaximumSize(QSize(15, 15))
        self.label_10.setPixmap(QPixmap(u":/icon/search.png"))
        self.label_10.setScaledContents(True)
        self.widget_7 = QWidget(self.widget_list_nurse)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(840, 30, 131, 91))
        self.widget_7.setStyleSheet(u"border: 1px solid black;\n"
"border-radius: 20px")
        self.label_4 = QLabel(self.widget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 30, 131, 31))
        self.label_4.setStyleSheet(u"border: None;\n"
"font: 700 13pt \"Arial\";")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.widget_list_patient = QWidget(self.page_6)
        self.widget_list_patient.setObjectName(u"widget_list_patient")
        self.widget_list_patient.setGeometry(QRect(-10, -10, 1061, 721))
        self.tableWidget_4 = QTableWidget(self.widget_list_patient)
        if (self.tableWidget_4.columnCount() < 7):
            self.tableWidget_4.setColumnCount(7)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, __qtablewidgetitem32)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setGeometry(QRect(100, 170, 871, 521))
        self.tableWidget_4.setStyleSheet(u"            QTableWidget {\n"
"                background-color: #f8f9fa;\n"
"                border: 2px solid #dee2e6;\n"
"                border-radius: 8px;\n"
"                selection-background-color: #007bff;\n"
"            }\n"
"\n"
"            QTableWidget::item {\n"
"                color: #495057;\n"
"                border-bottom: 1px solid #dee2e6;\n"
"            }\n"
"\n"
"            QTableWidget::item:selected {\n"
"                background-color: #007bff;\n"
"                color: #ffffff;\n"
"            }\n"
"\n"
"            QTableWidget::item:hover {\n"
"                background-color: #e0e0e0;\n"
"            }\n"
"\n"
"            QHeaderView::section {\n"
"                background-color: #343a40;\n"
"                color: #ffffff;\n"
"                border: 1px solid #343a40;\n"
"                border-radius: 4px;\n"
"                padding: 8px;\n"
"            }\n"
"\n"
"            QHeaderView::section:hover {\n"
"                background-color: #495057;\n"
"       "
                        "     }")
        self.label_11 = QLabel(self.widget_list_patient)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(680, 80, 181, 31))
        self.widget_8 = QWidget(self.widget_list_patient)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(110, 30, 411, 121))
        self.gridLayout_6 = QGridLayout(self.widget_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_12 = QLabel(self.widget_8)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_6.addWidget(self.label_12, 2, 0, 1, 1)

        self.label_13 = QLabel(self.widget_8)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 1)

        self.comboBox_10 = QComboBox(self.widget_8)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")

        self.gridLayout_6.addWidget(self.comboBox_10, 0, 1, 1, 1)

        self.comboBox_11 = QComboBox(self.widget_8)
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")

        self.gridLayout_6.addWidget(self.comboBox_11, 2, 2, 1, 1)

        self.textEdit_4 = QTextEdit(self.widget_8)
        self.textEdit_4.setObjectName(u"textEdit_4")

        self.gridLayout_6.addWidget(self.textEdit_4, 1, 0, 1, 3)

        self.comboBox_12 = QComboBox(self.widget_8)
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.setObjectName(u"comboBox_12")

        self.gridLayout_6.addWidget(self.comboBox_12, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_6)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 233, 740))
        self.widget.setStyleSheet(u"background-color: #CFC071;\n"
"\n"
"")
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(12, 12, 209, 81))
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(57, 54, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(40, 40))
        self.label_3.setPixmap(QPixmap(u":/icon/image/medical-symbol (1).png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_3)

        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/icon/medical-symbol (1).png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(56, 54, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.layoutWidget = QWidget(self.widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 90, 241, 633))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	padding: 10%;\n"
"	border: none;\n"
"	padding-left: 50%;\n"
"	text-align:left;\n"
"	font-size: 16px;\n"
"	font: 16pt \"Cambria\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 10%;\n"
"	padding-left: 45%;\n"
"	text-align:left;\n"
"	background: #A5995B;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icon/image/account2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	padding: 10%;\n"
"	border: none;\n"
"	padding-left: 50%;\n"
"	text-align:left;\n"
"	font-size: 16px;\n"
"	font: 16pt \"Cambria\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 10%;\n"
"	padding-left: 45%;\n"
"	text-align:left;\n"
"	background: #A5995B;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/image/appointment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_9 = QPushButton(self.layoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	padding: 10%;\n"
"	border: none;\n"
"	padding-left: 50%;\n"
"	text-align:left;\n"
"	font-size: 16px;\n"
"	font: 16pt \"Cambria\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 10%;\n"
"	padding-left: 45%;\n"
"	text-align:left;\n"
"	background: #A5995B;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icon/image/bill.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton_9)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	padding: 10%;\n"
"	border: none;\n"
"	padding-left: 50%;\n"
"	text-align:left;\n"
"	font-size: 16px;\n"
"	font: 16pt \"Cambria\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 10%;\n"
"	padding-left: 45%;\n"
"	text-align:left;\n"
"	background: #A5995B;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icon/image/history2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_10 = QPushButton(self.layoutWidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	padding: 10%;\n"
"	border: none;\n"
"	padding-left: 50%;\n"
"	text-align:left;\n"
"	font-size: 16px;\n"
"	font: 16pt \"Cambria\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 10%;\n"
"	padding-left: 45%;\n"
"	text-align:left;\n"
"	background: #A5995B;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icon/image/id-card.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon4)
        self.pushButton_10.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton_10)

        self.pushButton_5 = QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	padding: 10%;\n"
"	border: none;\n"
"	padding-left: 75%;\n"
"	text-align:left;\n"
"	font-size: 16px;\n"
"	font: 16pt \"Cambria\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 10%;\n"
"	padding-left: 70%;\n"
"	text-align:left;\n"
"	background: #A5995B;\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icon/image/doctor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	padding: 10%;\n"
"	border: none;\n"
"	padding-left: 75%;\n"
"	text-align:left;\n"
"	font-size: 16px;\n"
"	font: 16pt \"Cambria\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 10%;\n"
"	padding-left: 70%;\n"
"	text-align:left;\n"
"	background: #A5995B;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/icon/image/nurse.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	padding: 10%;\n"
"	border: none;\n"
"	padding-left: 75%;\n"
"	text-align:left;\n"
"	font-size: 16px;\n"
"	font: 16pt \"Cambria\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 10%;\n"
"	padding-left: 70%;\n"
"	text-align:left;\n"
"	background: #A5995B;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icon/image/hospitalisation.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon7)
        self.pushButton_7.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	padding: 10%;\n"
"	border: none;\n"
"	padding-left: 50%;\n"
"	text-align:left;\n"
"	font-size: 16px;\n"
"	font: 16pt \"Cambria\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 10%;\n"
"	padding-left: 45%;\n"
"	text-align:left;\n"
"	background: #A5995B;\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/icon/image/add-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon8)
        self.pushButton_8.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushButton_8)

        self.verticalSpacer = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	padding: 10%;\n"
"	border: none;\n"
"	padding-left: 50%;\n"
"	text-align:left;\n"
"	font-size: 16px;\n"
"	font: 16pt \"Cambria\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 10%;\n"
"	padding-left: 45%;\n"
"	text-align:left;\n"
"	background: #A5995B;\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icon/image/logout (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon9)
        self.pushButton_4.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.profile_label.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.profile_label_2.setText(QCoreApplication.translate("MainWindow", u"Last name:", None))
        self.profile_label_3.setText(QCoreApplication.translate("MainWindow", u"Role:", None))
        self.profile_label_4.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.profile_label_5.setText(QCoreApplication.translate("MainWindow", u"Phone number:", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Department", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Degree", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Salary", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Working Time", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Action", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Edit", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Total Doctors : ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sort by", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Search by ", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"employee_id", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"fname", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"lname", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"address", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"phone_number", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"department", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"qualifications", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"salary", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"working_time", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Ascending", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Descending", None))

        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Osaka'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"employee_id", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"fname", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"lname", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"address", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"phone_number", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"department", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"qualifications", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"salary", None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"working_time", None))

        self.appointment_page.setText(QCoreApplication.translate("MainWindow", u"Appointment", None))
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Time Stamp", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Actor", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Action", None));
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Target", None));
        self.textEdit_logs.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Time Stamp", None))
        self.textEdit_logs_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Actor", None))
        self.textEdit_logs_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Action", None))
        self.textEdit_logs_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Target", None))
        ___qtablewidgetitem15 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem16 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem17 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem18 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem19 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None));
        ___qtablewidgetitem20 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Department", None));
        ___qtablewidgetitem21 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Degree", None));
        ___qtablewidgetitem22 = self.tableWidget_3.horizontalHeaderItem(7)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Salary", None));
        ___qtablewidgetitem23 = self.tableWidget_3.horizontalHeaderItem(8)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Working Time", None));
        ___qtablewidgetitem24 = self.tableWidget_3.horizontalHeaderItem(9)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Action", None));
        ___qtablewidgetitem25 = self.tableWidget_3.horizontalHeaderItem(10)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Edit", None));
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Sort by", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"Ascending", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"Descending", None))

        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"employee_id", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"fname", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("MainWindow", u"lname", None))
        self.comboBox_7.setItemText(3, QCoreApplication.translate("MainWindow", u"address", None))
        self.comboBox_7.setItemText(4, QCoreApplication.translate("MainWindow", u"phone_number", None))
        self.comboBox_7.setItemText(5, QCoreApplication.translate("MainWindow", u"department", None))
        self.comboBox_7.setItemText(6, QCoreApplication.translate("MainWindow", u"qualifications", None))
        self.comboBox_7.setItemText(7, QCoreApplication.translate("MainWindow", u"salary", None))
        self.comboBox_7.setItemText(8, QCoreApplication.translate("MainWindow", u"working_time", None))

        self.comboBox_9.setItemText(0, QCoreApplication.translate("MainWindow", u"employee_id", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("MainWindow", u"fname", None))
        self.comboBox_9.setItemText(2, QCoreApplication.translate("MainWindow", u"lname", None))
        self.comboBox_9.setItemText(3, QCoreApplication.translate("MainWindow", u"address", None))
        self.comboBox_9.setItemText(4, QCoreApplication.translate("MainWindow", u"phone_number", None))
        self.comboBox_9.setItemText(5, QCoreApplication.translate("MainWindow", u"department", None))
        self.comboBox_9.setItemText(6, QCoreApplication.translate("MainWindow", u"qualifications", None))
        self.comboBox_9.setItemText(7, QCoreApplication.translate("MainWindow", u"salary", None))
        self.comboBox_9.setItemText(8, QCoreApplication.translate("MainWindow", u"working_time", None))

        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Osaka';\"><br /></p></body></html>", None))
        self.label_10.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Total Nurse : ", None))
        ___qtablewidgetitem26 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem27 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem28 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem29 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem30 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None));
        ___qtablewidgetitem31 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Action", None));
        ___qtablewidgetitem32 = self.tableWidget_4.horizontalHeaderItem(6)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Edit", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Total Patient : ", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Sort by", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Search by ", None))
        self.comboBox_10.setItemText(0, QCoreApplication.translate("MainWindow", u"patient_id", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("MainWindow", u"fname", None))
        self.comboBox_10.setItemText(2, QCoreApplication.translate("MainWindow", u"lname", None))
        self.comboBox_10.setItemText(3, QCoreApplication.translate("MainWindow", u"address", None))
        self.comboBox_10.setItemText(4, QCoreApplication.translate("MainWindow", u"phone_number", None))

        self.comboBox_11.setItemText(0, QCoreApplication.translate("MainWindow", u"Ascending", None))
        self.comboBox_11.setItemText(1, QCoreApplication.translate("MainWindow", u"Descending", None))

        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Osaka'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.comboBox_12.setItemText(0, QCoreApplication.translate("MainWindow", u"patient_id", None))
        self.comboBox_12.setItemText(1, QCoreApplication.translate("MainWindow", u"fname", None))
        self.comboBox_12.setItemText(2, QCoreApplication.translate("MainWindow", u"lname", None))
        self.comboBox_12.setItemText(3, QCoreApplication.translate("MainWindow", u"address", None))
        self.comboBox_12.setItemText(4, QCoreApplication.translate("MainWindow", u"phone_number", None))

        self.label_3.setText("")
        self.label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Appointment", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Payment", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Staff List", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Doctor", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Nurse", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Patient ", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Add User", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi

