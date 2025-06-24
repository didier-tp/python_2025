from sqlalchemy import create_engine , text
from sqlalchemy import MetaData
from sqlalchemy import Integer, String, Column, Table

metadata_object=MetaData()

region_table = Table(
     "region",
     metadata_object,
     Column('num', String(8), primary_key=True),
     Column('nom', String(64)),
     Column('chef_lieu', String(32))
)

departement_table = Table(
     "departement",
     metadata_object,
     Column('numero', String(6), primary_key=True),
     Column('nom', String(48)),
     Column('population',Integer),
     Column('superficie',Integer),
     Column('prefecture', String(48)),
     Column('ref_region', String(6))
)


'''
Valid SQLite URL forms are:
 sqlite:///:memory: (or, sqlite://)
 sqlite:///relative/path/to/file.db
 sqlite:////absolute/path/to/file.db
'''

db_name="geoDB"
db_url=f"sqlite:///./{db_name}"
engine = create_engine(db_url)

# emitting DDL
#metadata_object.create_all(engine)

with engine.connect() as cnx:
    with open("init_geoDB_sqlite.sql") as file:
        for ligne in file:
            query = text(ligne)
            cnx.execute(query)
    cnx.commit()