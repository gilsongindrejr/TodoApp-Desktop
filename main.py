import sys
import sqlite3
import os

from PySide2.QtCore import QSize, Qt, QRegExp, QRect
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QFrame, QVBoxLayout, QLineEdit, QButtonGroup

from ui.ui_login import Ui_Login
from ui.ui_register import Ui_Register
from ui.ui_main import Ui_Main
from models.user import User
from auth import auth_user, auth_pass_reg, auth_pass_log, auth_email


class MainWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        # Login Window
        self.ui_login = Ui_Login()
        self.ui_login.setupUi(self)

        # Register Window
        self.ui_register_window = QWidget()
        self.ui_register = Ui_Register()
        self.ui_register.setupUi(self.ui_register_window)

        # App window
        self.ui_main_window = QWidget()
        self.ui_main = Ui_Main()
        self.ui_main.setupUi(self.ui_main_window)

        # Button connections
        self.ui_login.pushButton_register.clicked.connect(self.register_window)
        self.ui_register.pushButton_back.clicked.connect(self.login_window)
        self.ui_login.pushButton_login.clicked.connect(self.login)
        self.ui_main.pushButton_logout.clicked.connect(self.login_window)
        self.ui_main.pushButton_new.clicked.connect(self.new)
        self.ui_register.pushButton_register.clicked.connect(self.register)

        # Create button group and slot
        self.btn_group = QButtonGroup(self.ui_main.scrollArea_content)
        self.btn_group.idClicked.connect(self.remove)

        # Counter used to name buttons
        self.counter = 0

        # DB path constant
        self.DB_PATH = './dbase.db'

    # Show register window
    def register_window(self):
        '''Show register window'''
        self.ui_register_window.show()
        self.hide()

    # Show login window
    def login_window(self):
        '''Show login window'''
        self.show()
        self.ui_register_window.hide()
        self.ui_main_window.hide()


    # New item function
    def new(self):
        '''Create a new button(frame containing button and line edit'''
        # Create the frame
        self.ui_main.frame_content = QFrame(self.ui_main.scrollArea_content)
        self.ui_main.frame_content.setObjectName(f"frame_content_{self.counter}")
        self.ui_main.frame_content.setMaximumSize(QSize(16777215, 70))
        self.ui_main.frame_content.setFrameShape(QFrame.StyledPanel)
        self.ui_main.frame_content.setFrameShadow(QFrame.Raised)
        # Create horizontal layout
        self.ui_main.horizontalLayout_4 = QHBoxLayout(self.ui_main.frame_content)
        self.ui_main.horizontalLayout_4.setObjectName(f"horizontalLayout_4_{self.counter}")
        # Create line edit content
        self.ui_main.line_content = QLineEdit(self.ui_main.frame_content)
        self.ui_main.line_content.setObjectName(f"line_content_{self.counter}")
        # Add line edit content to horizontal layout
        self.ui_main.horizontalLayout_4.addWidget(self.ui_main.line_content)
        # Create the button remove
        self.ui_main.btn_remove = QPushButton(self.ui_main.frame_content)
        self.ui_main.btn_remove.setObjectName(f"btn_remove_{self.counter}")
        self.ui_main.btn_remove.setMinimumSize(QSize(0, 50))
        self.ui_main.btn_remove.setMaximumSize(QSize(80, 16777215))
        self.ui_main.btn_remove.setText(u"Remove")
        # Add button remove to horizontal layout
        self.ui_main.horizontalLayout_4.addWidget(self.ui_main.btn_remove)
        # Add the frame content(contains line edit and button) to vertical layout
        self.ui_main.verticalLayout_3.addWidget(self.ui_main.frame_content, 0, Qt.AlignTop)
        # Add button to group
        self.btn_group.addButton(self.ui_main.btn_remove, self.counter)
        # Increment the counter to name the next button
        self.counter += 1

    # remove item function
    def remove(self, btn_id):
        '''Remove button(the label containing the button and line edit'''
        self.btn_group.button(btn_id).parent().deleteLater()

    def db_check(self):
        '''Check if database exists if not it create'''
        if os.path.isfile(self.DB_PATH):
            self.dbase = sqlite3.connect('dbase.db')
            print('Database already exists')
        else:
            self.dbase = sqlite3.connect('dbase.db')
            cursor = self.dbase.cursor()
            cursor.execute("CREATE TABLE users('username' text, 'password' text, 'email' text)")
            print('Database created')

    def register(self):
        '''Register new user'''
        self.db_check()
        # Instantiate user
        user = User(self.ui_register.lineEdit_user.text(), self.ui_register.lineEdit_pass.text(),
                    self.ui_register.lineEdit_confirm.text(), self.ui_register.lineEdit_email.text())
        cursor = self.dbase.cursor()
        # Get data from database to authenticate user
        cursor.execute(f"SELECT username FROM users WHERE username='{user.name}'")
        db_name = cursor.fetchall()
        cursor.execute(f"SELECT email FROM users WHERE email='{user.email}'")
        db_email = cursor.fetchall()
        # Call the authentication functions
        user_auth = auth_user(user.name, db_name)
        pass_auth = auth_pass_reg(user.password, user.password_c)
        email_auth = auth_email(user.email, db_email)
        # Let or not user register
        if user_auth == 0:
            if pass_auth == 0:
                if email_auth == 0:
                    cursor.execute(f"INSERT INTO users VALUES('{user.name}', '{user.password}', '{user.email}')")
                    self.dbase.commit()
                    print('Data inserted sucessfuly')
                    self.ui_register.lineEdit_user.clear()
                    self.ui_register.lineEdit_pass.clear()
                    self.ui_register.lineEdit_confirm.clear()
                    self.ui_register.lineEdit_email.clear()
                    self.ui_register.label_info.setText('Account created successfully')
                else:
                    self.ui_register.label_info.setText('Email already in use')
            else:
                self.ui_register.label_info.setText("Password doesn't match")
        else:
            self.ui_register.label_info.setText('Username already exists')

    def login(self):
        self.db_check()
        name = self.ui_login.lineEdit_user.text()
        password = self.ui_login.lineEdit_pass.text()
        cursor = self.dbase.cursor()
        cursor.execute(f"SELECT username FROM users WHERE username='{name}'")
        db_name = cursor.fetchall()
        cursor.execute(f"SELECT password FROM users WHERE password='{password}'")
        db_password = cursor.fetchall()
        user_auth = auth_user(name, db_name)
        pass_auth = auth_pass_log(password, db_password)
        if user_auth:
            if pass_auth:
                print('Login Successful')
                self.ui_main_window.show()
                self.hide()
            else:
                print("Incorrect password")
        else:
            print("Username doesn't exists")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
