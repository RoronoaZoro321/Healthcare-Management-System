# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QComboBox,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
from.import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1251, 720)
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
        self.profile_widget.setGeometry(QRect(50, 90, 901, 501))
        font = QFont()
        font.setFamilies([u"Osaka"])
        font.setBold(False)
        font.setItalic(False)
        self.profile_widget.setFont(font)
        self.profile_widget.setStyleSheet(u"QWidget {\n"
"	border: 1px solid #353535;\n"
"	font: 18px;\n"
"	padding: 20px;\n"
"}\n"
"")
        self.verticalLayout_7 = QVBoxLayout(self.profile_widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_6 = QWidget(self.profile_widget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"border: None;")
        self.label_5 = QLabel(self.widget_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(360, 0, 211, 101))
        self.label_5.setStyleSheet(u"font: 28px;\n"
"")

        self.verticalLayout_7.addWidget(self.widget_6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.profile_label = QLabel(self.profile_widget)
        self.profile_label.setObjectName(u"profile_label")
        self.profile_label.setStyleSheet(u"border-style: none;\n"
"font-size: 16px;\n"
"margin-left: 90%;")

        self.verticalLayout.addWidget(self.profile_label)

        self.profile_label_2 = QLabel(self.profile_widget)
        self.profile_label_2.setObjectName(u"profile_label_2")
        self.profile_label_2.setStyleSheet(u"border-style: none;\n"
"font-size: 16px;\n"
"margin-left: 90%;")

        self.verticalLayout.addWidget(self.profile_label_2)

        self.profile_label_3 = QLabel(self.profile_widget)
        self.profile_label_3.setObjectName(u"profile_label_3")
        self.profile_label_3.setStyleSheet(u"border-style: none;\n"
"font-size: 16px;\n"
"margin-left: 90%;\n"
"")

        self.verticalLayout.addWidget(self.profile_label_3)

        self.profile_label_4 = QLabel(self.profile_widget)
        self.profile_label_4.setObjectName(u"profile_label_4")
        self.profile_label_4.setStyleSheet(u"border-style: none;\n"
"font-size: 16px;\n"
"margin-left: 90%;")

        self.verticalLayout.addWidget(self.profile_label_4)

        self.profile_label_5 = QLabel(self.profile_widget)
        self.profile_label_5.setObjectName(u"profile_label_5")
        self.profile_label_5.setStyleSheet(u"border-style: none;\n"
"font-size: 16px;\n"
"margin-left: 90%;\n"
"margin-bottom: 30%;")

        self.verticalLayout.addWidget(self.profile_label_5)


        self.verticalLayout_7.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.widget_5 = QWidget(self.page_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(-30, -10, 1041, 721))
        self.widget_5.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.Calendar = QCalendarWidget(self.widget_5)
        self.Calendar.setObjectName(u"Calendar")
        self.Calendar.setGeometry(QRect(110, 410, 481, 181))
        self.Calendar.setStyleSheet(u"border: 1px solid black;\n"
"font: 8pt \"Cambria\";\n"
"\n"
"")
        self.Calendar.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.Submit = QPushButton(self.widget_5)
        self.Submit.setObjectName(u"Submit")
        self.Submit.setGeometry(QRect(870, 550, 75, 24))
        self.Submit.setStyleSheet(u"font: 8pt \"Cambria\";\n"
"")
        self.layoutWidget = QWidget(self.widget_5)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(660, 440, 279, 99))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"font: 10pt \"Cambria\";\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setStyleSheet(u"font: 10pt \"Cambria\";\n"
"")

        self.verticalLayout_3.addWidget(self.checkBox_2)

        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(450, 40, 521, 271))
        self.widget_8.setStyleSheet(u"border: 1px solid black;\n"
"background: #F8FAFC;")
        self.tableWidget = QTableWidget(self.widget_8)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 90, 501, 171))
        self.tableWidget.setStyleSheet(u"font: 12pt \"Cambria\";\n"
"border: None;")
        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(0, 40, 521, 51))
        self.widget_9.setStyleSheet(u"background: #ACACAC;")
        self.label_7 = QLabel(self.widget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(210, 10, 191, 31))
        self.label_7.setStyleSheet(u"font: 14pt \"Cambria\";\n"
"color: black;\n"
"border: None;")
        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(110, 370, 321, 41))
        self.label_6.setStyleSheet(u"font: 12pt \"Cambria\";")
        self.layoutWidget_1 = QWidget(self.widget_5)
        self.layoutWidget_1.setObjectName(u"layoutWidget_1")
        self.layoutWidget_1.setGeometry(QRect(110, 120, 302, 141))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 12pt \"Cambria\";\n"
