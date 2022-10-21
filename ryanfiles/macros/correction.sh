echo "Inside orgcorrection.sh"
rm -rf /home/thakur/mylab/ryanfiles/multisimulation/oct18-frontleftcorner-topdead0.0004-ceramic-den1.22/correctionoct18-frontleftcorner-topdead0.0004-ceramic-den1.22.dat
#echo "cor_file: $cor_file"
#if [ -f "$cor_file" ];then
#  echo "$cor_file exists and removing!"
#  rm -rf $cor_file
#else
#  echo "$cor_file doesnot exist!"
#  echo ""
#fi
  

#./correction.py am241
#./correction.py ba133
#./correction.py co60
#./correction.py cs137
#./correction.py eu152
#./correction.py na22
./correction.py pb210
#./correction.py ra226

#cp correction.dat correctionfeb17.dat
