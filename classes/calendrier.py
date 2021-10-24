class Jour:
    def __init__(self, nomJour, numJour) -> None:
        """
        
        Constructeur jour
        :param nomJour: Le nom du jour (Lundi, mardi,...)
        :param numeroJour: Numéro du jour dans le mois

        """
        self.setnomJour (nomJour)
        self.setnumeroJour (numJour)
    
    #Setter
    def setnomJour (self, nomJour : str) -> None:
        self.__nomJour = nomJour
    def setnumeroJour (self, numJour : int) -> None:
        self.__numJour = numJour
    #Getter
    def getnomJour (self) -> str:
        return self.__nomJour
    def getnumeroJour (self) -> int:
        return self.__numJour

class Mois:
    def __init__(self, nomMois, numMois, jourMois) -> None:
        """
        Constructeur mois
        
        :param numeroMois: Le numéro du mois dans l'année
        :param jourMois: La liste des jours dans le mois
        """
        self.setnomMois (nomMois)
        self.setnumeroMois (numMois)
        self.setjourMois (jourMois)
    #Setter
    def setnomMois (self, nomMois : str) -> None:
        self.__nomMois = nomMois
    def setnumeroMois (self, numMois : int) -> None:
        self.__numeroMois = numMois
    def setjourMois (self, jourMois : list) -> None:
        self.__jourMois = jourMois
    #Getter
    def getnomMois (self) -> str:
        return self.__nomMois
    def getnumeroMois (self) -> int:
        return self.__numeroMois
    def getjourMois (self) -> list:
        return self.__jourMois

class Annee:
    def __init__(self, nomAnnee, numAnnee, moisAnnee) -> None:
        """

        Constructeur annee
        :param nomAnnee: Le nom de l'année en toutes lettres (deux milles vingt et un,...)
        :param numAnnee: Le numéro de l'année en suivant le calendrier grégorien en vigueur en France

        """
        self.setnomAnnee (nomAnnee)
        self.setnumAnnee (numAnnee)
        self.setmoisAnnee (moisAnnee)
    #Setter
    def setnomAnnee (self, nomAnnee : str) -> None:
        self.__nomAnnee = nomAnnee
    def setnumAnnee (self, numAnnee : int) -> None:
        self.__numAnnee = numAnnee
    def setmoisAnnee (self, moisAnnee : list) -> None:
        self.__moisAnnee = moisAnnee
    #Getter
    def getnomAnnee (self) -> str:
        return self.__nomAnnee
    def getnumAnnee (self) -> int:
        return self.__numAnnee
    def getmoisAnnee (self) -> list:
        return self.__moisAnnee