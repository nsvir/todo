import unittest
from somme import *

class TestAddTwo(unittest.TestCase):

    def test_add_un_un(self):
        somme = Somme()
        self.assertEquals(2, somme.add(1,1))
