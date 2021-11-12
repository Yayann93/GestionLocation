import unittest
from classes.organisme import Organisme

class TestOrganisme(unittest.TestCase):

    def test_str(self):
        o = Organisme(2, "Auchan",51)
        d = o.__str__()
        self.assertEquals(d, "Code Organisme :2; Nom Organisme :Auchan; Numéro d'Agrément :51")
