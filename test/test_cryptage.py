import unittest
import mockito
from service.cryptage import *

class TestCryptage(unittest.TestCase):

    def test_cryptage(self):
        cryptage = Cryptage()
        self.assertEquals('name', cryptage.crypt('name'))
