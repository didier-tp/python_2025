#pip install sqlalchemy 
# est nécessaire soit au niveau global , soit au niveau .venv
from sqlalchemy import create_engine 
my_db_name="minibank_db"

my_db_url_sqlite=f"sqlite:///./{my_db_name}"

my_db_url_mysql=f"..."

# pour ce connecter à postgres , besoin de pip install psycopg2
# en plus de pip install sqlalchemy
#postgresql+psycopg2://user:password@hostname/database_name (default port = 5432)
my_db_url_posgres=f"postgresql+psycopg2://postgres:root@localhost/{my_db_name}"

my_db_url=my_db_url_sqlite  # ou bien url mysql ou autre (ex : postgres)
#my_db_url=my_db_url_posgres

my_db_sql_alchemy_engine = create_engine(my_db_url)