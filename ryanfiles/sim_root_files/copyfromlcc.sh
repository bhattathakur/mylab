#data copy
#scp -r lcc:/project/rma422_uksr/ge4/data/2020/effcal/02-14/door ~/mylab/data/
#simulation copy

#simu_link -> /project/rma422_uksr/gesim/door/
#scp -r lcc:simu_link ~/mylab/simulation/
#scp  lcc:simu_link/*.mac ~/mylab/ryanfiles/mac_files/
#scp  lcc:g4datalink/2020/effcal/02-14/door/*.dat ~/mylab/ryanfiles/chn_files/
scp  lcc:/home/rma422/dev/main/src/*.cxx ~/mylab/ryanfiles/chn_files/
