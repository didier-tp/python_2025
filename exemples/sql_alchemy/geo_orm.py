from sqlalchemy import String , create_engine , select
from sqlalchemy.orm import DeclarativeBase , Mapped , mapped_column
from sqlalchemy.orm import Session 

#######   Definition d'une classe d'objet persistant (Modèle structurel / partie de l'ORM)

class Base(DeclarativeBase):
   pass

class Departement(Base):
    __tablename__ = "departement"
   
    numero: Mapped[str] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(48))
    population: Mapped[int]
    superficie: Mapped[int]
    prefecture: Mapped[str]

    def __str__(self) :
        return f"Departement(numero={self.numero}, nom={self.nom}, population={self.population}, superficie={self.superficie} ,prefecture={self.prefecture})"

############## engine , connexion, ...

username="root"
pwd="root"
db_hostname="localhost"
db_name="geoDB"
db_url=f"mysql+mysqldb://{username}:{pwd}@{db_hostname}:3306/{db_name}"
#engine = create_engine(db_url)

engine = db_url=f"sqlite:///./{db_name}"
#engine = create_engine(db_url,echo=True) # avec affichage des requêtes déclenchées
engine = create_engine(db_url)


######  CRUD

### first session (add):

with Session(engine) as session:
    dep57=Departement(numero=57,nom="Moselle",prefecture="Metz")
    session.add(dep57)
    session.commit() # with a subcall to session.flush()


### second session (reload and update):
with Session(engine) as session:

    select_dep57_st=select(Departement).where(Departement.numero == "57")
    dep57_relu=session.scalars(select_dep57_st).one() #return one object or an exception
    print("after add , before update ,dep57_relu=",dep57_relu)

    dep57_relu.population=1049942
    dep57_relu.superficie=6216
    session.commit() #for update # with a subcall to session.flush()


### third session (delete):
with Session(engine) as session:

    select_dep57_st=select(Departement).where(Departement.numero == "57")
    dep57_relu=session.scalars(select_dep57_st).one() #return one object or an exception
    print("after update,before delete, dep57_relu=",dep57_relu)

    session.delete(dep57)
    session.commit() # with a subcall to session.flush()


    #select_dep57_st=select(Departement).where(Departement.numero == "57")
    nb_dep57_after_delete=len(session.scalars(select_dep57_st).all())
    print("nb_dep57_after_delete=",nb_dep57_after_delete)
