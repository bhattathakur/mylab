#!/user/bin/python

import subprocess
from datetime import datetime

"""This program copies the root file from lcc:$HOME/gesim_batch then uses plot.py program
to create the corresponding data file. 
example: plot.py na22.root na22.gdf(fitted gdf)  na22sim.dat
"""

#start time
start=datetime.now()
start_time=start.strftime('%H:%M:%S')
print("start_time\t",start_time)

root=" ~/mylab/ryanfiles/"                    #root
#..................change sim_dir
sim_dir='simulated_jan2'                 #sim_dir name
#local_path='/home/thakur/mylab/ryanfiles/'    #
mk_dir='mkdir '+root+sim_dir                  #command to create the dir in local computer

isotopes=['am241','ba133','co60','cs137','eu152','na22','pb210','ra226']   #isopotes
sim_data_loc='lcc:/mnt/gpfs2_4m/scratch/tpbh222/'+sim_dir+'/'              #location at lcc

print("simulated data location:\t",sim_data_loc)
#save_place='simulated_datadec31/'
print("destination data location:\t",root)

#create the directory at the local destination
subprocess.call(mk_dir,shell=True)
#command='scp lcc:/home/tpbh222/batch_gesim/'+root_file+' .'

for iso in isotopes:
  #checking for a single isotope
  #if iso!='am241':continue
  root_file=iso+'.root'

  #print("root file:\t",root_file)
  #command='scp lcc:/home/tpbh222/batch_gesim/'+root_file+' .'
  command='scp '+sim_data_loc+root_file+' .'  #copy here


  print("command:\t",command)
  subprocess.call(command,shell=True) #not working without shell=True option

  print("{} downloaded".format(root_file))

  #run plot.py
  gdf=root+"gdf/"+iso+".gdf"  #gdf file location (stays same)

  #crate the directory

  #print("gdf location:\t",gdf)
  save_place=root+sim_dir+"/"

  #sim_data=root+"simulated_datadec23/"+iso+"sim.dat"
  sim_data=save_place+iso+"sim.dat"
  command1='./plot.py '+root_file+gdf+sim_data

  print("command1:\t",command1)

  subprocess.call(command1,shell=True) #not working without shell=True option

  #deleting the root file
  command2="rm -f "+root_file

  #print("command2:\t",command2)
  print("deleting the file:\t",root_file)

  subprocess.call(command2,shell=True)


#end time
end=datetime.now()
end_time=end.strftime('%H:%M:%S')
print("end_time\t",end_time)

#time difference
diff=end-start

print("Time taken:\t",diff)


 
