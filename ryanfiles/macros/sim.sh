rm -f sim.dat
add="/home/thakur/mylab/ryanfiles/"
./sim.py na22  $add/mac_files/na22.mac  $add/simgdf/na22sim.gdf $add/nugdf/na22.gdf
./sim.py co60  $add/mac_files/co60.mac  $add/simgdf/co60sim.gdf $add/nugdf/co60.gdf
./sim.py ba133 $add/mac_files/ba133.mac $add/simgdf/ba133sim.gdf $add/nugdf/ba133.gdf
./sim.py cs137 $add/mac_files/cs137.mac $add/simgdf/cs137sim.gdf $add/nugdf/cs137.gdf
./sim.py eu152 $add/mac_files/eu152.mac $add/simgdf/eu152sim.gdf $add/nugdf/eu152.gdf
./sim.py pb210 $add/mac_files/pb210.mac $add/simgdf/pb210sim.gdf $add/nugdf/pb210.gdf
./sim.py ra226 $add/mac_files/ra226.mac $add/simgdf/ra226sim.gdf $add/nugdf/ra226.gdf
./sim.py am241 $add/mac_files/am241.mac $add/simgdf/am241sim.gdf $add/nugdf/am241.gdf

#./sim.py na22  $add/mac_files/na22.mac  $add/simgdf/na22sim.gdf /home/thakur/mylab/ryanfiles/nugdf/na22.gdf
#./sim.py co60  $add/mac_files/co60.mac  $add/simgdf/co60sim.gdf /home/thakur/mylab/ryanfiles/nugdf/co60.gdf
#./sim.py ba133 /home/thakur/mylab/ryanfiles/mac_files/ba133.mac /home/thakur/mylab/ryanfiles/simgdf/ba133sim.gdf /home/thakur/mylab/ryanfiles/nugdf/ba133.gdf
#./sim.py cs137 /home/thakur/mylab/ryanfiles/mac_files/cs137.mac /home/thakur/mylab/ryanfiles/simgdf/cs137sim.gdf /home/thakur/mylab/ryanfiles/nugdf/cs137.gdf
#./sim.py eu152 /home/thakur/mylab/ryanfiles/mac_files/eu152.mac /home/thakur/mylab/ryanfiles/simgdf/eu152sim.gdf /home/thakur/mylab/ryanfiles/nugdf/eu152.gdf
#./sim.py pb210 /home/thakur/mylab/ryanfiles/mac_files/pb210.mac /home/thakur/mylab/ryanfiles/simgdf/pb210sim.gdf /home/thakur/mylab/ryanfiles/nugdf/pb210.gdf
#./sim.py ra226 /home/thakur/mylab/ryanfiles/mac_files/ra226.mac /home/thakur/mylab/ryanfiles/simgdf/ra226sim.gdf /home/thakur/mylab/ryanfiles/nugdf/ra226.gdf
#./sim.py am241 /home/thakur/mylab/ryanfiles/mac_files/am241.mac /home/thakur/mylab/ryanfiles/simgdf/am241sim.gdf /home/thakur/mylab/ryanfiles/nugdf/am241.gdf
