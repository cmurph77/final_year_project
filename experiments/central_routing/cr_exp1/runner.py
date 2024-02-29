import traci as t,traci

# Connect to SUMO simulation
traci.start(["sumo", "-c", "random_20.sumocfg"])





# Retrieve a list of all edge IDs
network_edges = traci.edge.getIDList()

def get_edge_length():
    edge_lengths = {}
    for edge_id in network_edges:
        edge_lengths[edge_id] = traci.lane.getLength(edge_id)

    return edge_lengths
#  Creates a dictionary with key = edge_id and value = number of vehicles on that edge
def create_edges_current_vehicles(active_vehicles,step):
    edges_current_vehicles = {}
    for edge in network_edges:
        vehicles_on_edge = traci.edge.getLastStepVehicleIDs(edge)
        edges_current_vehicles[edge] = vehicles_on_edge

        # print ("step: " + str(step)+ " | On edge: " + edge + ", there are " + str(len(vehicles_on_edge)))


# runs forever
run = True
step = 0
while run:
    t.simulationStep()    
    # Your simulation logic here  -------------------------------------------------

    current_active_vehicles = traci.vehicle.getIDList()

    if step == 400:
        print("\nCurent Active Vehicle Count: " + str(len(current_active_vehicles)))
        print("On step 250 so creating a congestion matrix")
        edges_current_vehicles = create_edges_current_vehicles(current_active_vehicles,step)
        
        # for item  in edges_current_vehicles: print(item)




    # -----------------------------------------------------------------------------
    step += 1
    if t.vehicle.getIDCount() == 0:
        print("NO MORE VEHICLES")
        run = False


# Close TraCI connection
traci.close()