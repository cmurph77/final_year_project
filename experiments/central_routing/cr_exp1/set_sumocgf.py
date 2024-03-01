import xml.etree.ElementTree as ET

def set_netfile_value(new_value):
    tree = ET.parse('config.xml')
    root = tree.getroot()

    for input_element in root.iter('input'):
        for netfile_element in input_element.iter('net-file'):
            netfile_element.set('value', new_value)

    tree.write('config.xml')


if __name__ == "__main__":
    
    # Example usage
    new_netfile_value = "new_random_20.net.xml"
    set_netfile_value(new_netfile_value)
    print("Value for net-file attribute has been set to:", new_netfile_value)
