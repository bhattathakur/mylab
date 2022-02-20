#!/bin/bash

#This changes the high value number resulted in the simulated to 0

sed -i --debug '1s/.*/0  0/' {am241,ba133,pb210,ra226}*sim.dat 
sed -i --debug '2s/.*/1  0/' {co60,cs137,eu152}*sim.dat 
sed -i --debug '3s/.*/2  0/' na22*sim.dat 

