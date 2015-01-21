import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Card(QTextEdit):
    def __init__(self, title, parent):
        super(Card, self).__init__("fibo\n" + title, parent)
        palette1 = QPalette(self)
        # palette1.setColor(self.backgroundRole(), Qt.red  ) 
        palette1.setBrush(self.backgroundRole(), QBrush( QPixmap('./background/bg2.gif')))
        self.setAutoFillBackground(True)
        self.setPalette(palette1)
        self.setAcceptDrops(True)
        self.setReadOnly(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        fibo = "fibo\n"
        display = fibo + e.mimeData().text()
        self.setText(display)

class Form(QWidget):
    x_max = 640
    y_max = 480
    card_x_max = 6
    card_y_max = 4
    card_max = card_x_max * card_y_max
    card_count = 0

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        mainLayout = QGridLayout()
        mainLayout.addLayout(self.__input_init(), 1, 0)
        self.display_layout = self.__display_init()
        mainLayout.addLayout(self.display_layout, 0, 0)

        self.new_card("hello world")
        while self.card_count < self.card_max:
            self.new_card("compiler作業")

        self.setLayout(mainLayout)
        self.setWindowTitle("Fibonacci Card")
        self.resize(640,480)
    def __input_init(self):
        input_layout = QHBoxLayout()

        self.input_line = QLineEdit("", self)
        input_layout.addWidget(self.input_line)

        submitButton = QPushButton("Submit", self)
        input_layout.addWidget(submitButton)
        submitButton.clicked.connect(self.submitContact)
        return input_layout

    def __display_init(self):
        display_layout = QGridLayout()
        return display_layout

    def new_card(self, content):
        aCard = Card(content, self)
        (x,y) = self.__card_position(self.card_count)
        self.display_layout.addWidget(aCard, y,x)
        self.card_count += 1

    def __card_position(self, index):
        return ( index%self.card_x_max , index/self.card_x_max )
    
    def submitContact(self):
        input_data = self.input_line.text()
        self.new_card(input_data)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = Form()
    widget.show()
    app.exec_()

