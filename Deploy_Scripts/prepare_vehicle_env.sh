#!/bin/bash
source common.sh

set -o errexit
exec 3< nodes_vehicles.txt # Cambiar descriptor para evitar conflictos con SSH

prepare_vehicle_env() {
    local v_id=$1
    local node=$2

    local csv="veh_${v_id}.csv"
    local dest="${REMOTE_DIR}/veh_${v_id}"

    # Crear directorio remoto
    echo "[*] Creando directorio..."
    sshpass -p $PASS ssh -p $PORT $USER@$node "mkdir -p $dest"

    # Copiar ficheros necesarios
    echo "[*] Copiando ficheros..."
    sshpass -p $PASS scp -P $PORT ../Dataset/vehicles_csv/$csv $USER@$node:$dest/ # CSV
    sshpass -p $PASS scp -P $PORT ../Simulation/VehicleSimulation/vehicle.py $USER@$node:$dest/ # Script Simulacion
    sshpass -p $PASS scp -P $PORT ../Simulation/DataTypes/python/vehicle_data.py $USER@$node:$dest/ # Tipo de datos

    # Crear entorno vistual
    sshpass -p $PASS ssh -p $PORT $USER@$node "sudo apt-get update &&
    sudo apt-get install -y python3-venv && python3 -m venv $dest/venv"

    # Instalar dependencias
    sshpass -p $PASS ssh -p $PORT $USER@$node "source $dest/venv/bin/activate && \
        pip install --upgrade pip && pip install rti.connextdds"
}

v_n=1
while IFS= read -r node <&3; do
    v_id=$(printf "%02d" "$v_n")
    prepare_vehicle_env "$v_id" "$node"
    ((v_n++))
done < nodes_vehicles.txt

exec 3<&-




