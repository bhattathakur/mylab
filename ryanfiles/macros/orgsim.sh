rm -rf sim.dat

add1="/home/thakur/mylab/ryanfiles/multisimulation/simdir" #sim.dat and sim.gdf

add="/home/thakur/mylab/ryanfiles"                        #org gdf

echo "sim data file and fitting gdf dir: ${add1}"
echo "org gdf file dir: ${add}"


sleep 3

#exit 0
#
#echo "----------------------------------------------------------------- "
#./sim.py am241 $add1/am241.mac $add1/am241sim.gdf $add/nugdf/am241.gdf
#echo "----------------------------------------------------------------- "
#./sim.py ba133 $add1/ba133.mac $add1/ba133sim.gdf $add/nugdf/ba133.gdf
#echo "------------------------------------------------------------------ "
#./sim.py co60  $add1/co60.mac  $add1/co60sim.gdf $add/nugdf/co60.gdf
#echo "------------------------------------------------------------------ "
#./sim.py cs137 $add1/cs137.mac $add1/cs137sim.gdf $add/nugdf/cs137.gdf
#echo "------------------------------------------------------------------ "
#./sim.py eu152 $add1/eu152.mac $add1/eu152sim.gdf $add/nugdf/eu152.gdf
#echo "------------------------------------------------------------------ "
#./sim.py na22  $add1/na22.mac  $add1/na22sim.gdf $add/nugdf/na22.gdf
echo "------------------------------------------------------------------ "
./sim.py pb210 $add1/pb210.mac $add1/pb210sim.gdf $add/nugdf/pb210.gdf
#echo "------------------------------------------------------------------ "
#./sim.py ra226 $add1/ra226.mac $add1/ra226sim.gdf $add/nugdf/ra226.gdf
#echo "------------------------------------------------------------------ "

#copy sim.dat to add1
sleep 3
echo "copy sim.dat to: ${add1}"

sleep 3
cp sim.dat ${add1}/simsimdir.dat
echo "file created: ${add1}/simsimdir.dat"
