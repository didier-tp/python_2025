for l in range(8):
    ligne_etoiles=""
    for c in range(l+1):
        ligne_etoiles+="*"
    print(ligne_etoiles)

# ou bien , plus simplement
ligne_etoiles=""
for l in range(8):
    ligne_etoiles += "*" # ligne_etoiles = ligne_etoiles + "*"
    print(ligne_etoiles)