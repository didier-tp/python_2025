# listes en comprehension
phrases=[
    "Bonjour",
    "Python est un serpent efficace",
    "sans majuscule au debut",
    "Ok , tout va bien",
    "pasBien car commencant par une minuscule"
]
print("toutes_les_phrases",phrases)

tailles_de_toutes_les_phrases = [ len(p) for p in phrases]
print("tailles_de_toutes_les_phrases",tailles_de_toutes_les_phrases)

phrases_avec_majuscules = [ p for p in phrases if  p[0].isupper()]
print("phrases_avec_majuscules",phrases_avec_majuscules)

tailles_phrases_majuscules = [ len(p) for p in phrases if  p[0].isupper()]
print("tailles_phrases_majuscules",tailles_phrases_majuscules)