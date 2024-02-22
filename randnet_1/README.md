# for generating random trips
python3 /opt/homebrew/share/sumo/tools/randomTrips.py -n /Users/cianmurphy/code_directories/final_year_project/net_gen/randnet_1.net.xml -e 1000

# for generating routes
duarouter --trip-files=trips.trips.xml --net-file=randnet_1.net.xml --routing-algorithm astar --output-file=atar-routes.rou.xml