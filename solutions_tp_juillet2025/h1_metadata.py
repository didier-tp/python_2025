from sqlalchemy import MetaData
from sqlalchemy import Integer, String, Column, Table , Float

metadata_object=MetaData()

compte_table = Table(
     "compte",
     metadata_object,
     Column('numero', Integer, primary_key=True , autoincrement=True),
     Column('label', String(64)),
     Column('solde', Float())
)

