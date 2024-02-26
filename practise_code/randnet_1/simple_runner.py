import traci as t,traci

# Connect to SUMO simulation
traci.start(["sumo-gui", "-c", "randnet_1.sumocfg"])



# Simulation loop
step = 0
# runs forever
run = True
while run:
    t.simulationStep()    
    # Your simulation logic here
    step += 1
    if t.vehicle.getIDCount() == 0:
        print("NO MORE VEHICLES")
        run = False


# Close TraCI connection
traci.close()