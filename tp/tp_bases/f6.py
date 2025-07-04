import re # expressions regulieres

def camel_to_snake_case(s):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()

s1="unChameauAvecDesBossesPourChaqueMajuscule"

s2 = camel_to_snake_case(s1)
print("en snake_case:",s2)


def camel_to_snake_decorator(func):
    def wrapperFunction(*args,**kwargs):
        res=func(*args,**kwargs)
        res=camel_to_snake_case(res)
        return res
    return wrapperFunction

def encadrer1(chaine):
    return f">>>{chaine}<<<"

@camel_to_snake_decorator
def encadrer2(chaine):
    return f">>>{chaine}<<<"

liste_phrases_avec_bosses = [
"JeVeuxMaMaman",
"PythonQueJaime",
"PhraseQuiVaBien"
]

for p in liste_phrases_avec_bosses:
    print("avec encadrer1: " , encadrer1(p))
    print("avec encadrer2: " , encadrer2(p))