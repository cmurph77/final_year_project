import traci as t,traci
import xml.etree.ElementTree as ET
import csv
import set_sumocgf 
import random



def get_network_edges(net_file):
    return traci.edge.getIDList()   # gets a list of edges in the network

# creates a dict with { edge_id : edge_length }
def set_edge_length_dict():
    edge_lengths = {}
    for edge_id in network_edges:
        edge_lengths[edge_id] = traci.lane.getLength(edge_id)

    return edge_lengths

# creates a dict with { edge_id : current_vehicles_on_edge }
def create_edges_current_vehicles(active_vehicles,step):
    edges_current_vehicles = {}
    for edge in network_edges:
        vehicles_on_edge = traci.edge.getLastStepVehicleIDs(edge)
        edges_current_vehicles[edge] = vehicles_on_edge

        # print ("step: " + str(step)+ " | On edge: " + edge + ", there are " + str(len(vehicles_on_edge)))

#  creates a dict with {edge_id : current_traveltime}
def create_edges_current_traveltime():
    edges_current_traveltime = {}
    # print(network_edges)
    for edge in network_edges:
        current_traveltime = traci.edge.getTraveltime(edge)
        # print(current_traveltime)
        edges_current_traveltime[edge] = current_traveltime

    return edges_current_traveltime

# returns a congestion disctionary with { edge_id :  current_tt/ baseline_traveltime}
def create_congestion_dict(net_traveltimes):
    congestion_dict = {}
    for edge_id, current_tt in net_traveltimes.items():
        congestion_dict[edge_id] = round(current_tt / baseline_edges_traveltime[edge_id],3)    

    return congestion_dict

# extracts distances from net file in the form { edge_id : distance }
def get_distances_in_net(xml_file):
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

# outputs a csv file of the congestion matrix with edge_ids on top row and congestion at each time step below 
def output_congestion_matrix(congestion_matrix, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header
        # header = [list(entry.keys())[0] for entry in congestion_matrix[1]]
        field_headers = congestion_matrix[0].keys()
        # print(field_headers)
        writer.writerow(field_headers)
        
        # i = 0
        for cong_dict in congestion_matrix:
                # congestion_vals = [list(entry.values())[0] for entry in cong_dict]
            congestion_vals = cong_dict.values()
            writer.writerow(congestion_vals)
                
# This function produces a dict like { edge_id : Boolean of whether congestion exceeds set congestion threshold}                
def update_live_congestion(current_congestion,congestion_threshold):
    live_congestion = {}
    for edge_id, congeestion_level in current_congestion.items():
        if congeestion_level > congestion_threshold: congested = True
        else: congested = f=False
        live_congestion[edge_id] = congested

    return live_congestion

def congestion_on_route(route, live_congestion):
    for edge_id in route:
        congestion = live_congestion[edge_id]
        if congestion: return True

    return False

def get_remaining_route(current_location, routes):
    # Find the index of the current location in the routes list
    try:
        current_index = routes.index(current_location)
    except ValueError:
        # print(f"Error: Current location '{current_location}' not found in the route.")
        return []

    # Extract the remaining route from the current location onwards
    remaining_route = routes[current_index + 1:]

    return remaining_route
    

def run_simulation():
    run = True
    step = 0
    congestion_threshold = 100
    rereouting_prob = 75
    vehicle_rerouted = [False] * trip_count
    rerouted_count = 0
    central_route = False


    while run:
        t.simulationStep()    
        # Get Current Time Step Variables  -------------------------------------------------

        current_active_vehicles = traci.vehicle.getIDList()  # get a list of active vehicles
        active_veh_count = len(current_active_vehicles)  
        current_congestion = create_congestion_dict( create_edges_current_traveltime())   # get a congestion dict for time step
        congestion_matrix.append(current_congestion)    # add to congestion matrix
        live_congestion = update_live_congestion(current_congestion,congestion_threshold)  # get live congestion in boolean
        
        # ----- Analyse Each Vehicle  ------------------------------------------------

        # if central_route == True:
        #     for vehicle_id in current_active_vehicles:

        #         # Get Vehcile Details
        #         veh_location = traci.vehicle.getRoadID(vehicle_id)
        #         veh_route = traci.vehicle.getRoute(vehicle_id)
        #         veh_remaing_route = get_remaining_route(veh_location,veh_route)

        #         # Check if there is congestion on the route
        #         if congestion_on_route(veh_remaing_route,live_congestion):
        #             # if vehicle_rerouted[int(vehicle_id)] == False :
        #             random_num = random.randint(1,100)
        #             print("random_num: " + str(random_num))
        #             if random_num > rereouting_prob :
        #                 # print("Hit Congestion")
        #                 rerouted_count = rerouted_count + 1
        #                 print("   veh_id: " + str(vehicle_id) + ", location: " + str(veh_location)+ " | route = " + str(veh_route) + " | left = " + str(veh_remaing_route) )
        #                 traci.vehicle.rerouteTraveltime(vehicle_id)
        #                 vehicle_rerouted[int(vehicle_id)] = True

        
        # ----- Development Code  ------------------------------------------------




        # -----------------------------------------------------------------------------
        step += 1
        if t.vehicle.getIDCount() == 0:
            print("NO MORE VEHICLES")
            print("REREOUT COUNT: " + str(rerouted_count))

            run = False

if __name__ == "__main__":

    # Set Up simulation configeration
    trip_count = 1000
    path_to_sim_files = "sim_files/"
    config_file = path_to_sim_files + "random_20.sumocfg"
    net_file = "random_20.net.xml"
    set_sumocgf.set_netfile_value(config_file,net_file)
    set_sumocgf.set_route_file_value(config_file,"../trip_files_random20net/1000tr_rand20.trips.xml")
    set_sumocgf.set_routing_algo_value(config_file,"astar")

    # Sim output files
    congestion_matric_output_file = 'output_files/congestion_matrices/1000tr_cr_cm.csv'
    set_sumocgf.set_output_file_value(config_file,"../output_files/cr_1000tr.out.xml")

    # Connect to SUMO simulation
    traci.start(["sumo", "-c", config_file])

    #  Set up Code for measuring congestion
    network_edges = get_network_edges(net_file)   # gets a list of edges in the network
    baseline_edges_traveltime = create_edges_current_traveltime() # calculates the travel time for each edge 
    baseline_traveltimes = create_congestion_dict(baseline_edges_traveltime) 
    network_distances = get_distances_in_net(path_to_sim_files + net_file)
    congestion_matrix = []
    live_congestion = {}
    

    # Run the Simulation
    run_simulation()

    # Print out results
    output_congestion_matrix(congestion_matrix, congestion_matric_output_file)
    

    # Close TraCI connection
    traci.close()