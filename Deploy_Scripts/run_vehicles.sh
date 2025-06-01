#!/bin/bash
source common.sh

set -o errexit
exec 3< nodes_vehicles.txt # Cambiar descriptor para evitar conflictos con SSH

run_vehicles() {	
	local v_id=$1
	local node=$2

	local dir="$REMOTE_DIR/veh_${v_id}"
	local csv="veh_${v_id}.csv"
		
	# Ejecutar la simulacion y mantener en segundo plano. Guardar outputs en logs.
	echo "Ejecutando Vehiculo ${v_id} en $node..."
	sshpass -p $PASS ssh -p $PORT $USER@$node "cd $dir && source venv/bin/activate && \
		export RTI_LICENSE_FILE=/home/$USER/rti_workspace/7.5.0/rti_license.dat \
		nohup python3 vehicle.py $csv > ${v_id}.log 2>&1 &"
}

v_n=1
while IFS= read -r node <&3; do
	v_id=$(printf "%02d" "$v_n")
	run_vehicles "$v_id" "$node" &
	((v_n++))
done < nodes_vehicles.txt

exec 3>&-
