import shutil 
import os

source_path = "example.xml"
destination_path ="example2.xml"

dest = shutil.copy(source_path, destination_path)
#shutil.copymode(source_path, destination_path) 

# Print path of newly created file 
print("Destination path:", dest) 
