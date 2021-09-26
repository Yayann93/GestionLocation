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