import xml.etree.ElementTree as ET

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    edge_lengths = {}

    for edge in root.findall('edge'):
        edge_id = edge.attrib['id']
        lane = edge.find('lane')
        if lane is not None:
            length = float(lane.attrib['length'])
            edge_lengths[edge_id] = length

    return edge_lengths

def main():
    xml_file = 'random_20.net.xml'  # Replace 'your_xml_file.xml' with the path to your XML file
    edge_lengths = parse_xml(xml_file)
    print(edge_lengths)
    for edge,length in edge_lengths.items():
        print(str(edge) + "  " + str(length))

if __name__ == "__main__":
    main()
