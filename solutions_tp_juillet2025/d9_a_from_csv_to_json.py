import csv
import json

input_file_name="films.csv"

film_dict_list=[]

with open(input_file_name, mode='r') as file_to_read:
    # Reading the CSV file
    csv_reader = csv.reader(file_to_read,delimiter=';')
    
    # Skipping the header (uncomment or comment if needed)
    next(csv_reader)  

    # Displaying the contents of the CSV file and build actor_movies_dict_list:
    for line in csv_reader:
        print(line)
        film_dict_list.append ( { 'titre' : line[0] , 'date' : line[1] , 'realisateur' : line[2] , 'acteurs' : line[3]})
       

#print("actor_movies_map=",actor_movies_map)
filmsAsJsonString = json.dumps(film_dict_list,indent=4);
print("filmsAsJsonString=",filmsAsJsonString)
with open("films.json","wt") as f :
	f.write(filmsAsJsonString)
  

