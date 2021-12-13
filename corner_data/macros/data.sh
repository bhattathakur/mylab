rm -f data.dat
add="/home/thakur/mylab/corner_data/"
./data.py na22 $add/detector_data/na22.dat $add/gdf/na22.gdf $add/gdf0/na22.gdf
./data.py co60 $add/detector_data/co60.dat  $add/gdf/co60.gdf $add/gdf0/co60.gdf
./data.py ba133 $add/detector_data/ba133.dat $add/gdf/ba133.gdf $add/gdf0/ba133.gdf
./data.py cs137 $add/detector_data/cs137.dat $add/gdf/cs137.gdf $add/gdf0/cs137.gdf
./data.py eu152 $add/detector_data/eu152.dat $add/gdf/eu152.gdf $add/gdf0/eu152.gdf
./data.py ra226 $add/detector_data/ra226.dat $add/gdf/ra226.gdf $add/gdf0/ra226.gdf
./data.py am241 $add/detector_data/am241.dat $add/gdf/am241.gdf $add/gdf0/am241.gdf
./data.py pb210 $add/detector_data/pb210.dat $add/gdf/pb210.gdf $add/gdf0/pb210.gdf
./data.py pb210 $add/detector_data/pb210.dat $add/gdf/pb210-1in.gdf $add/gdf0/pb210.gdf
./data.py pb210 $add/detector_data/pb210.dat $add/gdf/pb210-15in.gdf $add/gdf0/pb210.gdf
./data.py pb210 $add/detector_data/pb210.dat $add/gdf/pb210-25in.gdf $add/gdf0/pb210.gdf
./data.py pb210 $add/detector_data/pb210.dat $add/gdf/pb210outer.gdf $add/gdf0/pb210.gdf


