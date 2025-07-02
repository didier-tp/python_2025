import csv

input_file_name="films.csv"
output_file_name="stats_films.csv"
input_field_names = ["titre","date","realisateur","acteurs"]
output_field_names = ["acteur","principaux_films"]

actor_movies_map={} #map/dict of dicts
# { 'a1' : [ 'm1' ,'m2'] , 'a2' : [ 'm3', m1'] }


def actor_movies_list_in_map(actor):
    movies=actor_movies_map.get(actor)
    if movies==None:
        movies= []
        actor_movies_map[actor]=movies
    return movies

with open(input_file_name, mode='r') as file_to_read:
    # Reading the CSV file
    csv_reader = csv.reader(file_to_read,delimiter=';')
    
    # Skipping the header (uncomment or comment if needed)
    next(csv_reader)  

    # Displaying the contents of the CSV file and build actor_movies_dict_list:
    for line in csv_reader:
        print(line)
        str_liste_acteurs = line[3]
        titre_film=line[0]
        acteurs=str_liste_acteurs.split(',')
        for actor in acteurs:
            movies_list=actor_movies_list_in_map(actor.strip())
            movies_list.append(titre_film)

#print("actor_movies_map=",actor_movies_map)
  

def as_actor_movies_dict_list():
    list_of_actor_movies_dict=[]
    # [ { 'acteur': 'a1', 'principaux_films': ['m1','m2']}]
    for a,movies in actor_movies_map.items():
        list_of_actor_movies_dict.append({ 'acteur' : a , 'principaux_films': ", ".join(movies) })
    return list_of_actor_movies_dict


actor_movies_dict_list=as_actor_movies_dict_list()
#print("actor_movies_dict_list=",actor_movies_dict_list)

with open(output_file_name, 'w', newline='') as csvfile:
    # Creating a CSV DictWriter object
    writer = csv.DictWriter(csvfile, fieldnames=output_field_names, delimiter=";")
    
    writer.writeheader()# Writing headers (field names)
    writer.writerows(actor_movies_dict_list)# Writing data rows 