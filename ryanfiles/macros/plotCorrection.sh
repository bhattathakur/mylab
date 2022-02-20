#!/bin/bash
rm -vrf /home/thakur/mylab/ryanfiles/multisimulation/feb18/sourceCorrectionfeb18.dat

python3 plotCorrection.py na22
python3 plotCorrection.py co60
python3 plotCorrection.py ba133
python3 plotCorrection.py cs137
python3 plotCorrection.py eu152
python3 plotCorrection.py pb210
python3 plotCorrection.py ra226
python3 plotCorrection.py am241
