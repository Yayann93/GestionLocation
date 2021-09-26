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
