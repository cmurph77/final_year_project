import traci as t,traci

# Connect to SUMO simulation
traci.start(["sumo-gui", "-c", "randnet_1.sumocfg"])


# Simulation loop
step = 0
# runs forever
while True:
    traci.simulationStep()
    # Your simulation logic here
    step += 1

# Close TraCI connection
traci.close()