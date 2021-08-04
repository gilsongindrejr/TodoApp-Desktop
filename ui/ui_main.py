# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(562, 492)
        Main.setStyleSheet(u"/* Global */\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 16px \"Open Sans\";\n"
"}\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 16px \"Open Sans\";\n"
"}\n"
"\n"
"/* Buttons */\n"
"QPushButton#pushButton_new{\n"
"	border-radius:10px;\n"
"	background-color: rgb(78, 154, 6);\n"
"}\n"
"QPushButton#pushButton_new:hover{\n"
"	background-color: rgb(78, 140, 6);\n"
"}\n"
"QPushButton#pushButton_new:pressed{\n"
"	background-color: rgb(78, 125, 6);\n"
"}\n"
"QPushButton#pushButton_save{\n"
"	border-radius:10px;\n"
"	background-color: rgb(242, 85, 9);\n"
"}\n"
"QPushButton#pushButton_save:hover{\n"
"	background-color: rgb(242, 71, 9);\n"
"}\n"
"QPushButton#pushButton_save:pressed{\n"
"	background-color: rgb(242, 56, 9);\n"
"}\n"
"QPushButton#pushButton_logout{\n"
"	border-radius:10px;\n"
"	background-color: rgb(0, 102, 212);\n"
"}\n"
"QPushButton#pushButton_logout:hover{\n"
"	background-color: rgb(0, 88, 212);\n"
"}\n"
"QPushButton#pushButton_logout:pressed{\n"
"	background-color: rgb(0, 73, 21"
                        "2);\n"
"}\n"
"\n"
"/* Scroll Area */\n"
"QScrollArea{\n"
"	background-color: rgb(46, 52, 54);\n"
"}\n"
"QWidget#scrollArea_content{\n"
"	background-color: rgb(46, 52, 54);\n"
"}\n"
"\n"
"/* Frames*/\n"
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
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 		#0066D4, stop:1 #003E7F);\n"
"}\n"
"QWidget#frame_login_main{\n"
"	background-color: rgb(46, 52, 54);\n"
"}")
        self.verticalLayout = QVBoxLayout(Main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_login_up = QFrame(Main)
        self.frame_login_up.setObjectName(u"frame_login_up")
        self.frame_login_up.setFrameShape(QFrame.NoFrame)
        self.frame_login_up.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_login_up)

        self.frame_login_center = QFrame(Main)
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
        self.frame_login_main.setMinimumSize(QSize(400, 400))
        self.frame_login_main.setMaximumSize(QSize(400, 800))
        self.frame_login_main.setFrameShape(QFrame.NoFrame)
        self.frame_login_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_login_main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame_login_main)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_new = QPushButton(self.frame_3)
        self.pushButton_new.setObjectName(u"pushButton_new")
        self.pushButton_new.setMinimumSize(QSize(0, 50))
        self.pushButton_new.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_new)


        self.horizontalLayout_9.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_save = QPushButton(self.frame_4)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMinimumSize(QSize(0, 50))
        self.pushButton_save.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_8.addWidget(self.pushButton_save)


        self.horizontalLayout_9.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_logout = QPushButton(self.frame_5)
        self.pushButton_logout.setObjectName(u"pushButton_logout")
        self.pushButton_logout.setMinimumSize(QSize(0, 50))
        self.pushButton_logout.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_5.addWidget(self.pushButton_logout)


        self.horizontalLayout_9.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.scrollArea = QScrollArea(self.frame_login_main)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QSize(400, 800))
        self.scrollArea.setStyleSheet(u"/* Frame Content */\n"
"QLineEdit{\n"
"	color:white;\n"
"	background-color: rgb(46, 52, 54);\n"
"	border:none;\n"
"	border-bottom:1px solid white;\n"
"}\n"
"QPushButton{\n"
"	border-radius:10px;\n"
"	background-color: rgb(220, 34, 34);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(212, 26, 26);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(201, 15, 15);\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea_content = QWidget()
        self.scrollArea_content.setObjectName(u"scrollArea_content")
        self.scrollArea_content.setGeometry(QRect(0, 0, 384, 400))
        self.verticalLayout_3 = QVBoxLayout(self.scrollArea_content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollArea_content)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.frame_login_main)

        self.frame_login_right = QFrame(self.frame_login_center)
        self.frame_login_right.setObjectName(u"frame_login_right")
        self.frame_login_right.setFrameShape(QFrame.NoFrame)
        self.frame_login_right.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_login_right)


        self.verticalLayout.addWidget(self.frame_login_center)

        self.frame_login_down = QFrame(Main)
        self.frame_login_down.setObjectName(u"frame_login_down")
        self.frame_login_down.setFrameShape(QFrame.NoFrame)
        self.frame_login_down.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_login_down)


        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"todoApp", None))
        self.pushButton_new.setText(QCoreApplication.translate("Main", u"New", None))
        self.pushButton_save.setText(QCoreApplication.translate("Main", u"Save", None))
        self.pushButton_logout.setText(QCoreApplication.translate("Main", u"Logout", None))
    # retranslateUi

