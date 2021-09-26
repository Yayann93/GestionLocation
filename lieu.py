class Lieu:
    def __init__(self, codeLieu, lieuLoc, prix) -> None:
        """
        
        Constructeur lieu
        :param codeLieu: son code dans la base de données
        :param lieuLoc: le lieu de la location
        :param prix: prix à la journée
        
        """
        self.setCodeLieu (codeLieu)
        self.setLieuLoc (lieuLoc)
        self.setPrix (prix)
    def __str__(self) -> str:
        return "code du lieu de location : "+str(self.getcodeLieu())+"; lieu de la location : "+self.getlieuLoc()+"; prix à la journée : "+self.getprix()
    #Setter
    def setCodeLieu (self, codelieu : int) -> None:
        self.__codeLieu = codelieu
    def setLieuLoc (self, lieuLoc : str) -> None:
        self.__lieuLoc = lieuLoc
    def setPrix (self, prix : str) -> None:
        self.__prix = prix
    #Getter
    def getCodeLieu (self) -> int:
        return self.__codeLieu
    def getLieuLoc (self) -> str:
        return self.__lieuLoc
    def getPrix (self) -> str:
        return self.__prix