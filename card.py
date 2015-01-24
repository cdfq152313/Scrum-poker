from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Card(QLabel):
    prefix = "fibo\n"
    def __init__(self, index,parent):
        super(Card, self).__init__(self.prefix, parent)
        self.register_screen(parent)
        self.index = index
        self.content = "" 
        palette1 = QPalette(self)
        # palette1.setColor(self.backgroundRole(), Qt.red  ) 
        palette1.setBrush(self.backgroundRole(), QBrush( QPixmap('./background/bg2.gif')))
        # background = QPixmap("./poker/1.gif").scaled( Qsize(100,40) );
        # palette1.setBrush(self.backgroundRole(), QBrush(background) ) 
        self.setAutoFillBackground(True)
        self.setPalette(palette1)
        self.setAcceptDrops(True)
        #self.setReadOnly(True)

    def set_content(self, content):
        self.content = content
        self.setText(self.prefix + content)
    def register_screen(self, screen):
        self.screen=screen
    def notify_screen(self):
        self.screen.card_shift(self.index)
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.notify_screen()
        self.set_content( e.mimeData().text() )

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

    def card_shift(self, index):
        cur = self.card_max-1
        while cur > index:
            self.card[cur].set_content( self.card[cur-1].content )
            cur -= 1

    def __card_position(self, index):
        return ( index%self.x_max , index/self.x_max )