#se connecter à une base de données et y créer les tables nécessaires:
from h1_db_params import my_db_sql_alchemy_engine,my_db_url
from h1_metadata import metadata_object , compte_table

metadata_object.create_all(my_db_sql_alchemy_engine)
# ce code python déclenche des ordres CREATE_TABLE