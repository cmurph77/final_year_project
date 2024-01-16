# Goal: reroute a vehicle if it gets to a location

import sys
import traci

# params (route, depart,type,id)
def add_vehicle(route, depart,type,id):
    
    vehicle = f'<vehicle id="{id}" type="typeWE" route="{route}" depart="{depart}" />'
    return vehicle

def create_roufile():
# HEADER
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<!-- generated on 2023-11-15 14:45:18 by Eclipse SUMO netedit Version 1.18.0
-->

<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">
    <!-- Routes -->
        """
# Routes
    # xml_content = xml_content + """ <route id="br_tl" edges="start_e  -E3 E10" color="cyan"/>"""


# Trips
    # xml_content = xml_content + """<trip id="t_0" depart="0.00" from="start_e" to="end_e"/>"""



# Vehicles
    xml_content = xml_content + """
    <vType id="car" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="10" guiShape="passenger"/>"""

    # for i in range (1,6):  
    #     xml_content = xml_content + add_vehicle('br_tl',0,'typeWE',i)
    
    # for i in range (6,11):
    #     xml_content = xml_content + add_vehicle('tr_bl',0,'typeWE',i)
    
    
# Footer
    xml_content = xml_content + """
</routes>"""

    # 098765432 file
    with open("dalkey.rou.xml", "w") as file:
        file.write(xml_content)


def run():
    # Simulation loop
    step = 0
    count = traci.vehicle.getIDCount()
    routeInfo = traci.simulation.findRoute('home', 'pub')
    print(routeInfo)
    veh_id = "one"
    traci.route.add('route1', routeInfo.edges)
    traci.vehicle.add(vehID=veh_id,typeID='car', routeID='route1')



    while step < 1000:
        traci.simulationStep()
        location = traci.vehicle.getRoadID(veh_id)
        print(location)
        




        # Your simulation logic here
        step += 1

    # Close TraCI connection
    traci.close()
    sys.stdout.flush()


if __name__ == "__main__":
    # Connect to SUMO simulation
    # create_roufile()
    print('Creating route file')
    traci.start(["sumo-gui", "-c", "dalkey.sumocfg"])  # opens the gui
    # traci.start(["sumo", "-c", "dalkey.sumocfg"])   

    run()
