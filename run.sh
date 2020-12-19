#!/bin/bash
while :
do
FLATTIME=$(date "+%H:%M")
echo $FLATTIME
sleep 1s
if [ $FLATTIME = "08:54" ];
then
echo "Running script"
python3 main.py
break
fi
done
