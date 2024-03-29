# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(491, 361)
        Form.setStyleSheet(u"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(2, 164, 153);\n"
"background-color: rgb(248, 250, 252);")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 491, 361))
        self.widget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	color: #353535;\n"
"	padding: 10px;\n"
"	border-radius: none;\n"
"	font-size: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(2, 131, 107);\n"
"	color: white;\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.pushButton_2, 5, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font-size: 30px;\n"
"margin: 30px;\n"
"color:  #353535;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(2, 164, 153);\n"
"	color: #F8FAFC;\n"
"	margin: 10px 160px;\n"
"	padding: 10px;\n"
"	border-radius: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(2, 131, 107);\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"padding: 7px;")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(211, 237, 237);\n"
"	border: 2px solid #353535;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #02A499;\n"
"}")

        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.widget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(211, 237, 237);\n"
"	border: 2px solid #353535;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #02A499;\n"
"}")

        self.verticalLayout.addWidget(self.lineEdit_2)


        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"SignUp", None))
        self.label.setText(QCoreApplication.translate("Form", u"Login", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Done", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"First Name", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
    # retranslateUi

