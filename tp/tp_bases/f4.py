phrases=[
"Bonjour",
"Python est un serpent efficace",
"sans majuscule au debut",
"Ok , tout va bien",
"pasBien car commencant par une minuscule"
]
print("toutes_les_phrases",phrases)

liste_tailles=[  len(p) for p in phrases ]
print("liste_tailles",liste_tailles)

liste_phrases_avec_maj = [p for p in phrases if len(p)>0 and p[0].isupper()  ]
print("liste_phrases_avec_maj",liste_phrases_avec_maj)

liste_tailles_phrases_avec_maj = [len(p) for p in phrases if len(p)>0 and p[0].isupper()  ]
print("liste_tailles_phrases_avec_maj",liste_tailles_phrases_avec_maj)