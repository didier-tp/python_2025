from e3_Compte import Compte
from h1_CompteDao import CompteDao
from h1_db_params import my_db_name, my_db_url , my_db_sql_alchemy_engine

compte_dao = CompteDao(my_db_sql_alchemy_engine)

compte_dao.deleteAllComptes()

c1=Compte(label="compteXyz", solde=50.0)

inserted_c1=compte_dao.insertNewCompte(c1)
print("insertedC1=",inserted_c1)

compte_c1_relu = compte_dao.compteByNum(inserted_c1.numero)
print("compte_c1_relu (after insert)=",compte_c1_relu )

c1=compte_c1_relu
c1.label="compte_xyz"
c1.solde=150.0
updated_c1=compte_dao.updateCompte(c1)

compte_c1_relu = compte_dao.compteByNum(c1.numero)
print("compte_c1_relu (after update)=",compte_c1_relu)

#compte_dao.deleteCompteByNum(compte_c1_relu.numero)

compte_list = compte_dao.allComptes()
print("\nTous les comptes dans la base de données:")
for c in compte_list:
    print(c)

