DROP TABLE IF EXISTS departement;
DROP TABLE IF EXISTS region;

CREATE TABLE region( num VARCHAR(8) PRIMARY KEY,nom VARCHAR(64) ,chef_lieu VARCHAR(32)) ;
CREATE TABLE departement(numero VARCHAR(6) PRIMARY KEY,nom VARCHAR(48) ,population INTEGER,	superficie INTEGER,	prefecture VARCHAR(48),	ref_region VARCHAR(8),FOREIGN KEY (ref_region) REFERENCES region(num));

INSERT INTO region(num, nom , chef_lieu ) VALUES ("FR-IDF", "Ile-de-France" , "Paris");
INSERT INTO region(num, nom , chef_lieu ) VALUES  ("FR-HDF", "Hauts-de-France" , "Lille" );
INSERT INTO region(num, nom , chef_lieu ) VALUES  ("FR-NOR", "Normandie","Rouen");
INSERT INTO region(num, nom , chef_lieu ) VALUES  ("FR-BRE", "Bretagne" , "Rennes");
INSERT INTO region(num, nom , chef_lieu ) VALUES  ("FR-NAQ", "Nouvelle-Aquitaine" , "Bordeaux" );
INSERT INTO region(num, nom , chef_lieu ) VALUES  ("FR-OCC", "Occitanie","Toulouse");
INSERT INTO region(num, nom , chef_lieu ) VALUES  ("FR-PDL", "Pays-de-la-Loire" , "Nantes" );
INSERT INTO region(num, nom , chef_lieu ) VALUES  ("FR-PAC", "Provence-Alpes-Cote-Azur","Marseille");
INSERT INTO region(num, nom , chef_lieu ) VALUES  ("FR-CVL", "Centre-Val-de-Loire" , "Orleans");
INSERT INTO region(num, nom , chef_lieu ) VALUES  ("FR-GES", "Grand-Est" , "Strasbourg" );
INSERT INTO region(num, nom , chef_lieu ) VALUES  ("FR-ARA", "Auvergne-Rhone-Alpes" , "Lyon");
INSERT INTO region(num, nom , chef_lieu ) VALUES  ("FR-BFC", "Bourgogne-Franche-Comte" , "Dijon" );
INSERT INTO region(num, nom , chef_lieu ) VALUES  ("FR-COR", "Corse","Ajaccio");
												
INSERT INTO departement(numero, nom , prefecture , population , superficie,  ref_region )  VALUES ("75", "Paris" , "Paris" ,2220445 ,105, "FR-IDF");
INSERT INTO departement(numero, nom , prefecture , population , superficie,  ref_region )  VALUES ("92", "Hauts-de-Seine" , "Nanterre",1597770, 176 , "FR-IDF");
INSERT INTO departement(numero, nom , prefecture , population , superficie,  ref_region )  VALUES ("78", "Yvelines" , "Versailles" ,1421670 ,2284, "FR-IDF");
INSERT INTO departement(numero, nom , prefecture , population , superficie,  ref_region )  VALUES ("93", "Seine-Saint-Denis" , "Bobigny", 1571028, 236 , "FR-IDF");
INSERT INTO departement(numero, nom , prefecture , population , superficie,  ref_region )  VALUES ("95", "Val-d-Oise" , "Cercy-Pontoise" ,1205539 ,1246, "FR-IDF");
INSERT INTO departement(numero, nom , prefecture , population , superficie,  ref_region )  VALUES ("77", "Seine-et-Marne" , "Melun",1377846, 5915 , "FR-IDF");
INSERT INTO departement(numero, nom , prefecture , population , superficie,  ref_region )  VALUES ("91", "Essonne" , "Evry" ,1268228 ,1804, "FR-IDF");
INSERT INTO departement(numero, nom , prefecture , population , superficie,  ref_region )  VALUES ("94", "Val-de-Marne" , "Creteil",1365039, 245 , "FR-IDF");
INSERT INTO departement(numero, nom , prefecture , population , superficie,  ref_region )  VALUES ("59", "Nord" , "Lille" ,2603472, 5743 , "FR-HDF");
INSERT INTO departement(numero, nom , prefecture , population , superficie,  ref_region )  VALUES ("62", "Pas de calais" , "Arras", 1472589,6671 , "FR-HDF");
INSERT INTO departement(numero, nom , prefecture , population , superficie,  ref_region )  VALUES ("60", "Oise" , "Beauvais" ,818380,5860 , "FR-HDF");
INSERT INTO departement(numero, nom , prefecture , population , superficie,  ref_region )  VALUES ("80", "Somme" , "Amiens" ,571632 ,6170, "FR-HDF");
INSERT INTO departement(numero, nom , prefecture , population , superficie,  ref_region )  VALUES ("02", "Aisne" , "Laon" ,539783 ,7369, "FR-HDF");
INSERT INTO departement(numero, nom , prefecture , population , superficie,  ref_region )  VALUES ("27", "Eure" , "Evreux" ,598347, 6040 , "FR-NOR");
INSERT INTO departement(numero, nom , prefecture , population , superficie,  ref_region )  VALUES ("76", "Seine-Maritime" , "Rouen", 1257920,6278 , "FR-NOR");
INSERT INTO departement(numero, nom , prefecture , population , superficie,  ref_region )  VALUES ("14", "Calvados" , "Caen" ,691670,5548 , "FR-NOR");
INSERT INTO departement(numero, nom , prefecture , population , superficie,  ref_region )  VALUES ("61", "Orne" , "Alençon" ,287750 ,6103, "FR-NOR");
INSERT INTO departement(numero, nom , prefecture , population , superficie,  ref_region )  VALUES ("50", "Manche" , "Saint-Lo" ,499958 ,5938, "FR-NOR");
			 
SELECT * FROM region;	
SELECT * FROM departement;


