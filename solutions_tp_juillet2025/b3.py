liste = [ "rouge" , "vert" , "bleu" , "rouge" , "vert"]
color_set = set(liste)
print("color_set=",color_set , " type = " , type(color_set))

color_set2 = { "jaune" , "vert" , "orange"}
allcolor_set = color_set.union(color_set2)
print("allcolor_set=",allcolor_set)

jour_set = { "erreur", "lundi" , "mardi" , "mercredi" , "jeudi"}
jour_set.discard("erreur")
jour_set.add("vendredi")
print("jour_set=",jour_set)
jour_set.update({"samedi" , "dimanche"})
print("jour_set=",jour_set)
jour_set.clear()
print("jour_set=",jour_set)