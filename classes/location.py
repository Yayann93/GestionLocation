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