"")

        self.verticalLayout_4.addWidget(self.label_2)

        self.Speciality = QComboBox(self.layoutWidget_1)
        self.Speciality.addItem("")
        self.Speciality.addItem("")
        self.Speciality.addItem("")
        self.Speciality.addItem("")
        self.Speciality.addItem("")
        self.Speciality.setObjectName(u"Speciality")
        self.Speciality.setStyleSheet(u"background: #ACACAC;\n"
"font: 12pt \"Cambria\";\n"
"color: white;")
        self.Speciality.setEditable(False)

        self.verticalLayout_4.addWidget(self.Speciality)

        self.verticalSpacer_2 = QSpacerItem(296, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.label_3 = QLabel(self.layoutWidget_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 12pt \"Cambria\";")

        self.verticalLayout_4.addWidget(self.label_3)

        self.Doctor = QComboBox(self.layoutWidget_1)
        self.Doctor.setObjectName(u"Doctor")
        self.Doctor.setStyleSheet(u"font: 12pt \"Cambria\";\n"
"background: #ACACAC;\n"
"color: white;")

        self.verticalLayout_4.addWidget(self.Doctor)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.history_page = QLabel(self.page_3)
        self.history_page.setObjectName(u"history_page")
        self.history_page.setGeometry(QRect(0, 60, 1011, 611))
        self.history_page.setStyleSheet(u"color: black;")
        self.history_page.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 231, 721))
        self.widget.setStyleSheet(u"background-color: #02A499;\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(64, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u":/icon/medical-symbol (1).png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)

        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/icon/image/medical-symbol (1).png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font1 = QFont()
        font1.setFamilies([u"Cambria"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	padding: 17%;\n"
"	padding-left: 40%;\n"
"	border: none;\n"
"	text-align:left;\n"
"	font-size: 18px;\n"
"	font: 16pt \"Cambria\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 17%;\n"
"	padding-left: 35%;\n"
"	text-align:left;\n"
"	background: #00847B;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/image/account2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	padding: 17%;\n"
"	border: none;\n"
"	padding-left: 40%;\n"
"	text-align:left;\n"
"	font-size: 18px;\n"
"	font: 16pt \"Cambria\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 17%;\n"
"	padding-left: 35%;\n"
"	text-align:left;\n"
"	background: #00847B;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/image/appointment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	padding: 17%;\n"
"	border: none;\n"
"	padding-left: 40%;\n"
"	text-align:left;\n"
"	font-size: 18px;\n"
"	font: 16pt \"Cambria\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 17%;\n"
"	padding-left: 35%;\n"
"	text-align:left;\n"
"	background: #00847B;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icon/image/history2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_9 = QPushButton(self.widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	padding: 17%;\n"
"	border: none;\n"
"	padding-left: 40%;\n"
"	text-align:left;\n"
"	font-size: 18px;\n"
"	font: 16pt \"Cambria\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 17%;\n"
"	padding-left: 35%;\n"
"	text-align:left;\n"
"	background: #00847B;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icon/image/bill.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon3)
        self.pushButton_9.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton_9)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	padding: 17%;\n"
"	border: none;\n"
"	padding-left: 40%;\n"
"	text-align:left;\n"
"	font-size: 18px;\n"
"	font: 16pt \"Cambria\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	padding: 17%;\n"
"	padding-left: 35%;\n"
"	text-align:left;\n"
"	background: #00847B;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icon/image/logout (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.pushButton_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PROFILE", None))
        self.profile_label.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.profile_label_2.setText(QCoreApplication.translate("MainWindow", u"Last name:", None))
        self.profile_label_3.setText(QCoreApplication.translate("MainWindow", u"Role:", None))
        self.profile_label_4.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.profile_label_5.setText(QCoreApplication.translate("MainWindow", u"Phone number:", None))
        self.Submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"6:00 am.- 12:00 pm.", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"13:00 pm.- 18:00 pm.", None))
        ___qtablewidgetitem = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Appointment", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"My Appointment", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Appointment Date", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Speciality", None))
        self.Speciality.setItemText(0, QCoreApplication.translate("MainWindow", u"Dentist", None))
        self.Speciality.setItemText(1, QCoreApplication.translate("MainWindow", u"Cardiology", None))
        self.Speciality.setItemText(2, QCoreApplication.translate("MainWindow", u"Pediatrics", None))
        self.Speciality.setItemText(3, QCoreApplication.translate("MainWindow", u"Surgery", None))
        self.Speciality.setItemText(4, QCoreApplication.translate("MainWindow", u"Obsterics and Gynaecology", None))

        self.Speciality.setCurrentText(QCoreApplication.translate("MainWindow", u"Dentist", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Doctor", None))
        self.history_page.setText(QCoreApplication.translate("MainWindow", u"Medical History", None))
        self.label_4.setText("")
        self.label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Appointment", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Medical History", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Payment", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi

