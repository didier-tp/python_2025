print("via sqlAchemy")
#pip install sqlachemy
from sqlalchemy import create_engine , text
import json

# db_url="database+dialect://username:password@hostname:port/databasename"
# NB: mysql+mysqlconnector works but with some limitations (depending of versions)
# mysql+mysqldb or mysql+pymysql are the classic connexions for mysql 
# mysql+mysqldb required pip install mysqlclient


#db_url="mysql+mysqldb://root:root@localhost:3306/geoDB"
username="root"
pwd="root"
db_hostname="localhost"
db_name="geoDB"
db_url=f"mysql+mysqldb://{username}:{pwd}@{db_hostname}:3306/{db_name}"
#engine = create_engine(db_url)

engine = db_url=f"sqlite:///./{db_name}"
engine = create_engine(db_url)

with engine.begin() as cnx:
    select_all_regions_sql="SELECT * FROM region"
    results=cnx.execute(text(select_all_regions_sql)).fetchall()
    for record in results:
        print(f"region={record}")

  
    insert_request = """insert into departement
             (numero, nom, population, superficie, prefecture)
             values (:numero, :nom, :population, :superficie , :prefecture)"""
    st_params = { "numero" :57 , "nom" : "Moselle" , "population" : 0 , "superficie" : 0, "prefecture" : "Metz"}
    insert_statement = text(insert_request)
    res=cnx.execute(insert_statement,st_params)  
    print("nombre de lignes affectées par insertion:",res.rowcount)

    update_request =  """update departement
             set population=:population, superficie=:superficie
             where numero=:numero""" 
    st_params = { "numero" :57 , "population" : 1049942 , "superficie" : 6216} 
    update_statement = text(update_request)
    res=cnx.execute(update_statement,st_params)
    print("nombre de lignes affectées par update:",res.rowcount)

    #select_all_departements_sql="SELECT * FROM Departement"
    select_all_departements_sql="SELECT numero, nom, population, superficie, prefecture FROM departement"
    results=cnx.execute(text(select_all_departements_sql)).fetchall()
    for record in results:
        #print(f"departement={record}")   #departement=('60', 'Oise', 818380, 5860, 'Beauvais', 'FR-HDF')  
        column_names = ("numero", "nom", "population", "superficie", "prefecture")
        dep_as_dict = dict(zip(column_names,record))  
        #print(dep_as_dict) # {'numero': '60', 'nom': 'Oise', 'population': 818380, 'superficie': 5860, 'prefecture': 'Beauvais'}
        dep_as_json_string = json.dumps(dep_as_dict)
        print (dep_as_json_string) # {"numero": "60", "nom": "Oise", "population": 818380, "superficie": 5860, "prefecture": "Beauvais"}

    delete_request = """delete from departement where numero=57"""
    delete_statement = text(delete_request)
    res=cnx.execute(delete_statement)
    print("nombre de lignes affectées par suppression:",res.rowcount)


    #commit automatique si pas d'exception en fin de bloc with ...as cnx:             
    #fermeture automatique de la connexion en fin de bloc with ...as cnx: