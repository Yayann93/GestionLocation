from classes.organisme import Client, Organisme
from classes.location import Louer, Salle
from classes.lieu import Lieu
import sqlite3

con = sqlite3.connect('Travail.db')
cur = con.cursor()

def consulterClient():
    for row in cur.execute('''SELECT * FROM client'''):
        c = Client (row[0], row[1], row[2], row [3], row [4])
        print (c)

def consulterOrganisme():
    for row in cur.execute('''SELECT * FROM organisme'''):
        o= Organisme (row[0], row[1], row[2])
        print (o)

def consulterLocation():
    for row in cur.execute('''SELECT * FROM client, organisme, louer, salle WHERE client.codeClient = louer.codeClient AND organisme.codeOrganisme = louer.codeOrganisme AND salle.codeSalle = louer.codeSalle'''):
        l = Louer (row[8], row[9], Salle(row[13], row[14], row[15]), Organisme(row[5], row[6], row[7]), Client(row[0], row[1], row[2], row[3], row[4]))
        print (l)

def consulterSalle():
    for row in cur.execute('''SELECT * FROM salle'''):
        s = Salle (row[0], row[1], row[2])
        print (s)


def choixConsulter():
    consulter=input("Quelle catégorie souhaitez-vous consulter ? [Client; Organisme; Location; Salle]")

    if consulter == "Client":
        consulterClient()
    
    elif consulter == "Organisme":
        consulterOrganisme()
    
    elif consulter == "Location":
        consulterLocation()
    
    elif consulter == "Salle":
        consulterSalle()


choixConsulter()


con.close()