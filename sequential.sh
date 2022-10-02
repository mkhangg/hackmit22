#!/bin/bash

echo ">> Starting pipeline..."
sudo python mic/vad_doa.py & 
echo ">> Collecting data..."
sleep 0.5
echo -ne "   Progress: >>>                        [20%]\r"
sleep 0.5
echo -ne "   Progress: >>>>>>>                    [40%]\r"
sleep 0.5
echo -ne "   Progress: >>>>>>>>>>>>>>             [60%]\r"
sleep 0.5
echo -ne "   Progress: >>>>>>>>>>>>>>>>>>>>>>>    [80%]\r"
sleep 0.5
echo -ne "   Progress: >>>>>>>>>>>>>>>>>>>>>>>>>> [100%]\r"
sleep 0.5
echo -ne "\n"
wait 
echo ">> Finished collecting data..."

sudo python body/Code/Server/testMove.py
echo ">> Executed command..."
echo ">> Ending pipeline..."