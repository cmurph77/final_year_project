import traci as t,traci

# Connect to SUMO simulation
traci.start(["sumo", "-c", "random_20.sumocfg"])



# Simulation loop
step = 0
network_edges = []

# Retrieve a list of all edge IDs
edge_list = traci.edge.getIDList()


# runs forever
run = True
while run:
    t.simulationStep()    
    # Your simulation logic here
    vehicles_on_edge = traci.edge.getLastStepVehicleIDs(':10_0')
    # print(vehicles_on_edge)
    # for edge in edge_list:
    #     print(edge)

    current_active_vehicles = traci.vehicle.getIDList()
    print("vehicle count:" +  str(len(current_active_vehicles)))






    step += 1
    if t.vehicle.getIDCount() == 0:
        print("NO MORE VEHICLES")
        run = False


# Close TraCI connection
traci.close()