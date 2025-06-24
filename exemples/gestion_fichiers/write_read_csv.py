import csv

file_name="produits.csv"

field_names = ["ref","label","prix"]

data_dict_list = [
   { 'ref':1 , 'label' : "cahier" , 'prix' : 4.2},
   { 'ref':2 , 'label' : "stylo" , 'prix' : 2.2},
   { 'ref':3 , 'label' : "classeur" , 'prix' : 5.2},
   { 'ref':4 , 'label' : "gomme" , 'prix' : 3.2}
]

with open(file_name, 'w', newline='') as csvfile:
    # Creating a CSV DictWriter object
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    
    writer.writeheader()# Writing headers (field names)
    writer.writerows(data_dict_list)# Writing data rows

############################
######## relecture

# Opening the CSV file
with open(file_name, mode='r') as file_to_read:
    # Reading the CSV file
    csv_reader = csv.reader(file_to_read)
    
    # Skipping the header (uncomment or comment if needed)
    next(csv_reader)  

    # Displaying the contents of the CSV file
    for line in csv_reader:
        print(line)