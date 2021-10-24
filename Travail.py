from classes.location import Location, Client
from classes.calendrier import Jour, Mois, Annee
from classes.organisme import Organisme
from classes.lieu import Lieu
"""

Import des différentes classes du projet

"""
### Organismes
a = Organisme (codeOrga=1, nomOrga="Auchan", numOrga=1)
b = Organisme (codeOrga=2, nomOrga="Casino", numOrga=2)
c = Organisme (codeOrga=3, nomOrga="Leclerc", numOrga=3)
d = Organisme (codeOrga=4, nomOrga="Carrefour", numOrga=4)

print (a)
print (b)
print (c)
print (d)

print("Ca marche du tonnerre")

### Salles
aa = Lieu (codeLieu=1, lieuLoc="Bahamas", prix="1300€")
ab = Lieu (codeLieu=2, lieuLoc="Canaries", prix="1150€")
ac = Lieu (codeLieu=3, lieuLoc="Antilles", prix="1200€")
ad = Lieu (codeLieu=4, lieuLoc="Ibiza", prix="600€")

print (aa)
print (ab)
print (ac)
print (ad)


from datetime import date

today = date.today()
print("Date d'aujourd'hui:", today)