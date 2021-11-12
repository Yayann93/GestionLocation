import unittest
from classes.organisme import Organisme, Client

class TestOrganisme(unittest.TestCase):

    def test_str(self):
        o = Organisme(2, "Auchan",51)
        d = o.__str__()
        self.assertEquals(d, "Code Organisme :2; Nom Organisme :Auchan; Numéro d'Agrément :51")

class TestClient(unittest.TestCase):

    def test_str(self):
        c = Client(3,"Bertrand", "31 rue des Capucines", "22/08/1965", "Auchan")
        d = c.__str__()
        self.assertEquals(d, "Code Client :3; Nom Client :Bertrand; Adresse du Client :31 rue des Capucines; Date de naissance :22/08/1965; Organisme :Auchan")