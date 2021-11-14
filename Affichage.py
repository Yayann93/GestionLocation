from classes.organisme import Client, Organisme
from classes.location import Louer, Salle
import sqlite3

def consulterClient():
    con = sqlite3.connect('Travail.db')
    cur = con.cursor()
    ls = []
    for row in cur.execute('''SELECT * FROM client'''):
        c = Client (row[0], row[1], row[2], row [3], row [4])
        ls.append(c)
    con.close()
    return ls

def consulterOrganisme():
    con = sqlite3.connect('Travail.db')
    cur = con.cursor()
    ls=[]
    for row in cur.execute('''SELECT * FROM organisme'''):
        o= Organisme (row[0], row[1], row[2])
        ls.append(o)
    con.close()
    return ls

def consulterLocation():    
    con = sqlite3.connect('Travail.db')
    cur = con.cursor()
    ls = []
    for row in cur.execute('''SELECT * FROM client, organisme, louer, salle WHERE client.codeClient = louer.codeClient AND organisme.codeOrganisme = louer.codeOrganisme AND salle.codeSalle = louer.codeSalle'''):
        l = Louer (row[8], row[9], Salle(row[13], row[14], row[15]), Organisme(row[5], row[6], row[7]), Client(row[0], row[1], row[2], row[3], row[4]))
        ls.append(l)
    con.close()
    return ls

def consulterSalle():
    con = sqlite3.connect('Travail.db')
    cur = con.cursor()
    ls=[]
    for row in cur.execute('''SELECT * FROM salle'''):
        s = Salle (row[0], row[1], row[2])
        ls.append(s)
    con.close()
    return ls