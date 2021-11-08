import unittest
from classes.lieu import Lieu

class TestLieu(unittest.TestCase):

    def test_str(self):
        l = Lieu(0,"Bahamas",12)
        d = l.__str__()
        self.assertEquals(d, "code du lieu de location : 0; lieu de la location : Bahamas; prix à la journée : 12")
    
    def test_getPrix(self):
        l = Lieu(0,"Bahamas",12)
        self.assertEquals(l.getPrix(), 12)