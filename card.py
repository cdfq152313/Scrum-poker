from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class CardHeader(QWidget):
    fibo = []
    import csv
    with open('fibo.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            fibo = row

    def __init__(self, index,parent):
        super(CardHeader, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.__init_background()
        self.__init_widgets(self.fibo[index])

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
        palette1 = QPalette(self)
        palette1.setBrush(self.backgroundRole(), QBrush( QPixmap('./background/bg2.gif')))
        self.setAutoFillBackground(True)
        self.setPalette(palette1)
        self.setAcceptDrops(True)

    def notify_card_shift(self):
        self.parent.notify_screen_shift(None)
    def notify_card_shift(self, drop_index):
        self.parent.notify_screen_shift(drop_index)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        if e.mimeData().hasHtml():
            self.notify_card_shift( int(e.mimeData().html()) )
        else:
            self.notify_card_shift()
        self.setText( e.mimeData().text() )

    def mouseMoveEvent(self, e):
        if e.buttons() and Qt.LeftButton:
            distance = (e.pos() - self.startPos).manhattanLength()
            if distance >= QApplication.startDragDistance():
                self.performDrag()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.startPos = e.pos()
        super(CardContent, self).mousePressEvent(e)

    def performDrag(self):
        mimeData = QMimeData()
        mimeData.setText(self.text())
        mimeData.setHtml(str(self.parent.index))
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        if drag.exec_(Qt.MoveAction) == Qt.MoveAction:
            pass
        
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
        return self.content.text()

    def register_screen(self, screen):
        self.screen=screen
    def notify_screen_shift(self, drag_index):
        self.screen.card_shift(drag_index, self.index)

class CardScreen(QWidget):
    x_max = 5
    y_max = 3
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
        self.card_shift(None, 0)
        self.card[0].set_content(text)

    def card_shift(self, drag_index, drop_index):
        if drag_index is None:
            drag_index = self.card_max-1
        # drag_index in fornt of drop_index
        if drag_index < drop_index:
            cur = drag_index
            while cur < drop_index:
                self.card[cur].set_content( self.card[cur+1].get_content() )
                cur += 1
        elif drag_index > drop_index:
            cur = drag_index
            while cur > drop_index:
                self.card[cur].set_content( self.card[cur-1].get_content() )
                cur -= 1

    def __card_position(self, index):
        return ( index%self.x_max , index/self.x_max )
