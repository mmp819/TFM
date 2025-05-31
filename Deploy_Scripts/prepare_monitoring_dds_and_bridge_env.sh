#!/bin/bash
source common.sh

set -o errexit

prepare_monitoring_dds_and_bridge_env() {
	local node=$1
	local dir_export="${REMOTE_DIR}/dds_export"
	local dir_routing="${REMOTE_DIR}/routing"
	
	echo "[*] Creando directorios..."
	sshpass -p $PASS ssh -p $PORT $USER@$node "mkdir -p $dir_export"
	sshpass -p $PASS ssh -p $PORT $USER@$node "mkdir -p $dir_routing"
	
	echo "[*] Copiando exportador DDS y Bridge..."
	sshpass -p $PASS scp -P $PORT ../Simulation/Monitoring/Exporters/DDS/*.py $USER@$node:$dir_export/
	sshpass -p $PASS scp -P $PORT ../Simulation/Bridge/dds_kafka_bridge.xml $USER@$node:$dir_routing/
	
	echo "[*] Creando entorno virtual..."
	echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo apt-get update &&
    sudo apt-get install -y python3-venv && python3 -m venv $dir_export/venv"
	
	echo "[*] Instalando dependencias..."
	sshpass -p $PASS ssh -p $PORT $USER@$node "source $dir_export/venv/bin/activate && \
		pip install --upgrade pip && pip install prometheus_client rti.connext==7.5.0"
}

prepare_monitoring_dds_and_bridge_env "$1"
