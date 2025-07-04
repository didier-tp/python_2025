import re # expressions regulieres
def camel_to_snake_case(s):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()

s1="unChameauAvecDesBossesPourChaqueMajuscule"
s2 = camel_to_snake_case(s1)
print("en snake_case:",s2)

def camel_to_snake_decorator(func):
    def wrapperFunction(*args,**kwargs):
        stringRes=func(*args,**kwargs)
        if len(stringRes)>0:
            stringRes=camel_to_snake_case(stringRes)
        return stringRes
    return wrapperFunction

liste_phrases_avec_bosses = [
    "JeVeuxMaMaman",
    "PythonQueJaime",
    "PhraseQuiVaBien"
]

def encadrer1(chaine):
    return f">>>{chaine}<<<"

@camel_to_snake_decorator
def encadrer2(chaine):
    return f">>>{chaine}<<<"

print([encadrer1(p) for p in liste_phrases_avec_bosses])
print([encadrer2(p) for p in liste_phrases_avec_bosses])