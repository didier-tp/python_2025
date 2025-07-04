from sqlalchemy import text,insert
from h1_db_params import my_db_sql_alchemy_engine,my_db_url
from h1_metadata import metadata_object , compte_table


with my_db_sql_alchemy_engine.begin() as cnx:
    #req_insert_compte="INSERT INTO compte (numero,label,solde) VALUES(2,'comptezz',60.0)"
    #req_insert_compte="INSERT INTO compte (label,solde) VALUES('comptezz',60.0)"
    #insert_statement=text(req_insert_compte)
    #res= cnx.execute(insert_statement)
    
    insert_stmt = insert(compte_table).values(label='compteXyz', solde=70.0)
    res=cnx.execute(insert_stmt)
    auto_incr_pk=res.inserted_primary_key[0] # ici pk avec une seule colonne
    print("numero du compte ajouté =", auto_incr_pk )