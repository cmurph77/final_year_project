# final_year_project
This is a repository for Cian Murphys Final year project. The goal of this project is to measure the impact of vehicle routing algorithms on the over traffic in a city simulation.


# net generate
python3 /opt/homebrew/share/sumo/tools/randomTrips.py -n randnet_1.net.xml -e 1000 

# duarouter
duarouter --trip-files=trips.trips.xml --net-file=randnet_1.net.xml --routing-algorithm astar --output-file=atar-routes.rou.xml