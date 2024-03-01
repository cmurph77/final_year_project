import xml.etree.ElementTree as ET

def calculate_average_travel_time(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        total_travel_time = 0
        num_vehicles = 0

        for vehicle in root.findall('vehicle'):
            depart = float(vehicle.get('depart'))
            arrival = float(vehicle.get('arrival'))
            travel_time = arrival - depart
            total_travel_time += travel_time
            num_vehicles += 1

        if num_vehicles > 0:
            average_travel_time = total_travel_time / num_vehicles
            return average_travel_time
        else:
            return 0
    except FileNotFoundError:
        print("Error: File not found.")

filename = input("Enter the filename: ")
average_travel_time = calculate_average_travel_time(filename)
if average_travel_time is not None:
    print("Average Travel Time:", average_travel_time)
