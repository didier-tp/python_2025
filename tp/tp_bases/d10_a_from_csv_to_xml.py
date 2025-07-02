import csv

input_file_name="films.csv"

film_xml_str_list=[]

def escapeXml( str_xml: str ):
    str_xml = str_xml.replace("&", "&amp;")
    str_xml = str_xml.replace("<", "&lt;")
    str_xml = str_xml.replace(">", "&gt;")
    str_xml = str_xml.replace("\"", "&quot;")
    str_xml = str_xml.replace("'", "&apos;")
    return str_xml

with open(input_file_name, mode='r') as file_to_read:
    # Reading the CSV file
    csv_reader = csv.reader(file_to_read,delimiter=';')
    
    # Skipping the header (uncomment or comment if needed)
    next(csv_reader)  

    # Displaying the contents of the CSV file and build actor_movies_dict_list:
    for line in csv_reader:
        film_xml_str_list.append ( f"<film titre='{escapeXml(line[0])}' date='{line[1]}' realisateur='{escapeXml(line[2])}' acteurs='{escapeXml(line[3])}' />")
       
     
with open("films.xml","wt") as f:
    f.write("<films>\n")
    for film_xml_str in film_xml_str_list:
        print(film_xml_str)
        f.write(f"\t{film_xml_str}\n")
    f.write("</films>")
    
  

