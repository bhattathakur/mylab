rm -vrf /home/thakur/mylab/ryanfiles/multisimulation/simdir/correctionsimdir.dat

./correction.py am241
./correction.py ba133
./correction.py co60
./correction.py cs137
./correction.py eu152
./correction.py na22
./correction.py pb210
./correction.py ra226

#cp correction.dat correctionfeb17.dat
