import sys

from PySide2.QtCore import QSize, Qt, QRegExp, QRect
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QFrame, QVBoxLayout, QLineEdit, \
    QButtonGroup

from ui.ui_login import Ui_Login
from ui.ui_register import Ui_Register
from ui.ui_main import Ui_Main


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
        self.ui_login.pushButton_login.clicked.connect(self.main_window)
        self.ui_main.pushButton_logout.clicked.connect(self.login_window)
        self.ui_main.pushButton_new.clicked.connect(self.new)

        # Create button group and slot
        self.btn_group = QButtonGroup(self.ui_main.scrollArea_content)
        self.btn_group.buttonClicked.connect(self.remove)

        # Counter used to name buttons
        self.counter = 0

    # Show register window
    def register_window(self):
        self.ui_register_window.show()
        self.hide()

    # Show login window
    def login_window(self):
        self.show()
        self.ui_register_window.hide()
        self.ui_main_window.hide()

    # Show app window
    def main_window(self):
        self.ui_main_window.show()
        self.hide()

    # New item function
    def new(self):
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
        self.btn_group.addButton(self.ui_main.btn_remove)
        # Increment the counter to name the next button
        self.counter += 1

    # remove item function
    def remove(self, btn):
        btn.parent().deleteLater()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
