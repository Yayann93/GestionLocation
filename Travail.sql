CREATE TABLE organisme
(codeOrganisme INTEGER NOT NULL,
nomOrganisme CHAR(25),
codeNumAgrement INTEGER NOT NULL,
CONSTRAINT pk_nomOrganisme PRIMARY KEY (codeNomOrganisme));

CREATE TABLE salle
(codeSalle INTEGER NOT NULL,
nomSalle CHAR(25),
prixSalle CHAR (10),
CONSTRAINT pk_nomSalle PRIMARY KEY (nomSalle));

CREATE TABLE client
(codeClient INTEGER NOT NULL,
nomClient CHAR (50),
adresseClient CHAR (50),
dateDeNaissance DATE,
nomOrganisme CHAR (25),
CONSTRAINT pk_nomClient PRIMARY KEY (nomClient),
CONSTRAINT fk_nomOrganisme FOREIGN KEY (nomOrganisme) REFERENCES organisme(nomOrganisme));

CREATE TABLE louer
(dateLocation DATE NOT NULL,
nomSalle CHAR(25),
nomOrganisme INTEGER NOT NULL,
nomClient CHAR (50),
CONSTRAINT fk_nomSalle FOREIGN KEY (nomSalle) REFERENCES salle(nomSalle),
CONSTRAINT fk_nomOrganisme FOREIGN KEY (nomOrganisme) REFERENCES organisme(nomOrganisme),
CONSTRAINT fk_nomClient FOREIGN KEY (nomClient) REFERENCES client(nomClient));