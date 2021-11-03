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

    def __str__(self) -> str:
        return "Code Organisme :"+int(self.getcodeOrganisme())+"; Nom Organisme :"+str(self.getnomOrganisme())+"; Numéro d'Agrément :"+int(self.getnumAgrement())

    
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

    def __str__(self) -> str:
        return "Code Client :"+int(self.getcodeClient())+"; Nom Client :"+str(self.getnomClient())+"; Adresse du Client :"+str(self.getadresseClient())+"; Date de naissance :"+int(self.getdateDeNaissance())+"; Organisme :"+str(self.getorganisme())


    #Setter
    def setcodeClient (self, codeClient : int) -> None:
        self.__codeClient = codeClient

    def setnomClient (self, nomClient : str) -> None:
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