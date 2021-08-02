# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_register.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Register(object):
    def setupUi(self, Register):
        if not Register.objectName():
            Register.setObjectName(u"Register")
        Register.resize(444, 492)
        Register.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 16px \"Open Sans\";\n"
"}\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 16px \"Open Sans\";\n"
"}\n"
"QPushButton#pushButton_register{\n"
"	border-radius:10px;\n"
"	background-color: rgb(0, 102, 212);\n"
"}\n"
"QPushButton#pushButton_register:hover{\n"
"	background-color: rgb(0, 88, 212);\n"
"}\n"
"QPushButton#pushButton_register:pressed{\n"
"	background-color: rgb(0, 73, 212);\n"
"}\n"
"QPushButton#pushButton_back{\n"
"	border:none;\n"
"	background-color: rgb(46, 52, 54);\n"
"}\n"
"QPushButton#pushButton_back:pressed{\n"
"	border:none;\n"
"	background-color: rgb(42, 48, 50);\n"
"}\n"
"QWidget#frame_login_up{\n"
"	background-color: #0066D4;\n"
"}\n"
"QWidget#frame_login_down{\n"
"	background-color: #003E7F;\n"
"}\n"
"QWidget#frame_login_left{\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 		#0066D4, stop:1 #003E7F);\n"
"}\n"
"QWidget#frame_login_right{\n"
"	background-color: qlineargradient(spread:pad, x1:0."
                        "5, y1:0, x2:0.5, y2:1, stop:0 		#0066D4, stop:1 #003E7F);\n"
