import xml.etree.ElementTree as ET

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root

def extract_vehicle_data(vehicle):
    depart = float(vehicle.attrib['depart'])
    arrival = float(vehicle.attrib['arrival'])
    travel_time = arrival - depart
    
    vehicle_data = {
        'depart': depart,
        'arrival': arrival,
        'travel_time': travel_time,
        'route': vehicle.find('route').attrib['edges']
    }
    return vehicle_data

def extract_routes(xml):
    routes = {}
    for vehicle in xml.findall('vehicle'):
        vehicle_id = int(vehicle.attrib['id'])
        vehicle_id = vehicle.attrib['id']
        try:
            vehicle_id_integer = int(vehicle_id)
            # Now vehicle_id_integer holds the integer value of vehicle_id
        except ValueError:
            print("Error: vehicle_id is not a valid integer")

        routes[vehicle_id] = extract_vehicle_data(vehicle)
    return routes

def compare_routes(xml1, xml2):
    routes1 = extract_routes(xml1)
    routes2 = extract_routes(xml2)
    # routes1 = sorted(routes1, key=lambda x: x['id'])

    print(routes1)

    common_vehicles = set(routes1.keys()).intersection(routes2.keys())
    different_routes = []

    for vehicle_id in common_vehicles:
        if routes1[vehicle_id] != routes2[vehicle_id]:
            different_routes.append(vehicle_id)

    return different_routes

if __name__ == "__main__":
    file1 = "out_5_a.xml"
    file2 = "out_5_d.xml"

    xml1 = parse_xml(file1)
    xml2 = parse_xml(file2)

    different_routes = compare_routes(xml1, xml2)

    if different_routes:
        print("Different routes found for vehicles:", different_routes)
    else:
        print("Routes are the same in both XML files.")
