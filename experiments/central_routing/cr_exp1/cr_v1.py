import traci as t,traci


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
        
def run_simulation():
    run = True
    step = 0
    while run:
        t.simulationStep()    
        # Your simulation logic here  -------------------------------------------------

        current_active_vehicles = traci.vehicle.getIDList()
        active_veh_count = len(current_active_vehicles)

        # ----- Development Code  -------------------------------------------------
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
    net_file = "random_20.sumocfg"

    #  Set up Code
    network_edges = traci.edge.getIDList()
    baseline_edges_traveltime = create_edges_current_traveltime()
    



    # run_simulation()

    # Close TraCI connection
    traci.close()