# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow2.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
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
        self.history_page = QLabel(self.page_3)
        self.history_page.setObjectName(u"history_page")
        self.history_page.setGeometry(QRect(0, 60, 1011, 611))
        self.history_page.setStyleSheet(u"color: black;")
        self.history_page.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)

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

        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/icon/image/hospital.png"))
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
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(203, 203, 203);\n"
"	margin: 20px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: white;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/image/account.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(203, 203, 203);\n"
"	margin: 20px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/image/schedule.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(203, 203, 203);\n"
"	margin: 20px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: white;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/image/history.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(203, 203, 203);\n"
"	margin: 20px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: white;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/image/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.pushButton_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.profile_label.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.profile_label_2.setText(QCoreApplication.translate("MainWindow", u"Last name:", None))
        self.profile_label_3.setText(QCoreApplication.translate("MainWindow", u"Role:", None))
        self.profile_label_4.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.profile_label_5.setText(QCoreApplication.translate("MainWindow", u"Phone number:", None))
        self.appointment_page.setText(QCoreApplication.translate("MainWindow", u"Appointment", None))
        self.history_page.setText(QCoreApplication.translate("MainWindow", u"Medical History", None))
        self.label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Appointment", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Medical History", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi
