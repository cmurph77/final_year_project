# Path name
/Users/cianmurphy/code_directories/final_year_project/experiments/dva/dva_exp2

# Generate Network
link: https://sumo.dlr.de/docs/netgenerate.html
netgenerate --rand ----rand.iterations 20

# for generating random trips
python3 /opt/homebrew/share/sumo/tools/randomTrips.py -n <path-to-repo>/random_20.net.xml -e 100
python3 /opt/homebrew/share/sumo/tools/randomTrips.py -n /Users/cianmurphy/code_directories/final_year_project/experiments/dva/dva_exp2/grid_10.net.xml -e 100

# for generating routes
duarouter --trip-files=trips.trips.xml --net-file=random_20.net.xml --routing-algorithm astar --output-file=atar-routes.rou.xml
duarouter --trip-files=trips.trips.xml --net-file=random_20.net.xml --routing-algorithm dijkstra --output-file=dijsktra-routes.rou.xml

duarouter --trip-files=trips.trips.xml --net-file=random_20.net.xml --routing-algorithm dijkstra --output-file=dfrouter-routes.rou.xml

# what ive done
1. i created a grid network of size 10x10
2. 
