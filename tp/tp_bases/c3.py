def enchainer_transformation_et_affichage_formate(s, f_trans ,f_format):
	s_tranforme = f_trans(s)
	print(f_format(s_tranforme))
	
def convert_maj(s):
    return s.upper()

def prefixer(s):
    return "**" + s

enchainer_transformation_et_affichage_formate("python",convert_maj,prefixer)  

enchainer_transformation_et_affichage_formate("IleDeFrance",
                                              lambda s:s.lower(),
                                              lambda s : "**"+s+"**") 