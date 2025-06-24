restrictions sur script sql pour sqlite:
--------------------------------------
pas d'execution du script/fichier complet , mais execution logne par ligne
pas de alter table ... add constraint ... mais foreign key (...) des le create table .
----
PRAGMA est un mot clef supporté par sqlite et qui permet de lancer des instructions très spécifiques
exemple: 
-- Activer les clés étrangères pour l'intégrité des données
PRAGMA foreign_keys = ON;