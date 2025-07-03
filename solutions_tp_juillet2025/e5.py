from e3_Compte import Compte
########## utilisation de e3_Compte avec nouvelle méthode de classe auto_incr_num()

c1=Compte(1,"compte_a",50.0)
print("c1=",c1)

c12=Compte(12,"compte_b",50.0)
print("c12=",c12)

nouveau_compte_c = Compte( Compte.auto_incr_num() ,"compte_c",120.0)
print("nouveau_compte_c=",nouveau_compte_c)

c3=Compte(3,"compte_c3",60.0)
print("c3=",c3)

nouveau_compte_d = Compte( Compte.auto_incr_num() ,"compte_d",20.0)
print("nouveau_compte_d=",nouveau_compte_d)

