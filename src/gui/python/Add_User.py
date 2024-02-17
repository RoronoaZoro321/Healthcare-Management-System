# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Add_User.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(491, 675)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 491, 671))
        self.widget.setStyleSheet(u"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(2, 164, 153);\n"
"background-color: rgb(248, 250, 252);")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
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

        self.lineEdit_3 = QLineEdit(self.widget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(211, 237, 237);\n"
"	border: 2px solid #353535;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #02A499;\n"
"}")

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.widget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(211, 237, 237);\n"
"	border: 2px solid #353535;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #02A499;\n"
"}")

        self.verticalLayout.addWidget(self.lineEdit_4)

        self.comboBox = QComboBox(self.widget_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.lineEdit_5 = QLineEdit(self.widget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(211, 237, 237);\n"
"	border: 2px solid #353535;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #02A499;\n"
"}")

        self.verticalLayout.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.widget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(211, 237, 237);\n"
"	border: 2px solid #353535;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #02A499;\n"
"}")

        self.verticalLayout.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.widget_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(211, 237, 237);\n"
"	border: 2px solid #353535;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #02A499;\n"
"}")

        self.verticalLayout.addWidget(self.lineEdit_7)

        self.lineEdit_8 = QLineEdit(self.widget_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(211, 237, 237);\n"
"	border: 2px solid #353535;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #02A499;\n"
"}")

        self.verticalLayout.addWidget(self.lineEdit_8)

        self.lineEdit_9 = QLineEdit(self.widget_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(211, 237, 237);\n"
"	border: 2px solid #353535;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #02A499;\n"
"}")

        self.verticalLayout.addWidget(self.lineEdit_9)


        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)

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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

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


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"First Name", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Last Name", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"Address", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"Phone Number", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Patient", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Doctor", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Nurse", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"Admin", None))

        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Form", u"Department", None))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("Form", u"Specialty", None))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("Form", u"Qualifications", None))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("Form", u"Salary", None))
        self.label.setText(QCoreApplication.translate("Form", u"Add User", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Done", None))
    # retranslateUi

