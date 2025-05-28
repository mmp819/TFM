#!/bin/bash
source common.sh

run_vehicles() {
	local v_n=1
	
	# Para cada nodo asignado a un vehiculo
	while read node; do
		veh_id=$(printf "%02d" $v_n)
		csv_dir="$REMOTE_DIR/veh_${veh_id}"
		csv="veh_${veh_id}.csv"
		
		# Ejecutar la simulacion y mantener en segundo plano. Guardar outputs en logs.
		echo "Ejecutando Vehiculo ${veh_id} en $node..."
		sshpass -p $PASS ssh -p $PORT $USER@$node "cd $csv_dir && source venv/bin/activate && \
			nohup python3 vehicle.py $csv > ${veh_id}.log 2>&1 &"
			
		((v_n++)) # Incremento de contador asignado al numero que conforma el ID de los vehiculos.
	done < nodes_vehicles.txt
}

run_vehicles
