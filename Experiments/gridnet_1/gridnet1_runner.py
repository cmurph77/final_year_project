import traci as t,traci

# Connect to SUMO simulation
traci.start(["sumo-gui", "-c", "gridnet_1.sumocfg"])

run = True;

# Simulation loop
step = 0
# runs forever

while run:
    traci.simulationStep()

    # Your simulation logic here
    step += 1
    
    if traci.vehicle.getIDCount() == 0:
        run = False

# Close TraCI connection
traci.close()