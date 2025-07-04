from e3_Compte import Compte
from sqlalchemy import text , insert , update , delete
from h1_metadata import compte_table

class CompteDao():
    def __init__(self,sqlAlchemyEngine):
        self.engine = sqlAlchemyEngine

    def allComptes(self):
        with self.engine.begin() as cnx:
             select_all_comptes_sql="SELECT * FROM compte"
             results=cnx.execute(text(select_all_comptes_sql)).fetchall() # as list of tuple
             compte_list=[ Compte(c_tuple[0],c_tuple[1],c_tuple[2]) for c_tuple in results ]
             return compte_list #as list of instances of Compte class
        
    def compteByNum(self,num):
        with self.engine.begin() as cnx:
             select_compte_by_num_sql="SELECT * FROM compte WHERE numero = :numero"
             st_params={ 'numero' : num}
             res_tuple=cnx.execute(text(select_compte_by_num_sql),st_params).fetchone() # as  tuple
             compte=Compte(res_tuple[0],res_tuple[1],res_tuple[2]) 
             return compte #as instance of Compte class        

    def insertNewCompte(self, compte):
        with self.engine.begin() as cnx:
            insert_stmt = insert(compte_table).values(label=compte.label, solde=compte.solde)
            res=cnx.execute(insert_stmt)  
            #print("nombre de lignes affectées par insertion:",res.rowcount)
            num_compte=res.inserted_primary_key[0] # ici pk avec une seule colonne 
            #print("num_compte (after auto_increment)=", num_compte )
            compte.numero=num_compte
            return compte # avec auto_incr pk
        
    def updateCompte(self, compte):
        with self.engine.begin() as cnx:
            update_stmt = update(compte_table).values(label=compte.label, solde=compte.solde).where(compte_table.c.numero ==compte.numero)
            cnx.execute(update_stmt)  
            return compte  

    def deleteCompteByNum(self, num):
        with self.engine.begin() as cnx:
            delete_stmt = delete(compte_table).where(compte_table.c.numero == num)
            cnx.execute(delete_stmt)  

    def deleteAllComptes(self):
        with self.engine.begin() as cnx:
            delete_all_comptes_sql="DELETE FROM compte" #without "WHERE ..."
            cnx.execute(text(delete_all_comptes_sql))
