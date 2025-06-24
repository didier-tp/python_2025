from sqlalchemy import create_engine , text

username="root"
pwd="root"
db_hostname="localhost"
db_name="geoDB"
db_url=f"mysql+mysqldb://{username}:{pwd}@{db_hostname}:3306/{db_name}"
engine = create_engine(db_url)

with engine.connect() as cnx:
    with open("init_geoDB_mysql.sql") as file:
        query = text(file.read())
        cnx.execute(query)
    cnx.commit()

'''
NB: this kind of script not working with sqllite:
ERROR : You can only execute one statement at a time
'''    