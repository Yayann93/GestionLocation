from classes.location import Louer, Salle
from classes.organisme import Organisme, Client
"""

Import des différentes classes du projet

"""
### Organismes
oa = Organisme (codeOrga=1, nomOrga="Auchan", numOrga=1)
ob = Organisme (codeOrga=2, nomOrga="Casino", numOrga=2)
oc = Organisme (codeOrga=3, nomOrga="Leclerc", numOrga=3)
od = Organisme (codeOrga=4, nomOrga="Carrefour", numOrga=4)

print (oa)
print (ob)
print (oc)
print (od)

### Client
ca = Client (codeClient=1, nomClient="M. BERNARD", adresseClient="28 rue des églantines", dateDeNaissance="28/03/1984", organisme="Auchan")

print (ca)

### Salle
sa = Salle (codeSalle=1, nomSalle="Bahamas", prixSalle="1300€")
sb = Salle (codeSalle=2, nomSalle="Canaries", prixSalle="1150€")
sc = Salle (codeSalle=3, nomSalle="Antilles", prixSalle="1200€")
sd = Salle (codeSalle=4, nomSalle="Ibiza", prixSalle="600€")

print (sa)
print (sb)
print (sc)
print (sd)


### Location
la = Louer (dateDebut=1639569600, dateFin=1639591200, salle="Bahamas",organisme="Auchan",client="M. BERNARD")

print (la)