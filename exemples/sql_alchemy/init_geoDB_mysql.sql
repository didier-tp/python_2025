CREATE DATABASE IF NOT EXISTS geoDB ;
USE geoDB;

DROP TABLE IF EXISTS departement;
DROP TABLE IF EXISTS region;


CREATE TABLE region( 
    num VARCHAR(8) PRIMARY KEY,
	nom VARCHAR(64) ,
	chef_lieu VARCHAR(32)
) ENGINE=InnoDB;



CREATE TABLE departement( 
    numero VARCHAR(6) PRIMARY KEY,
	nom VARCHAR(48) ,
	population INTEGER,
	superficie INTEGER,
	prefecture VARCHAR(48),
	ref_region VARCHAR(8)
)ENGINE=InnoDB;

ALTER TABLE departement
 ADD CONSTRAINT FK_RegionValidePourDepartement
  FOREIGN KEY (ref_region) REFERENCES region(num) ;


INSERT INTO region(num, nom , chef_lieu ) 
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
												
INSERT INTO departement(numero, nom , prefecture , population , superficie,  ref_region ) 
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
			 
SELECT * FROM region;	
SELECT * FROM departement;


