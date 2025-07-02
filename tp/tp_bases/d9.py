
import json


input_file_name="films.json"
output_file_name="stats_films.json"

actor_movies_map={} #map/dict of dicts
# { 'a1' : [ 'm1' ,'m2'] , 'a2' : [ 'm3', m1'] }


def actor_movies_list_in_map(actor):
    movies=actor_movies_map.get(actor)
    if movies==None:
        movies= []
        actor_movies_map[actor]=movies
    return movies

with open(input_file_name,"rt") as f :
	fileContentAsJsonString=f.read()
	films = json.loads(fileContentAsJsonString)
	print("films=",films) #as list of dict:
    
for film in films:
    #print("film=",film)
    acteurs=film['acteurs'].split(',')
    for actor in acteurs:
        movies_list=actor_movies_list_in_map(actor.strip())
        movies_list.append(film.get('titre'))

#print("actor_movies_map=",actor_movies_map)        

def as_actor_movies_dict_list():
    list_of_actor_movies_dict=[]
    # [ { 'acteur': 'a1', 'principaux_films': ['m1','m2']}]
    for a,movies in actor_movies_map.items():
        list_of_actor_movies_dict.append({ 'acteur' : a , 'principaux_films': ", ".join(movies) })
    return list_of_actor_movies_dict


actor_movies_dict_list=as_actor_movies_dict_list()
#print("actor_movies_dict_list=",actor_movies_dict_list)   
acteursStatsAsJsonString = json.dumps(actor_movies_dict_list,indent=4);
#print("acteursStatsAsJsonString=",acteursStatsAsJsonString)
with open(output_file_name,"wt") as f :
	f.write(acteursStatsAsJsonString)     