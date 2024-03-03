# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowDoctor.ui'
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
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
from . import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1286, 720)
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
        self.widget_5.setGeometry(QRect(-30, -10, 1051, 721))
        self.widget_5.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(420, 300, 141, 101))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.widget_8 = QWidget(self.page_3)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(-10, -10, 1051, 721))
        self.textEdit = QTextEdit(self.widget_8)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(570, 80, 301, 41))
        self.tableWidget = QTableWidget(self.widget_8)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(120, 170, 761, 431))
        self.tableWidget.setStyleSheet(u"border: none;")
        self.tableWidget.setShowGrid(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.widget_7 = QWidget(self.page_4)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(0, -20, 1051, 721))
        self.widget_9 = QWidget(self.widget_7)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(20, 20, 551, 691))
        self.gridLayout_3 = QGridLayout(self.widget_9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_6 = QLineEdit(self.widget_9)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_3.addWidget(self.lineEdit_6, 7, 3, 1, 1)

        self.label_13 = QLabel(self.widget_9)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 10, 0, 1, 1)

        self.label_11 = QLabel(self.widget_9)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 9, 0, 1, 1)

        self.textEdit_2 = QTextEdit(self.widget_9)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.gridLayout_3.addWidget(self.textEdit_2, 18, 2, 1, 2)

        self.label_10 = QLabel(self.widget_9)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 6, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.widget_9)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_3.addWidget(self.lineEdit_5, 6, 3, 1, 1)

        self.label_14 = QLabel(self.widget_9)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 7, 0, 1, 1)

        self.label_12 = QLabel(self.widget_9)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 18, 0, 1, 1)

        self.comboBox = QComboBox(self.widget_9)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_3.addWidget(self.comboBox, 0, 3, 1, 1)

        self.label_15 = QLabel(self.widget_9)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_3.addWidget(self.label_15, 4, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.widget_9)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_3.addWidget(self.lineEdit_3, 4, 3, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget_9)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_3.addWidget(self.lineEdit_2, 3, 1, 1, 3)

        self.lineEdit_7 = QLineEdit(self.widget_9)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_3.addWidget(self.lineEdit_7, 9, 3, 1, 1)

        self.label_7 = QLabel(self.widget_9)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.widget_9)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit, 2, 1, 1, 3)

        self.label_3 = QLabel(self.widget_9)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 3)

        self.lineEdit_8 = QLineEdit(self.widget_9)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_3.addWidget(self.lineEdit_8, 10, 3, 1, 1)

        self.lineEdit_4 = QLineEdit(self.widget_9)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_3.addWidget(self.lineEdit_4, 5, 3, 1, 1)

        self.label_8 = QLabel(self.widget_9)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_9 = QLabel(self.widget_9)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 5, 0, 1, 1)

        self.widget_10 = QWidget(self.widget_7)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(590, 70, 431, 221))
        self.verticalLayout_3 = QVBoxLayout(self.widget_10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_17 = QLabel(self.widget_10)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_3.addWidget(self.label_17)

        self.label_18 = QLabel(self.widget_10)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_3.addWidget(self.label_18)

        self.label_19 = QLabel(self.widget_10)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_3.addWidget(self.label_19)

        self.label_20 = QLabel(self.widget_10)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_3.addWidget(self.label_20)

        self.label_21 = QLabel(self.widget_10)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_3.addWidget(self.label_21)

        self.pushButton_5 = QPushButton(self.widget_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(800, 660, 131, 51))
        self.pushButton_6 = QPushButton(self.widget_7)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(590, 320, 121, 51))
        self.pushButton_7 = QPushButton(self.widget_7)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(600, 480, 111, 51))
        self.label_6 = QLabel(self.widget_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(590, 40, 131, 16))
        self.label_16 = QLabel(self.widget_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(720, 40, 131, 16))
        self.listWidget = QListWidget(self.widget_7)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(740, 320, 261, 131))
        self.listWidget_2 = QListWidget(self.widget_7)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(740, 480, 261, 141))
        self.pushButton_8 = QPushButton(self.widget_7)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(740, 450, 261, 21))
        self.pushButton_10 = QPushButton(self.widget_7)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(740, 622, 261, 20))
        self.lineEdit_9 = QLineEdit(self.widget_7)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(590, 660, 181, 31))
        self.stackedWidget.addWidget(self.page_4)

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

        self.stackedWidget.setCurrentIndex(2)


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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"appointment", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Patient ID", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Patient Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Problem Description", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Problem Title", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"BP", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Allegies", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Sex", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Patient Name:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Weight", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Pulse rate", None))
        self.label_17.setText("")
        self.label_18.setText("")
        self.label_19.setText("")
        self.label_20.setText("")
        self.label_21.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Medicine", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Billing", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"From Doctor :", None))
        self.label_16.setText("")
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"View Medicine Data", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"View Billing Data", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Overall Discount %", None))
        self.label_4.setText("")
        self.label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Appointment", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Medical History", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Write Report", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi

