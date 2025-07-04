from sqlalchemy import text
from h1_db_params import my_db_sql_alchemy_engine,my_db_url
from h1_metadata import metadata_object , compte_table


with my_db_sql_alchemy_engine.begin() as cnx:
    req_insert_compte="INSERT INTO compte (numero,label,solde) VALUES(1,'comptexy',50.0)"
    insert_statement=text(req_insert_compte)
    cnx.execute(insert_statement)