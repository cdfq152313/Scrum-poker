from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class InputScreen(QWidget):
    def __init__(self, parent=None):
        super(InputScreen, self).__init__(parent)
        self.parent = parent
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.__init_widgets()

    def __init_widgets(self):
        self.edit = QLineEdit("", self)
        self.edit.setDragEnabled(True)
        self.layout.addWidget(self.edit)

        submitButton = QPushButton("Submit", self)
        self.layout.addWidget(submitButton)
        submitButton.clicked.connect(self.notify_screen)

    def notify_screen(self):
        text = self.edit.text()
        self.parent.enter_input(text)