import unittest
from location import Louer

class TestLocation(unittest.TestCase):

    def test_str(self):
        s = Louer(12/5/2020, 16/5/2020,"Bahamas", "Auchan", "Durant")
        d = s.__str__()
        self.assertEquals(d, "Date de début de location : 12/06/2020 ; Date de fin de location : 16/06/2020 ; Salle louée : Bahamas ; Organisme locataire : Auchan ; Client : Durant")
