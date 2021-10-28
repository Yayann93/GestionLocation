<<<<<<< Updated upstream:classes/location.py
class Location:
    def __init__(self, dateLocation, clientLoueur, lieuLocation, organismeLocation, prixLocation) -> None:
        """
        
        Constructeur de Location
        :param organismeLocation: L'organisme ayant proposé la location
        :param prixLocation: Le prix de la location
        
        """
        self.setDateLocation(dateLocation)
        self.setclientLoueur(clientLoueur)
        self.setlieuLocation(lieuLocation)
        self.setorganismeLocation(organismeLocation)
        self.setprixLocation(prixLocation)

    #Mutateur, Setter
    def setDateLocation (self, dateLocation : str) -> None:
        self.__dateLocation = dateLocation
    #Accesseur, Getter
    def getdateLocation (self) -> str:
        return self.__dateLocation
    def setclientLoueur(self, clientLoueur : str) -> None:
        self.__clientLoueur = clientLoueur
    def getclientLoueur(self) -> str:
        return self.__clientLoueur
    def setlieuLocation (self, lieuLocation : str) -> None:
        self.__lieuLocation = lieuLocation
    def getlieuLocation (self) -> str:
        return self.__lieuLocation
    def setorganismeLocation (self, organismeLocation : str) -> None:
        self.__organismeLocation = organismeLocation
    def getorganismeLocation (self) -> str:
        return self.__organismeLocation
    def setprixLocation (self, prixLocation : str) -> None:
        self.__prixLocation = prixLocation
    def getprixLocation (self) -> str:
        return self.__prixLocation
    
class Client:
    def __init__(self, codeClient, nom, adresse, dateDeNaissance) -> None:
        """
        Constructeur de Client
        :param codeClient: Code du client dans la base de donnée
        """
        self.setCodeClient(codeClient)
        self.setNom(nom)
        self.setAdresse(adresse)
        self.setDateDeNaissance(dateDeNaissance)

    #Setter
    def setCodeClient (self, codeClient : int) -> None:
        self.__codeClient = codeClient
    def getCodeClient (self) -> int:
        return self.__codeClient
    def setNom (self, nom : str) -> None:
        self.__nom = nom
    def getNom (self) -> str:
        return self.__nom
    def setAdresse (self, adresse : str) -> None:
        self.__adresse = adresse
    def getAdresse (self) -> str:
        return self.__adresse
    def setDateDeNaissance (self, dateDeNaissance : str) -> None:
        self.__dateDeNaissance = dateDeNaissance
    def getDateDeNaissance (self) -> str:
        return self.__dateDeNaissance
=======
class Louer:
    def __init__(self, dateDebut, dateFin, salle, organisme, client) -> None:
       
        """

        Constructeur de Louer
        :param dateDebut: Début de la location
        :param dateFin: Fin de la location
        
        """
        self.setdateDebut(dateDebut)
        self.setdateFin(dateFin)
        self.setsalle(salle)
        self.setorganisme(organisme)
        self.setclient(client)

    def __str__(self) -> str:
        return "Date de début de location : "+str(self.getdateDebut())+"; Date de fin de location : "+str(self.getdateFin())+"; Salle louée : "+str(self.getsalle())+"; Organisme locataire : "+str(self.getorganisme())+"; Client : "+str(self.getclient())


    #Mutateur, Setter

    def setdateDebut (self, dateDebut : int) -> None:
        self.__dateDebut = dateDebut

    def setdateFin(self, dateFin : int) -> None:
        self.__dateFin = dateFin

    def setsalle (self, salle : str) -> None:
        self.__salle = salle

    def setorganisme (self, organisme : str) -> None:
        self.__organisme = organisme

    def setclient (self, client : str) -> None:
        self.__client = client


    #Accesseur, Getter

    def getdateDebut (self) -> int:
        return self.__dateDebut
    
    def getdateFin(self) -> int:
        return self.__dateFin
    
    def getsalle (self) -> str:
        return self.__salle
    
    def getorganisme (self) -> str:
        return self.__organisme
    
    def getclient (self) -> str:
        return self.__client



class Salle:
    def __init__(self, codeSalle, nomSalle, prixSalle) -> None:


        self.setcodeSalle (codeSalle)
        self.setnomSalle (nomSalle)
        self.setprixSalle (prixSalle)
    
    def __str__(self) -> str:
        return "Code Salle :"+int(self.getcodeSalle())+"; Nom Salle :"+str(self.getnomSalle())+"; Prix de la Salle :"+int(self.getprixSalle())

    #Mutateur, Setter     
    
    def setcodeSalle (self, codeSalle : int) -> None:
        self.__codeSalle = codeSalle
    
    def setnomSalle (self, nomSalle : str) -> None:
        self.__nomSalle = nomSalle
    
    def setprixSalle (self, prixSalle : int) -> None:
        self.__prixSalle = prixSalle

    #Accesseur, Getter

    def getcodeSalle (self) -> int:
        return self.__codeSalle

    def getnomSalle (self) -> str:
        return self.__nomSalle

    def getprixSalle (self) -> int:
        return self.__prixSalle
>>>>>>> Stashed changes:location.py
