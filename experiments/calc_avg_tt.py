import xml.etree.ElementTree as ET
import csv
import matplotlib.pyplot as plt
import numpy as np
import argparse


# Strores the overal sim results for each trip size
t1_average_tt = []
t2_average_tt = []
same_route_counts = []
same_tt_counts = []

print_results_to_conole = True



def parse_data(data):
    parsed_data = {}
    for entry in data:
        key = list(entry.keys())[0]
        value = list(entry.values())[0]
        parsed_data[key] = value
    return parsed_data


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
       'route': [route.attrib['edges'] for route in vehicle.findall('.//route[@edges]')]
    }
    return vehicle_data

def extract_routes(xml):
    routes = {}
    i = 0
    for vehicle in xml.findall('vehicle'):
        i = i +1
        vehicle_id = int(vehicle.attrib['id'])
        vehicle_id = vehicle.attrib['id']
        try:
            vehicle_id_integer = int(vehicle_id)
            # Now vehicle_id_integer holds the integer value of vehicle_id
        except ValueError:
            print("Error: vehicle_id is not a valid integer")


        routes[vehicle_id] = extract_vehicle_data(vehicle)
    return routes

def create_csv(trips1,output_filename,filename_1,filename_2,trips):
    # Open a CSV file in write mode
    # if print_results_to_conole: print("\nComparing " + filename_1 + " & " + filename_2 + " -> output file: " + output_filename)

        trips1_name = filename_1

        num_trips = len(trips1)
    


        # size 
        # store the total trip times
        trip1_tot_tt = 0;
        trip2_tot_tt = 0;
        same_route_count = 0
        same_tt_count = 0
    

        for i in range(0,(len(trips1))):
            
            # print("i:" + str(trips1[str(i)]))
            # Load in data from the trips1 and 2
            trip1_tt = trips1[str(i)]['travel_time']

            # Update the total trip times
            trip1_tot_tt = trip1_tot_tt + trip1_tt;

  

            
        # store same rout and same time cou


        # Calculate Average Travel Times
        trip1_avg_tt = trip1_tot_tt/num_trips;
        t1_average_tt.append({trips:trip1_avg_tt})

        print("Average Time: " +  str(trip1_avg_tt))


def compare_output_files(output_filename, xml1, filename_1,filename_2,trips):
    trips1 = extract_routes(xml1)
    
    sorted_trips1 = dict(sorted(trips1.items()))
    create_csv(sorted_trips1,output_filename,filename_1,filename_2,trips)

def get_avg(fname):
    file1_name = "astar_tr_reg"
    xml1 = parse_xml(fname)
    file2_name = "cr_tr"
    xml2 = parse_xml(fname)
    output_file_loc = "/Users/cianmurphy/code_directories/final_year_project/experiments/central_routing/test.csv"
    compare_output_files(output_file_loc,xml1,file1_name,file2_name,str(1000))


if __name__ == "__main__":
    print(" \n")
    file = "/Users/cianmurphy/code_directories/final_year_project/experiments/central_routing/cr_exp1/net_001_output_files/cr_1000tr.out.xml"
    avg = get_avg(file)
    print(" \n")








    
    