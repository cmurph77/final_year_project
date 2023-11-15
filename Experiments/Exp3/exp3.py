import sys
import traci

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
    traci.start(["sumo-gui", "-c", "exp3.sumocfg"])
    run()
