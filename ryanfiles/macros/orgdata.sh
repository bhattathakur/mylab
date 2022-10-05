rm -f data.dat
data_dir=DATADIR
dest_folder=DESTDIR
add="/home/thakur/mylab/ryanfiles/"
add1="/home/thakur/mylab/ryanfiles/$data_dir" #data obtained from .Chn
file_dir=/home/thakur/mylab/ryanfiles/multisimulation/

echo "Experimental data and fitted gdf dir: $add1"
echo "Original gdf dir                    : $add"

#./data.py am241 $add1/am241.dat $add1/am241.gdf $add/nugdf/am241.gdf
#./data.py ba133 $add1/ba133.dat $add1/ba133.gdf $add/nugdf/ba133.gdf
#./data.py co60  $add1/co60.dat  $add1/co60.gdf  $add/nugdf/co60.gdf
#./data.py cs137 $add1/cs137.dat $add1/cs137.gdf $add/nugdf/cs137.gdf
#./data.py eu152 $add1/eu152.dat $add1/eu152.gdf $add/nugdf/eu152.gdf
#./data.py na22  $add1/na22.dat  $add1/na22.gdf  $add/nugdf/na22.gdf
./data.py pb210 $add1/pb210.dat $add1/pb210.gdf $add/nugdf/pb210.gdf
#./data.py ra226 $add1/ra226.dat $add1/ra226.gdf $add/nugdf/ra226.gdf


#copy data.dat to the distination folder
echo "copying data.dat to $file_dir$dest_folder !"
mv data.dat $file_dir$dest_folder/data$dest_folder.dat
