from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CardHeader(QWidget):
    fibo = []
    def __init__(self, fibo_number,parent):
        super(CardHeader, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.__init_background()
        self.__init_widgets(fibo_number)

    def __init_background(self):
        palette1 = QPalette(self)
        palette1.setBrush(self.backgroundRole(), QBrush( QPixmap('./background/bg3.gif')))
        self.setAutoFillBackground(True)
        self.setPalette(palette1)

    def __init_widgets(self, fibo_number):
        self.text = QLabel()
        self.text.setText( str(fibo_number) )
        self.layout.addWidget(self.text, 0)

class CardContent(QLabel):
    def __init__(self, parent):
        super(CardContent, self).__init__(parent)
        self.parent = parent
        self.content = "" 
        palette1 = QPalette(self)
        palette1.setBrush(self.backgroundRole(), QBrush( QPixmap('./background/bg2.gif')))
        self.setAutoFillBackground(True)
        self.setPalette(palette1)
        self.setAcceptDrops(True)

    def setText(self, content):
        super(CardContent, self).setText(content)
        self.content = content

    def notify_card(self):
        self.parent.notify_screen()

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.notify_card()
        self.setText( e.mimeData().text() )

class Card(QLabel):
    def __init__(self, index,parent):
        super(Card, self).__init__(parent)
        self.register_screen(parent)
        self.index = index

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.__init_widgets()

    def __init_widgets(self):
        self.hearder = CardHeader(self.index, self)
        self.content = CardContent(self)
        self.layout.addWidget(self.hearder, 0)
        self.layout.addWidget(self.content, 1)

    def set_content(self, content):
        self.content.setText(content)
    def get_content(self):
        return self.content.content

    def register_screen(self, screen):
        self.screen=screen
    def notify_screen(self):
        self.screen.card_shift(self.index)

class CardScreen(QWidget):
    x_max = 6
    y_max = 4
    card_max = x_max * y_max
    card = []
    def __init__(self, parent=None):
        super(CardScreen, self).__init__(parent)
        self.layout = QGridLayout()

        card_count = 0
        while card_count < self.card_max:
            self.__init_card(card_count)
            card_count += 1

        self.setLayout(self.layout)

    def __init_card(self, index):
        aCard = Card(index,self)
        (x,y) = self.__card_position(index)
        self.layout.addWidget(aCard, y,x)
        self.card.append(aCard)

    def new_card(self, text):
        self.card_shift(0)
        self.card[0].set_content(text)

    def card_shift(self, index):
        cur = self.card_max-1
        while cur > index:
            self.card[cur].set_content( self.card[cur-1].get_content() )
            cur -= 1

    def __card_position(self, index):
        return ( index%self.x_max , index/self.x_max )