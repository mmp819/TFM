#!/bin/bash
source common.sh

set -o errexit

prepare_aggregator_env() {
	local node=$1
	local dest="${REMOTE_DIR}/aggregator"
	
	# Crear directorio remoto
	echo "[*] Creando directorio..."
	sshpass -p $PASS ssh -p $PORT $USER@$node "mkdir -p $dest"
	
	# Copiar ficheros necesarios
	echo "[*] Copiando ficheros..."
	sshpass -p $PASS scp -P $PORT ../Simulation/Aggregator/agregator.py $USER@$node:$dest/ # Script de agregacion
	sshpass -p $PASS scp -P $PORT ../Simulation/Aggregator/routing_vehicle_to_dds_domain10.xml $USER@$node:$dest/ # Configuracion del routing service
	sshpass -p $PASS scp -P $PORT ../Simulation/DataTypes/python/vehicle_data.py $USER@$node:$dest/ # Tipo de datos
	
	# Crear entorno virtual de Python
	echo "[*] Creando entorno virtual..."
	echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo apt-get update &&
    sudo apt-get install -y python3-venv && python3 -m venv ${dest}/venv"
	
	# Instalar dependencias
	sshpass -p $PASS ssh -p $PORT $USER@$node "source $dest/venv/bin/activate && \
		pip install --upgrade pip && pip install rti.connext==7.5.0"
}

prepare_aggregator_env "$1"
	
	
