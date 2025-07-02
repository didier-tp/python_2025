import xml.etree.ElementTree as ET

input_file_name="films.xml"
output_file_name="stats_films.xml"

actor_movies_map={} #map/dict of dicts
# { 'a1' : [ 'm1' ,'m2'] , 'a2' : [ 'm3', m1'] }


def actor_movies_list_in_map(actor):
    movies=actor_movies_map.get(actor)
    if movies==None:
        movies= []
        actor_movies_map[actor]=movies
    return movies

# Parse the XML file
tree = ET.parse(input_file_name)

# Get the root element
root = tree.getroot()

# Iterate through each child of the root element
for child in root:
    # Print the tag and attributes of each child element
    print(f"<{child.tag}>  with attributes list= {child.attrib}" )
    filmAttrsDict = child.attrib
    #print("filmAttrsDict=",filmAttrsDict)
    acteurs=filmAttrsDict['acteurs'].split(',')
    for actor in acteurs:
        movies_list=actor_movies_list_in_map(actor.strip())
        movies_list.append(filmAttrsDict.get('titre'))

#print("actor_movies_map=",actor_movies_map)        

 
xmlStatsRoot=ET.Element("acteurs")
xmlStatsTree=ET.ElementTree(xmlStatsRoot)   

for a in actor_movies_map.keys() :
    acteurElement=ET.Element("acteur")
    acteurElement.set("nom",a)
    acteurElement.set("principaux_films",", ".join(actor_movies_map[a]))
    xmlStatsRoot.append(acteurElement)

with open(output_file_name,"wb") as f :
	xmlStatsTree.write(f, encoding='utf-8')   