import traci as t,traci

# Connect to SUMO simulation
traci.start(["sumo-gui", "-c", "randnet_1.sumocfg"])


start_e = str(-4747)
end_e = str(2846)
alt_e = str(4745)

routing_mode = 1
routeInfo = traci.simulation.findRoute(start_e, end_e,routingMode= routing_mode)
print(str(routing_mode) + ":  "+ str(routeInfo.edges))
routing_mode = 2
routeInfo = traci.simulation.findRoute(start_e, end_e,routingMode= routing_mode)
print(str(routing_mode) + ":  "+ str(routeInfo.edges))
routing_mode = 3
routeInfo = traci.simulation.findRoute(start_e, end_e,routingMode= routing_mode)
print(str(routing_mode) + ":  "+ str(routeInfo.edges))
veh_id = "one"
traci.route.add('route1', routeInfo.edges)
traci.vehicle.add(vehID=veh_id,typeID='car', routeID='route1')

# traci.vehicle.changeTarget(veh_id,alt_e)
# Simulation loop
step = 0
while True:
    traci.simulationStep()
    # Your simulation logic here
    step += 1

# Close TraCI connection
traci.close()