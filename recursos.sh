#!/bin/bash

# Obtener el intervalo de tiempo desde el usuario
read -p "Ingrese el intervalo de tiempo en segundos: " intervalo

while true; do
    # Obtener estadísticas de memoria y CPU y guardarlas en el archivo recursos.csv
    echo "$(date +"%Y-%m-%d %H:%M:%S"),$(free -m | grep Mem | awk '{print $3","$4}'),$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')" >> recursos.csv
    sleep $intervalo
done &


echo 'Para detener el proceso se utiliza el comando: kill $(pgrep -f "recursos.sh")
'
