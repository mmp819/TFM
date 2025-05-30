#!/bin/bash
source common.sh

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
    sshpass -p $PASS ssh -p $PORT $USER@$node "python3 -m venv $dest/venv"

    # Instalar dependencias
    sshpass -p $PASS ssh -p $PORT $USER@$node "source $dest/venv/bin/activate && \
        pip install --upgrade pip && pip install rti.connextdds"
}

prepare_vehicle_env $1 $2


