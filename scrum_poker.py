import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from card import CardScreen
from input_ import InputScreen

class Form(QWidget):
    x_max = 640
    y_max = 480

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.__init_widgets()

        self.setWindowTitle("Fibonacci Card")
        self.resize(self.x_max, self.y_max)
    def __init_widgets(self):
        self.input_ = InputScreen(parent=self)
        self.layout.addWidget(self.input_, 1, 0)

        self.display = CardScreen(parent=self)
        self.layout.addWidget(self.display, 0, 0)

    def enter_input(self, text):
        self.display.new_card(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = Form()
    widget.show()
    app.exec_()

