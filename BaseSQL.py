import sqlite3

class Database:
    """
        Classe effectuant la connexion

        :author: Delmas Pierre <panda@delmasweb.net>
        :date: 30 Août 2021
        :version: 0.3
    """

    def __init__(self, filePath : str) -> None:
        """
            Constructeur de la classe d'appel SQL
            
            :param filePath: Le chemin du fichier de base de données
            :type filePath: str
            :rtype: None
        """
        self.__connectToDB(filePath)

    def __setFilePath(self, filePath : str) -> None:
        """
            Mutateur du chemin de fichier

            :param filePath: Le chemin du fichier de base de données
            :type filePath: str
            :rtype: None
            :meta private:
        """
        self.__filePath = filePath

    def getFilePath(self) -> str:
        """
            Accesseur du chemin de la base de données
        
            :returns: Le chemin du fichier de la base de données sous la forme d'une chaîne de caractères
            :rtype: str
            :meta public:
        """
        return self.__filePath

    def getCursor(self) -> sqlite3.Cursor:
        """
            Accesseur du curseur de base de données

            :returns: Un curseur sqlite3.Cursor de la base de données
            :rtype: sqlite3.Cursor
            :meta public:
        """
        return self.__cur
    
    def __getConnection(self) -> sqlite3.Connection:
        """
            Accesseur de la connexion à la base de données

            :returns: Une connexion à la base de données sqlite3.Connection
            :rtype: sqlite3.Connection
            :meta private:
        """
        return self.__conn

    
    def commit(self):
        """
            Cette méthode permet de commit les modifications dans la base de données
            :rtype: None
            :meta public:
        """
        self.__getConnection().commit()

    def __connectToDB(self, filePath : str) -> None:
        """
            Cette méthode permet de faire la connexion à la base de données

            :param filePath: Le chemin de la base de données
            :rtype: None
            :meta private:
        """
        self.__setFilePath(filePath)
        self.__conn = sqlite3.connect(self.getFilePath())
        self.__cur = self.__getConnection().cursor()