#check if data.dat exists ... delete if so
if [[ -f data.dat ]]
then 
  echo "'data.dat' exists on the filesystem."
  echo "deleting ...."
fi

add="/home/thakur/mylab/ryanfiles/"
rm -f data.dat
isotopes=("na22" "co60" "ba133" "cs137" "eu152" "pb210" "ra226" "am241")
da=".dat"
gd=".gdf"

for iso in ${isotopes[@]};do
  echo "working with $iso"
  echo "-------------------------------------------------------------"
  ./data.py $iso $add/datfiles/$iso$da $add/gdf/$iso$gd $add/nugdf/$iso$gd
done
