#!/bin/bash

while true; do
    date +"%Y-%m-%d %H:%M:%S" >> save_hour.txt
    sleep 5
done &
echo 'Para detener el proceso se utiliza el comando: kill $(pgrep -f "save_hour.sh")
'
