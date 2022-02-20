#!/user/bin/python

import subprocess
from datetime import datetime

"""This program copies the root file from lcc location then uses plot.py program
to create the corresponding data file. Need to correct the data file for some initial entry. 
example:python3 plot.py na22.root na22.gdf(fitted gdf)  na22sim.dat
"""

#Notes
#sim_dir  (name same in remote and local)
#lcc_loc  (lcc location)
#st,en =>change the count/range of the simulation to include the required files
#root for local to save the final data file (root/sim_dir/data.dat)

#start time
start=datetime.now()
start_time=start.strftime('%H:%M:%S')
print("start_time\t",start_time)


################################### simulation data location #################################
sim_dir='batch_gesim'                                         #directory name
lcc_loc='lcc:/home/tpbh222/'+sim_dir+'/'                      #location at lcc home
#lcc_loc='lcc:/mnt/gpfs2_4m/scratch/tpbh222/'+sim_dir+'/'     #location at lcc scratch
st=10;en=20                                                   #count


#Create the local directory to store the final asci data
root=" ~/mylab/ryanfiles/"                    #root
mk_dir='mkdir '+root+sim_dir                  #command to create the dir in local computer
subprocess.call(mk_dir,shell=True)            #make distination directory


print("simulated data location:\t",lcc_loc)
print("destination data location:\t",root+sim_dir+"/")

#isotopes
isotopes=['am241','ba133','co60','cs137','eu152','na22','pb210','ra226'] 

#downloading range
print("range:\t",st,"-",en-1)
wait=input("WANT TO DOWNLOAD?")

for iso in isotopes:
  #checking for a single isotope
  if iso=='am241':continue
  for i in range(st,en):   #change the count of the simulation 
    root_file=iso+str(i)+'.root'

    print("root file:\t",root_file)

    #COPY ROOT FILES HERE
    command='scp '+lcc_loc+root_file+' .'  #copy here
    print("command:\t",command)
    subprocess.call(command,shell=True)    #not working without shell=True option

    print("{} downloaded".format(root_file))

    #RUN PLOT.PY

    #gdf file location
    gdf=root+"gdf/"+iso+".gdf"             #gdf file location (stays same)
    print("gdf file location:\t",gdf)

    #Place to save resultant data file
    save_place=root+sim_dir+"/"
    sim_data=save_place+iso+str(i)+"sim.dat"                    #sim data name
    command1='python3 /home/thakur/mylab/ryanfiles/macros/plot.py '+root_file+gdf+sim_data

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