"}\n"
"QWidget#frame_login_main{\n"
"background-color: rgb(85, 87, 83);\n"
"	background-color: rgb(46, 52, 54);\n"
"}\n"
"QLabel#label_main{\n"
"	font: 24pt \"Open Sans\";\n"
"}\n"
"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border:none;\n"
"	border-bottom:1px solid white;\n"
"	background-color: rgb(46, 52, 54);\n"
"}\n"
"QLabel#label_info{\n"
"		font: 13px \"Open Sans\";\n"
"}")
        self.verticalLayout = QVBoxLayout(Register)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_login_up = QFrame(Register)
        self.frame_login_up.setObjectName(u"frame_login_up")
        self.frame_login_up.setFrameShape(QFrame.NoFrame)
        self.frame_login_up.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_login_up)

        self.frame_login_center = QFrame(Register)
        self.frame_login_center.setObjectName(u"frame_login_center")
        self.frame_login_center.setFrameShape(QFrame.NoFrame)
        self.frame_login_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_login_center)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_login_left = QFrame(self.frame_login_center)
        self.frame_login_left.setObjectName(u"frame_login_left")
        self.frame_login_left.setStyleSheet(u"")
        self.frame_login_left.setFrameShape(QFrame.NoFrame)
        self.frame_login_left.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_login_left)

        self.frame_login_main = QFrame(self.frame_login_center)
        self.frame_login_main.setObjectName(u"frame_login_main")
        self.frame_login_main.setMinimumSize(QSize(250, 200))
        self.frame_login_main.setMaximumSize(QSize(250, 16777215))
        self.frame_login_main.setFrameShape(QFrame.NoFrame)
        self.frame_login_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_login_main)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_label = QFrame(self.frame_login_main)
        self.frame_label.setObjectName(u"frame_label")
        self.frame_label.setFrameShape(QFrame.NoFrame)
        self.frame_label.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_label)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_label)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(40, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_back = QPushButton(self.frame)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setMinimumSize(QSize(0, 40))

        self.verticalLayout_5.addWidget(self.pushButton_back)


        self.horizontalLayout_5.addWidget(self.frame)

        self.label_main = QLabel(self.frame_label)
        self.label_main.setObjectName(u"label_main")
        self.label_main.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_main)


        self.verticalLayout_2.addWidget(self.frame_label)

        self.frame_user = QFrame(self.frame_login_main)
        self.frame_user.setObjectName(u"frame_user")
        self.frame_user.setFrameShape(QFrame.NoFrame)
        self.frame_user.setFrameShadow(QFrame.Raised)
        self.frame_user.setLineWidth(1)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_user)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_usr_info = QFrame(self.frame_user)
        self.frame_usr_info.setObjectName(u"frame_usr_info")
        self.frame_usr_info.setFrameShape(QFrame.NoFrame)
        self.frame_usr_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_usr_info)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_user = QLabel(self.frame_usr_info)
        self.label_user.setObjectName(u"label_user")
        self.label_user.setFrameShape(QFrame.NoFrame)
        self.label_user.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_user, 0, Qt.AlignHCenter)

        self.label_pass = QLabel(self.frame_usr_info)
        self.label_pass.setObjectName(u"label_pass")
        self.label_pass.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_pass, 0, Qt.AlignHCenter)

        self.label = QLabel(self.frame_usr_info)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.frame_usr_info)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.frame_usr_info)

        self.frame_5 = QFrame(self.frame_user)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(150, 16777215))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.lineEdit_user = QLineEdit(self.frame_5)
        self.lineEdit_user.setObjectName(u"lineEdit_user")
        self.lineEdit_user.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_4.addWidget(self.lineEdit_user)

        self.lineEdit_pass = QLineEdit(self.frame_5)
        self.lineEdit_pass.setObjectName(u"lineEdit_pass")
        self.lineEdit_pass.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_4.addWidget(self.lineEdit_pass)

        self.lineEdit_confirm = QLineEdit(self.frame_5)
        self.lineEdit_confirm.setObjectName(u"lineEdit_confirm")

        self.verticalLayout_4.addWidget(self.lineEdit_confirm)

        self.lineEdit_email = QLineEdit(self.frame_5)
        self.lineEdit_email.setObjectName(u"lineEdit_email")

        self.verticalLayout_4.addWidget(self.lineEdit_email)


        self.horizontalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_user)

        self.frame_info = QFrame(self.frame_login_main)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setMaximumSize(QSize(16777215, 25))
        self.frame_info.setFrameShape(QFrame.NoFrame)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_info)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_info = QLabel(self.frame_info)
        self.label_info.setObjectName(u"label_info")

        self.horizontalLayout_4.addWidget(self.label_info, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_info)

        self.frame_btn = QFrame(self.frame_login_main)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setMaximumSize(QSize(16777215, 40))
        self.frame_btn.setFrameShape(QFrame.NoFrame)
        self.frame_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_btn)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.pushButton_register = QPushButton(self.frame_btn)
        self.pushButton_register.setObjectName(u"pushButton_register")

        self.horizontalLayout_2.addWidget(self.pushButton_register)


        self.verticalLayout_2.addWidget(self.frame_btn)


        self.horizontalLayout.addWidget(self.frame_login_main)

        self.frame_login_right = QFrame(self.frame_login_center)
        self.frame_login_right.setObjectName(u"frame_login_right")
        self.frame_login_right.setFrameShape(QFrame.NoFrame)
        self.frame_login_right.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_login_right)


        self.verticalLayout.addWidget(self.frame_login_center)

        self.frame_login_down = QFrame(Register)
        self.frame_login_down.setObjectName(u"frame_login_down")
        self.frame_login_down.setFrameShape(QFrame.NoFrame)
        self.frame_login_down.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_login_down)


        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"todoApp", None))
        self.pushButton_back.setText(QCoreApplication.translate("Register", u"<", None))
        self.label_main.setText(QCoreApplication.translate("Register", u"Register", None))
        self.label_user.setText(QCoreApplication.translate("Register", u"Username", None))
        self.label_pass.setText(QCoreApplication.translate("Register", u"Password", None))
        self.label.setText(QCoreApplication.translate("Register", u"Password", None))
        self.label_2.setText(QCoreApplication.translate("Register", u"Email", None))
        self.lineEdit_user.setPlaceholderText(QCoreApplication.translate("Register", u"Username", None))
        self.lineEdit_pass.setPlaceholderText(QCoreApplication.translate("Register", u"Password", None))
        self.lineEdit_confirm.setPlaceholderText(QCoreApplication.translate("Register", u"Confirm password", None))
        self.lineEdit_email.setPlaceholderText(QCoreApplication.translate("Register", u"Email", None))
        self.label_info.setText("")
        self.pushButton_register.setText(QCoreApplication.translate("Register", u"Register", None))
    # retranslateUi

