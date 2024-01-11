import xml.etree.ElementTree as ET

def insert_tag_within_routes(xml_file_path, new_tag):
    # Parsing the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Finding all <routes> tags in the document
    print("finding routes tag")
    routes_tags = root.findall('routes')

    # Inserting the new tag within each <routes> tag
    for routes_tag in routes_tags:
        # Creating a new element
        new_element = ET.Element(new_tag)
        print("creating a new element")
        # Inserting the new element within the <routes> tag
        routes_tag.insert(len(routes_tag), new_element)

    # Saving the modified XML to a new file
    modified_xml_file_path = xml_file_path.replace('.xml', '_modified.xml')
    tree.write(xml_file_path)
    return xml_file_path


# Path to the XML file
xml_file_path = 'net1.rou.xml'

# Example of a tag to insert

# Running the function
modified_xml_path = insert_tag_within_routes(xml_file_path, new_tag)
modified_xml_path

