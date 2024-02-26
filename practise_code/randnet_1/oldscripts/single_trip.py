# Routes one vehicle through the random net and prints out the time taken
import traci as t,traci

# Connect to SUMO simulation
traci.start(["sumo-gui", "-c", "randnet_1.sumocfg"])


start_e = str(-4747)
end_e = str(2846)
alt_e = str(4745)

routing_mode = 1
routeInfo = traci.simulation.findRoute(start_e, end_e,routingMode= routing_mode)
print("Route Edges:  "+ str(routeInfo.edges))

veh_id = "one"
traci.route.add('route1', routeInfo.edges)
# traci.vehicle.add(vehID=veh_id, routeID='route1')


# Simulation loop
step = 0
# runs forever
while True:
    traci.simulationStep()
    if step == 10:
        count = traci.vehicle.getIDCount()
        print(count)
    step += 1

# Close TraCI connection
traci.close()