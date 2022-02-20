#!/bin/bash

folder_name='feb18'
echo "Copying simulation data..."
scp lcc:/home/tpbh222/root_to_ascii/${folder_name}/{am241,ba133,cs137,co60,eu152,na22,pb210,ra226}sim.dat .

echo "Copying simulation mac files ..."
scp lcc:/home/tpbh222/batch_gesim/{am241,ba133,cs137,co60,eu152,na22,pb210,ra226}0.mac .

echo "Renaming simulation mac files ..."
rename -v 's/0.mac/.mac/' *.mac
echo "Copying simulation gdfs..."

scp lcc:/home/tpbh222/simgdf/* .



