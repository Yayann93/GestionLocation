import unittest
from classes.location import Louer

class TestLocation(unittest.TestCase):

    def test_str(self):
        s = Louer(250, 500,"Bahamas", "Auchan", "Durant")
        d = s.__str__()
        self.assertEquals(d, "Date de début de location : 250 ; Date de fin de location : 500 ; Salle louée : Bahamas ; Organisme locataire : Auchan ; Client : Durant")
