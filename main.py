import sys

from PySide2.QtCore import QSize, Qt, QRegExp
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QFrame, QVBoxLayout, QLineEdit

from ui.ui_login import Ui_Login
from ui.ui_register import Ui_Register
from ui.ui_main import Ui_Main


class MainWindow(QWidget):
    counter = 1

    def __init__(self):
        QWidget.__init__(self)
        self.ui_login = Ui_Login()
        self.ui_login.setupUi(self)

        self.ui_register_window = QWidget()
        self.ui_register = Ui_Register()
        self.ui_register.setupUi(self.ui_register_window)

        self.ui_main_window = QWidget()
        self.ui_main = Ui_Main()
        self.ui_main.setupUi(self.ui_main_window)

    # Button connections
        self.ui_login.pushButton_register.clicked.connect(self.register_window)
        self.ui_register.pushButton_back.clicked.connect(self.login_window)
        self.ui_login.pushButton_login.clicked.connect(self.main_window)
        self.ui_main.pushButton_logout.clicked.connect(self.login_window)
        self.ui_main.pushButton_new.clicked.connect(self.content)
        self.ui_main.pushButton_remove.clicked.connect(self.remove)



        # Window show
    def register_window(self):
        self.ui_register_window.show()
        self.hide()

    def login_window(self):
        self.show()
        self.ui_register_window.hide()
        self.ui_main_window.hide()

    def main_window(self):
        self.ui_main_window.show()
        self.hide()

    def content(self):
        self.widgets = []
        self.ui_main.widget_content = QWidget(self.ui_main.scrollArea_content)
        self.ui_main.widget_content.setObjectName(u"widget_content")
        self.ui_main.widget_content.setMinimumSize(QSize(70, 70))
        self.ui_main.widget_content.setMaximumSize(QSize(700, 70))
        self.ui_main.horizontalLayout_4 = QHBoxLayout(self.ui_main.widget_content)
        self.ui_main.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ui_main.frame_content_line = QFrame(self.ui_main.widget_content)
        self.ui_main.frame_content_line.setObjectName(u"frame_content_line")
        self.ui_main.frame_content_line.setFrameShape(QFrame.NoFrame)
        self.ui_main.frame_content_line.setFrameShadow(QFrame.Raised)
        self.ui_main.verticalLayout_7 = QVBoxLayout(self.ui_main.frame_content_line)
        self.ui_main.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.ui_main.lineEdit_content = QLineEdit(self.ui_main.frame_content_line)
        self.ui_main.lineEdit_content.setObjectName(u"lineEdit_content")
        self.ui_main.verticalLayout_7.addWidget(self.ui_main.lineEdit_content)
        self.ui_main.horizontalLayout_4.addWidget(self.ui_main.frame_content_line)
        self.ui_main.frame_content_btn = QFrame(self.ui_main.widget_content)
        self.ui_main.frame_content_btn.setObjectName(u"frame_content_btn")
        self.ui_main.frame_content_btn.setMinimumSize(QSize(0, 0))
        self.ui_main.frame_content_btn.setMaximumSize(QSize(80, 16777215))
        self.ui_main.frame_content_btn.setFrameShape(QFrame.NoFrame)
        self.ui_main.frame_content_btn.setFrameShadow(QFrame.Raised)
        self.ui_main.verticalLayout_6 = QVBoxLayout(self.ui_main.frame_content_btn)
        self.ui_main.verticalLayout_6.setSpacing(0)
        self.ui_main.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.ui_main.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ui_main.pushButton_remove = QPushButton(self.ui_main.frame_content_btn)
        self.ui_main.pushButton_remove.setObjectName(f"pushButton_remove{self.counter}")
        self.ui_main.pushButton_remove.setMinimumSize(QSize(0, 50))
        self.ui_main.pushButton_remove.setMaximumSize(QSize(80, 16777215))
        self.ui_main.pushButton_remove.setText(u"Remove")
        self.ui_main.verticalLayout_6.addWidget(self.ui_main.pushButton_remove)
        self.ui_main.horizontalLayout_4.addWidget(self.ui_main.frame_content_btn)
        self.widgets.append(self.ui_main.widget_content)
        self.ui_main.verticalLayout_3.addWidget(self.ui_main.widget_content, 0, Qt.AlignTop)


    def remove(self):
        self.widgets = self.ui_main.scrollArea_content.findChildren(QWidget, 'widget_content')
        print(self.widgets)
        print(self.widgets[0].objectName())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
