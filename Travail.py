from classes.location import Louer, Salle
from classes.organisme import Organisme, Client
import sqlite3
con = sqlite3.connect('Travail.db')


cur = con.cursor()
cur.execute('''INSERT INTO organisme (nomOrganisme, codeNumAgrement) VALUES("Auchan",3)''')
cur.execute('''INSERT INTO client (nomClient, adresseClient, dateDeNaissance, codeOrganisme) VALUES ("M. BERNARD", "28 rue des églantines", "28/03/1984", "Auchan")''')
con.commit()
con.close()


"""

Import des différentes classes du projet

"""
### Organismes
oa = Organisme (codeOrganisme=1, nomOrganisme="Auchan", numAgrement=1)
ob = Organisme (codeOrganisme=2, nomOrganisme="Casino", numAgrement=2)
oc = Organisme (codeOrganisme=3, nomOrganisme="Leclerc", numAgrement=3)
od = Organisme (codeOrganisme=4, nomOrganisme="Carrefour", numAgrement=4)

print (oa)
print (ob)
print (oc)
print (od)

oa.save('Travail.db')

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