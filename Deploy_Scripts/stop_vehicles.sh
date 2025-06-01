#!/bin/bash
source common.sh

set -o errexit
exec 3< nodes_vehicles.txt # Cambiar descriptor para evitar conflictos con SSH

stop_vehicles() {
	echo "Deteniendo vehiculo asignado a $1..."
		
	# Matar proceso
	echo "Deteniendo $1..."
	echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "pkill -f vehicle.py && echo 'Simulacion detenida.'"
}

while IFS= read -r node <&3; do
	stop_vehicles "$node" &
done < nodes_vehicles.txt

exec 3>&-