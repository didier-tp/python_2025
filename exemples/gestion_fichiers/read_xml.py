import xml.etree.ElementTree as ET

# Parse the XML file

tree = ET.parse('example.xml')
# Get the root element
root = tree.getroot()

# Iterate through each child of the root element
for child in root:
    # Print the tag and attributes of each child element
    print(child.tag, child.attrib)