#!/bin/bash
source common.sh

stop_vehicles() {
	# Para cada nodo asignado a un vehiculo
	while read node; do
		echo "Deteniendo vehiculo asignado a $node..."
		
		# Matar proceso
		echo "Ejecutando Vehiculo ${veh_id} en $node..."
		sshpass -p $PASS ssh -p $PORT $USER@$node "pkill -f vehicle.py && echo 'Simulacion detenida.'"
	done < nodes_dds.txt
}

stop_vehicles
