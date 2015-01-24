import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from card import *


class Form(QWidget):
    x_max = 640
    y_max = 480

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        mainLayout = QGridLayout()
        mainLayout.addLayout(self.__input_init(), 1, 0)
        self.display = CardScreen(parent=self)
        mainLayout.addWidget(self.display, 0, 0)

        self.setLayout(mainLayout)
        self.setWindowTitle("Fibonacci Card")
        self.resize(self.x_max, self.y_max)

    def __input_init(self):
        input_layout = QHBoxLayout()

        self.input_line = QLineEdit("", self)
        input_layout.addWidget(self.input_line)

        submitButton = QPushButton("Submit", self)
        input_layout.addWidget(submitButton)
        submitButton.clicked.connect(self.submitContact)
        return input_layout
  
    def submitContact(self):
        input_data = self.input_line.text()
        self.display.new_card(input_data)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = Form()
    widget.show()
    app.exec_()

