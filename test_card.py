import unittest
import card
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CardScreenTestCase(unittest.TestCase):
    def setUp(self):
        self.args = ['hello moto', 'hehehe', 'dadadodo']

        app = QApplication(sys.argv)
        self.screen = card.CardScreen()
        self.screen.show()

    def tearDown(self):
        self.screen = None

    def test_new_card(self):
        for s in self.args:
            self.screen.new_card(s)
        i = 0
        while i < len( self.args ):
            card_s = self.screen.card[i].get_content()
            arg_s = self.args[ len(self.args)-i-1 ]
            self.assertEquals(card_s , arg_s) 
            i+=1
    def test_shift_card(self):
        pass

if __name__ == '__main__':
    tests = unittest.TestLoader().loadTestsFromTestCase(CardScreenTestCase)
    unittest.TextTestRunner(verbosity=2).run(tests)
