-- On préférera stocker les dates comme un epoch Unix, c'est-à-dire un nombre de secondes écoulées depuis une date connue (en l'occurence le 1 Janvier 1970 à 0h UTC)
-- Ce type de stockage rend les calculs sur les dates et les écarts de date plus simple

-- On ajoute des drops au début du fichier SQL car cette base de données n'a pas un objectif de production mais d'apprentissage ainsi si on efface les données
-- à chaque fois que l'on fait des modifications sur celle-ci ce n'est pas très grave. C'est evidemment une mauvaise pratique du développement puisqu'on ne drop jamais de table
-- normalement
DROP TABLE louer;
DROP TABLE client;
DROP TABLE salle;
DROP TABLE organisme;

CREATE TABLE organisme
(codeOrganisme INTEGER NOT NULL ,
nomOrganisme CHAR(25),
codeNumAgrement INTEGER NOT NULL,
CONSTRAINT pk_nomOrganisme PRIMARY KEY (codeOrganisme));

CREATE TABLE salle
(codeSalle INTEGER NOT NULL,
nomSalle CHAR(25),
prixSalle INTEGER NOT NULL DEFAULT 0,
CONSTRAINT pk_codeSalle PRIMARY KEY (codeSalle));

CREATE TABLE client
(codeClient INTEGER NOT NULL,
nomClient CHAR (50),
adresseClient CHAR(250),
dateDeNaissance INTEGER,
codeOrganisme INTEGER NOT NULL,
CONSTRAINT pk_codeClient PRIMARY KEY (codeClient),
CONSTRAINT fk_codeOrganisme FOREIGN KEY (codeOrganisme) REFERENCES organisme(codeOrganisme));

CREATE TABLE louer
(dateLocationDebut INTEGER NOT NULL,
dateLocationFin INTEGER NOT NULL,
codeSalle INTEGER NOT NULL,
codeOrganisme INTEGER NOT NULL,
codeClient INTEGER NOT NULL,
CONSTRAINT pk_louer PRIMARY KEY (codeSalle, codeOrganisme, codeClient),
CONSTRAINT fk_codeSalle FOREIGN KEY (codeSalle) REFERENCES salle(codeSalle),
CONSTRAINT fk_codeOrganisme FOREIGN KEY (codeOrganisme) REFERENCES organisme(codeOrganisme),
CONSTRAINT fk_codeClient FOREIGN KEY (codeClient) REFERENCES client(codeClient));