<<<<<<< Updated upstream:classes/organisme.py
class Organisme:
    def __init__(self, codeOrga, nomOrga, numOrga) -> None:
        """
        
        Constructeur Organisme
        :param codeOrga: son code dans la base de donnée
        :param numOrga: son numéro d'agrément
        
        """
        self.setcodeOrga (codeOrga)
        self.setnomOrga (nomOrga)
        self.setnumOrga (numOrga)

    def __str__(self) -> str:
        return "code de l'organisme : "+str(self.getcodeOrga())+"; nom de l'organisme : "+self.getnomOrga()+"; numéro de l'organisme : "+str(self.getnumOrga())
    
    #Setter
    def setcodeOrga (self, codeOrga : int) -> None:
        self.__codeOrga = codeOrga
    def setnomOrga (self, nomOrga : str) -> None:
        self.__nomOrga = nomOrga
    def setnumOrga (self, numOrga : int) -> None:
        self.__numOrga = numOrga
    #Getter
    def getcodeOrga (self) -> int:
        return self.__codeOrga
    def getnomOrga (self) -> str:
        return self.__nomOrga
    def getnumOrga (self) -> int:
        return self.__numOrga
=======
class Organisme:

    def __init__(self, codeOrganisme, nomOrganisme, numAgrement) -> None:

        """
        
        Constructeur Organisme
        :param codeOrganisme: son code dans la base de donnée
        :param numOrganisme: son numéro d'agrément
        
        """

        self.setcodeOrganisme (codeOrganisme)
        self.setnomOrganisme (nomOrganisme)
        self.setnumAgrement (numAgrement)

    
    #Setter

    def setcodeOrganisme (self, codeOrganisme : int) -> None:
        self.__codeOrganisme = codeOrganisme

    def setnomOrganisme (self, nomOrganisme : str) -> None:
        self.__nomOrganisme = nomOrganisme

    def setnumAgrement (self, numAgrement : int) -> None:
        self.__numAgrement = numAgrement

    #Getter

    def getcodeOrganisme (self) -> int:
        return self.__codeOrganisme

    def getnomOrganisme (self) -> str:
        return self.__nomOrganisme

    def getnumAgrement (self) -> int:
        return self.__numAgrement
            
class Client:

    def __init__(self, codeClient, nomClient, adresseClient, dateDeNaissance, organisme) -> None:
        """
        Constructeur de Client
        :param codeClient: Code du client dans la base de donnée
        """
        self.setcodeClient (codeClient)
        self.setnomClient (nomClient)
        self.setadresseClient (adresseClient)
        self.setdateDeNaissance (dateDeNaissance)
        self.setorganisme (organisme)

    #Setter
    def setcodeClient (self, codeClient : int) -> None:
        self.__codeClient = codeClient

    def setnomClient (self, nomClient : int) -> None:
        self.__nomClient = nomClient

    def setadresseClient (self, adresseClient : str) -> None:
        self.__adresseClient = adresseClient

    def setdateDeNaissance (self, dateDeNaissance : int) -> None:
        self.__dateDeNaissance = dateDeNaissance

    def setorganisme (self, organisme : str) -> None:
        self.__organisme = organisme


    #Getter
    def getcodeClient (self) -> int:
        return self.__codeClient

    def getnomClient (self) -> int:
        return self.__nomClient

    def getadresseClient (self) -> str:
        return self.__adresseClient

    def getdateDeNaissance (self) -> int:
        return self.__dateDeNaissance

    def getorganisme (self) -> str:
        return self.__organisme
>>>>>>> Stashed changes:organisme.py
