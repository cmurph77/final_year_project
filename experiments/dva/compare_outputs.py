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
    trips1 = extract_routes(xml1)
    trips2 = extract_routes(xml2)
    # trips1 = sorted(trips1, key=lambda x: x['id'])

    for trip_id, trip_data in trips1.items():
        print(trip_id,trip_data)


if __name__ == "__main__":
    file1 = "out_5_a.xml"
    file2 = "out_5_d.xml"

    xml1 = parse_xml(file1)
    xml2 = parse_xml(file2)

    compare_routes(xml1, xml2)

