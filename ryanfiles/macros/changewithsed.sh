#!/bin/bash

#make changes in the files
#change in the file sim.sh

folder=feb18
orgfile="orgsim.sh"
plotsimpy="orgplotSim.py"
orgcorr="orgcorrection.py"
corsh="orgcorrection.sh"
corplotsh="orgplotCorrection.sh"
orgplotcorr="orgplotCorrection.py"
orgplotcorrs="orgplotCorrections.py"





#echo "Editing file: ${orgfile}"
#sed "s/simdir/${folder}/" "${orgfile}" > sim.sh
#
##run the file sim.sh
#echo "Running sim.sh file..."
#bash sim.sh
#
#sleep 3
##modify orgplotSim.py
#echo "Editing file: ${plotsimpy}"
#sed "s/simdir/${folder}/" "${plotsimpy}" > plotSim.py 
#
#sleep 3
##running the file plotSim.py
#echo "running the file plotSim.sh"
#
#sleep 3
##edit the file orgcorrection.sh
#echo "Editing file: ${corsh}"
#sed "s/simdir/${folder}/g" "${corsh}" > correction.sh 
#
#
#sleep 3
##edit the file orgcorrection.py
#echo "Editing file: ${orgcorr}"
#sed "s/simdir/${folder}/" "${orgcorr}" > correction.py 
#echo "running the file correction.sh"
#bash correction.sh
#sleep 3
#
#edit the file plotCorrection.sh
#echo "Editing file: ${corplotsh}"
#sed "s/simdir/${folder}/g" "${corplotsh}" > plotCorrection.sh 
#
#sleep 3
#
##edit the file orgplotCorrection.py
#echo "Editing file: ${orgplotcorr}"
#sed "s/simdir/${folder}/" "${orgplotcorr}" > plotCorrection.py 
#echo "running the file plotCorrection.sh"
#bash plotCorrection.sh

sleep 3

#edit the file orgplotCorrections.py
echo "Editing file: ${orgplotcorrs}"
sed "s/simdir/${folder}/" "${orgplotcorrs}" > plotCorrections.py 
echo "running the file plotCorrections.py"
python3 plotCorrections.py
