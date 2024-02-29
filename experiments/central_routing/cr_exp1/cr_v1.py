import traci as t,traci
import xml.etree.ElementTree as ET
import csv



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
                
def update_live_congestion(current_congestion):
    live_congestion = {}
    for edge_id, congeestion_level in current_congestion.items():
        if congeestion_level > congestion_threshold: congested = True
        else: congested = f=False
        live_congestion[edge_id] = congested

def run_simulation():
    run = True
    step = 0
    while run:
        t.simulationStep()    
        # Your simulation logic here  -------------------------------------------------

        current_active_vehicles = traci.vehicle.getIDList()
        active_veh_count = len(current_active_vehicles)
        current_congestion = create_congestion_dict( create_edges_current_traveltime())
        congestion_matrix.append(current_congestion)
        update_live_congestion(current_congestion)


        # ----- Development Code  ------------------------------------------------

        # if step == 343:
        #     # current_net_traveltime = create_edges_current_traveltime()
        #     congestion = create_congestion_dict( create_edges_current_traveltime())

        #     for edge_id, c in congestion.items():
        #         print(str(edge_id) + "   " + str(c))
                

        # print("edge 117 travel timme " + str(traci.edge.getTraveltime('117')) + ", vehicles on edge: " + str(len(traci.edge.getLastStepVehicleIDs('117'))))


        # if step == 400:
        #     print("\nCurent Active Vehicle Count: " +     print("edge 17 travel timme " + str(traci.edge.getTraveltime('17')) + ", ")

        #     print("On step 250 so creating a congestion matrix")
        #     edges_current_vehicles = create_edges_current_vehicles(current_active_vehicles,step)
            
        #     # for item  in edges_current_vehicles: print(item)




        # -----------------------------------------------------------------------------
        step += 1
        if t.vehicle.getIDCount() == 0:
            print("NO MORE VEHICLES")
            run = False

if __name__ == "__main__":

    # Connect to SUMO simulation
    traci.start(["sumo", "-c", "random_20.sumocfg"])
    net_file = "random_20.net.xml"

    #  Set up Code
    network_edges = traci.edge.getIDList()   # gets a list of edges in the network
    baseline_edges_traveltime = create_edges_current_traveltime() # calculates the travel time for each edge 
    baseline_traveltimes = create_congestion_dict(baseline_edges_traveltime) 
    network_distances = get_distances_in_net(net_file)
    congestion_matrix = []
    live_congestion = {}
    # init_live_congestion()
    congestion_threshold = 2





    # for edge, dist in network_distances.items():
    #     print(str(edge) + "  " + str(dist))
    



    run_simulation()

    # Post proccessing
    # print("step" + str(step))
    # output_congestion_matrix(congestion_matrix, 'congestion_matrix.csv')
    

    # Close TraCI connection
    traci.close()