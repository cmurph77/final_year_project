import sys
import traci

def add_vehicle(route, depart,type,id):
    
    vehicle = f'<vehicle id="{id}" type="typeWE" route="{route}" depart="{depart}" />'
    return vehicle

def create_roufile():
    # header
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<!-- generated on 2023-11-15 14:45:18 by Eclipse SUMO netedit Version 1.18.0
-->

<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">
    <!-- Routes -->
        """
    # Routes
    xml_content = xml_content + """
        <route id="br_tl" edges="-E11 E8 -E3 E10" color="cyan"/>
        <route id="tr_bl" edges="E0 -E4 -E5 -E6" color="cyan"/> """

    xml_content = xml_content + """
    <vType id="typeWE" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="10" guiShape="passenger"/>"""
    
    # vehicles

    for i in range (1,6):
        xml_content = xml_content + add_vehicle('br_tl',0,'typeWE',i)
    
    for i in range (6,11):
        xml_content = xml_content + add_vehicle('tr_bl',0,'typeWE',i)
    
    
    # footer
    xml_content = xml_content + """
</routes>"""

    # 098765432 file
    with open("exp4.rou.xml", "w") as file:
        file.write(xml_content)


def run():
    # Simulation loop
    step = 0
    while step < 1000:
        traci.simulationStep()
        # Your simulation logic here
        step += 1

    # Close TraCI connection
    traci.close()
    sys.stdout.flush()


if __name__ == "__main__":
    # Connect to SUMO simulation
    create_roufile()
    traci.start(["sumo-gui", "-c", "exp4.sumocfg"])
    run()
