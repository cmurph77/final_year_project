import sys
import traci
def generate_routefile():
    with open("exp1.rou.xml", "w") as routes:
        print("""
                <routes>
                        <vType id="typeWE" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="16.67" guiShape="passenger"/>
                        <vType id="typeNS" accel="0.8" decel="4.5" sigma="0.5" length="7" minGap="3" maxSpeed="25" guiShape="bus"/>

                        <route id="r1" edges="E2 E3 E6 E7" />

                    <vehicle id="left_0" type="typeWE" route="r1" depart="0" />
                </routes>
                """, file=routes)

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
    generate_routefile();

    # Connect to SUMO simulation
    traci.start(["sumo-gui", "-c", "exp1.sumocfg"])
    run()



