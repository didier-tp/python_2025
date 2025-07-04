from h1_db_params import my_db_name, my_db_url , my_db_sql_alchemy_engine
from h1_metadata import metadata_object

# emitting DDL :
metadata_object.create_all(my_db_sql_alchemy_engine)
print(f"database {my_db_url} initialized")