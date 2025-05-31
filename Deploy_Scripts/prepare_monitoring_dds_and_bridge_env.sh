#!/bin/bash
source common.sh

prepare_monitoring_dds_and_bridge_env() {
	local node=$1
	local dir_export="${REMOTE_DIR}/dds_export"
	local dir_routing="${REMOTE_DIR}/routing"
	
	echo "[*] Creando directorio..."
	sshpass -p $PASS ssh -p $PORT $USER@$node "mkdir -p $dir_dest"
	
	echo "[*] Copiando exportador DDS y Bridge..."
	sshpass -p $PASS scp -P $PORT ../Simulation/Monitoring/Exporters/DDS/exporter_dds.py $USER@$node:$dir_export/
	# PENDIENTE AÑADIR LOS TIPOS DE DATOS DE MONITORIZACION
	sshpass -p $PASS scp -P $PORT ../Simulation/Bridge/dds_kafka_bridge.xml $USER@$node:$dir_routing/
	
	echo "[*] Creando entorno virtual..."
	sshpass -p $PASS ssh -p $PORT $USER@$node "python3 -m venv $dir_export/venv"
	
	echo "[*] Instalando dependencias..."
	sshpass -p $PASS ssh -p $PORT $USER@$node "source $dir_routing/venv/bin/activate && \
		pip install --upgrade pip && pip install prometheus_client rti.connextdds"
}

prepare_monitoring_dds_and_brigde_env() "$1"
