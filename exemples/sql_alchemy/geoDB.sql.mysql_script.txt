# script SQL pour mySql
#DROP DATABASE IF EXISTS geoDB;
#CREATE DATABASE geoDB;

CREATE DATABASE IF NOT EXISTS geoDB ;

USE geoDB;

# DROP TABLE Dans ordre inverse des CREATE TABLE et/ou INSERT INTO si FOREIGN KEY CONSTRAINTS
DROP TABLE IF EXISTS Departement;
DROP TABLE IF EXISTS Region;


CREATE TABLE Region( 
    num VARCHAR(8) PRIMARY KEY,
	nom VARCHAR(64) ,
	chef_lieu VARCHAR(32)
) ENGINE=InnoDB;
# via des quotes inversees , un nom de tables ou de colonne pourrait comporter
# des espaces ex `chef lieu`


CREATE TABLE Departement( 
    numero VARCHAR(6) PRIMARY KEY,
	nom VARCHAR(48) ,
	population INTEGER,
	superficie INTEGER,
	prefecture VARCHAR(48),
	refRegion VARCHAR(8)
)ENGINE=InnoDB;

ALTER TABLE Departement
 ADD CONSTRAINT FK_RegionValidePourDepartement
  FOREIGN KEY (refRegion) REFERENCES Region(num) ;

# show tables est une instruction MySql qui affiche la liste des tables
show tables;

INSERT INTO Region(num, nom , chef_lieu ) 
VALUES ("FR-IDF", "Ile-de-France" , "Paris"),
  ("FR-HDF", "Hauts-de-France" , "Lille" ),
  ("FR-NOR", "Normandie","Rouen"),
  ("FR-BRE", "Bretagne" , "Rennes"),
  ("FR-NAQ", "Nouvelle-Aquitaine" , "Bordeaux" ),
  ("FR-OCC", "Occitanie","Toulouse"),
  ("FR-PDL", "Pays-de-la-Loire" , "Nantes" ),
  ("FR-PAC", "Provence-Alpes-Cote-Azur","Marseille"),
  ("FR-CVL", "Centre-Val-de-Loire" , "Orleans"),
  ("FR-GES", "Grand-Est" , "Strasbourg" ),
  ("FR-ARA", "Auvergne-Rhone-Alpes" , "Lyon"),
  ("FR-BFC", "Bourgogne-Franche-Comte" , "Dijon" ),
  ("FR-COR", "Corse","Ajaccio");
												
INSERT INTO Departement(numero, nom , prefecture , population , superficie,  refRegion ) 
      VALUES ("75", "Paris" , "Paris" ,2220445 ,105, "FR-IDF"),
	         ("92", "Hauts-de-Seine" , "Nanterre",1597770, 176 , "FR-IDF"),
			 ("78", "Yvelines" , "Versailles" ,1421670 ,2284, "FR-IDF"),
	         ("93", "Seine-Saint-Denis" , "Bobigny", 1571028, 236 , "FR-IDF"),
			 ("95", "Val-d-Oise" , "Cercy-Pontoise" ,1205539 ,1246, "FR-IDF"),
	         ("77", "Seine-et-Marne" , "Melun",1377846, 5915 , "FR-IDF"),
			 ("91", "Essonne" , "Evry" ,1268228 ,1804, "FR-IDF"),
	         ("94", "Val-de-Marne" , "Creteil",1365039, 245 , "FR-IDF"),
	         ("59", "Nord" , "Lille" ,2603472, 5743 , "FR-HDF"),
             ("62", "Pas de calais" , "Arras", 1472589,6671 , "FR-HDF"),
			 ("60", "Oise" , "Beauvais" ,818380,5860 , "FR-HDF"),
			 ("80", "Somme" , "Amiens" ,571632 ,6170, "FR-HDF"),
			 ("02", "Aisne" , "Laon" ,539783 ,7369, "FR-HDF"),
			 ("27", "Eure" , "Evreux" ,598347, 6040 , "FR-NOR"),
             ("76", "Seine-Maritime" , "Rouen", 1257920,6278 , "FR-NOR"),
			 ("14", "Calvados" , "Caen" ,691670,5548 , "FR-NOR"),
			 ("61", "Orne" , "Alençon" ,287750 ,6103, "FR-NOR"),
			 ("50", "Manche" , "Saint-Lo" ,499958 ,5938, "FR-NOR");
			 
			 
			 
# cette insertion devrait être refusée (region "FR-99" existe pas):			 
#INSERT INTO Departement(numero, nom , prefecture , refRegion ) 
#      VALUES ("AA", "ABC" , "XYZ" , "FR-99");			 
												
# affichage de la structure pour verifier:
#describe Region;
#describe Departement;

# affichage des donnees pour verifier:
SELECT * FROM Region;	
SELECT * FROM Departement;

#ajout , modification et  suppression Region inconnue:
INSERT INTO Region(num, nom , chef_lieu ) VALUES ("FR-XYZ", "Region-inconnue" , "???");	
UPDATE Region SET nom="Region-perdue" WHERE num="FR-XYZ" ;
DELETE FROM Region WHERE num="FR-XYZ";

#population et superficie des regions ayant au plus 5 departements:
SELECT refRegion , SUM(population) , SUM(superficie) FROM Departement GROUP BY refRegion HAVING Count(*) <=5;									

#jointure entre Region et Departement avec tri selon region en ordre decroissant:
SELECT Departement.nom , Region.nom FROM Departement INNER JOIN Region ON Departement.refRegion = Region.num ORDER BY Region.nom DESC;


