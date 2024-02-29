# trips = {
#     1: {'depart': 1.0, 'arrival': 73.0, 'travel_time': 72.0, 'route': 'C8C9 C9C8 C8C7 C7C6 C6C5 C5C4 C4C3 C3D3'},
#     2: {'depart': 5.0, 'arrival': 45.0, 'travel_time': 40.0, 'route': 'A2B2 B2B3 B3B4 B4B5 B5B6 B6B7 B7B8 B8B9 B9C9'},
#     3: {'depart': 3.0, 'arrival': 55.0, 'travel_time': 52.0, 'route': 'X1Y1 Y1Z1 Z1Z2 Z2Z3 Z3Z4 Z4Z5 Z5Z6 Z6Z7 Z7Z8 Z8Z9'}
# }
# 
# Example of hwo to access
# 
# trip_id = 1
# travel_time = trips[trip_id]['travel_time']


import xml.etree.ElementTree as ET
import csv

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

def create_csv(trips1,trips2,output_filename,filename_1,filename_2):
    # Open a CSV file in write mode
   print("\nComparing " + filename_1 + " & " + filename_2 + " -> output file: " + output_filename)
   with open(output_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        trips1_name = filename_1
        trips2_name = filename_2

        if len(trips1) != len(trips2):
            print("Error: There is not the same number of trips in both files")

        num_trips = len(trips1)
    

        # Write each row of data to the CSV file
        # write in the header row
        writer.writerow(['id',
                         trips1_name+'_dep',
                         trips2_name+'_dep',
                         trips1_name+'_arr',
                         trips2_name+'_arr',
                         trips1_name+'_route',
                         trips2_name+'_route',
                         trips1_name+'_traveltime',
                         trips2_name+'_traveltime',
                         'same_traveltime?',
                         "same_route?",
                        ])
        # size 
        # store the total trip times
        trip1_tot_tt = 0;
        trip2_tot_tt = 0;

        for i in range(0,(len(trips1))):
            
            # print("i:" + str(trips1[str(i)]))
            # Load in data from the trips1 and 2
            trip1_rou = trips1[str(i)]['route']
            trip2_rou = trips2[str(i)]['route']
            trip1_tt = trips1[str(i)]['travel_time']
            trip2_tt = trips2[str(i)]['travel_time']

            # Update the total trip times
            trip1_tot_tt = trip1_tot_tt + trip1_tt;
            trip2_tot_tt = trip2_tot_tt + trip2_tt;

            # Check is the trip time is the same
            if trip1_tt == trip2_tt:
                same_time = True
            else :
                same_time = False

            # Check if the route is the same
            if (trip1_rou == trip2_rou):
                same_route = True
            else: 
                same_route = False

            # Write the data to a new line
            writer.writerow([i,
                             trips1[str(i)]['depart'],
                             trips2[str(i)]['depart'],
                             trips1[str(i)]['arrival'],
                             trips2[str(i)]['arrival'],
                             trips1[str(i)]['route'],
                             trips2[str(i)]['route'],
                             trips1[str(i)]['travel_time'],
                             trips2[str(i)]['travel_time'],
                            same_time,
                            same_route,
                             ])
            


        # Calculate Averages
        trip1_avg_tt = trip1_tot_tt/num_trips;
        trip2_avg_tt = trip2_tot_tt/num_trips;
        print("    " +filename_1 + ' Average Time: ' +  str(trip1_avg_tt))
        print("    " +filename_2 + ' Average Time: ' +  str(trip2_avg_tt))


        
        print("    CSV file " + output_filename+" has been created.\n")

def compare_output_files(output_filename, xml1, xml2,filename_1,filename_2):
    trips1 = extract_routes(xml1)
    trips2 = extract_routes(xml2)
    
    # sort the trips by id
    sorted_trips1 = dict(sorted(trips1.items()))
    sorted_trips2 = dict(sorted(trips2.items()))

    # for i in range (0,len(sorted_trips1)):
    #     print(str(i) + ": " + str(sorted_trips1[str(i)]))

    # print(sorted_trips2)

    create_csv(sorted_trips1,sorted_trips2,output_filename,filename_1,filename_2)

    


if __name__ == "__main__":
    
    
    file1_name = "a_500"
    xml1 = parse_xml("sim_outputs/astar/a_500tr.out.xml")


    file2_name = "d_500"
    xml2 = parse_xml("sim_outputs/dijkstra/d_500tr.out.xml")

    # compare_output_files('dva_500tr_rand20.csv',xml1, xml2,file1_name,file2_name)

    file1_name = "a_1500"
    xml1 = parse_xml("sim_outputs/astar/a_1500tr.out.xml")


    file2_name = "d_1500"
    xml2 = parse_xml("sim_outputs/dijkstra/d_1500tr.out.xml")

    compare_output_files('dva_1500tr_rand20.csv',xml1, xml2,file1_name,file2_name)

    

