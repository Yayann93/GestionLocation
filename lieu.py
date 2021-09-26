class Lieu:
    def __init__(self, codeLieu, lieuLoc, prix) -> None:
        """
        
        Constructeur lieu
        :param codeLieu: son code dans la base de données
        :param lieuLoc: le lieu de la location
        :param prix: prix à la journée
        
        """
        self.setcodeLieu (codeLieu)
        self.setlieuLoc (lieuLoc)
        self.setprix (prix)
    def __str__(self) -> str:
        return "code du lieu de location : "+str(self.getcodeLieu())+"; lieu de la location : "+self.getlieuLoc()+"; prix à la journée : "+self.getprix()
    #Setter
    def setcodeLieu (self, codelieu : int) -> None:
        self.__codeLieu = codelieu
    def setlieuLoc (self, lieuLoc : str) -> None:
        self.__lieuLoc = lieuLoc
    def setprix (self, prix : str) -> None:
        self.__prix = prix
    #Getter
    def getcodeLieu (self) -> int:
        return self.__codeLieu
    def getlieuLoc (self) -> str:
        return self.__lieuLoc
    def getprix (self) -> str:
        return self.__prix