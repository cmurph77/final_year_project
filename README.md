# final_year_project
This is a repository for Cian Murphys Final year project. The goal of this project is to measure the impact of vehicle routing algorithms on the over traffic in a city simulation.


# Path name
/Users/cianmurphy/code_directories/final_year_project

# Generate Network
link: https://sumo.dlr.de/docs/netgenerate.html
command netgenerate --rand ----rand.iterations 20


# for generating random trips
python3 /opt/homebrew/share/sumo/tools/randomTrips.py -n <path-to-repo>/random_20.net.xml -e 100

# for generating routes
duarouter --trip-files=trips.trips.xml --net-file=random_20.net.xml --routing-algorithm astar --output-file=atar-routes.rou.xml
duarouter --trip-files=trips.trips.xml --net-file=random_20.net.xml --routing-algorithm dijkstra --output-file=dijsktra-routes.rou.xml

duarouter --trip-files=trips.trips.xml --net-file=random_20.net.xml --routing-algorithm dijkstra --output-file=dfrouter-routes.rou.xml