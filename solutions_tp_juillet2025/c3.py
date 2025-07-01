def enchainer_transformation_et_affichage_formate(s, f_trans ,f_format):
	s_tranforme = f_trans(s)
	print(f_format(s_tranforme))
	
enchainer_transformation_et_affichage_formate("bonjour" ,
											  lambda s : s.upper() ,
											  lambda s : "** " + s + " **")   

enchainer_transformation_et_affichage_formate("Hello" ,
											  lambda s : s.lower() ,
											  lambda s : ">>> " + s ) 

enchainer_transformation_et_affichage_formate("cba" ,
											  lambda s : ''.join(reversed(s)) ,
											  lambda s : "[" + s + "]") 
