import unittest
from classes.location import Louer, Salle

class TestLocation(unittest.TestCase):

    def test_str(self):
        s = Louer(250, 500,"Bahamas", "Auchan", "Durant")
        d = s.__str__()
        self.assertEquals(d, "Date de début de location : 250; Date de fin de location : 500; Salle louée : Bahamas; Organisme locataire : Auchan; Client : Durant")

class TestSalle(unittest.TestCase):

    def test_str(self):
        r = Salle (1, "Bahamas", "1300€")
        d = r.__str__()
        self.assertEquals(d, "Code Salle :1; Nom Salle :Bahamas; Prix de la Salle :1300€")