#!/bin/bash
source common.sh

set -o errexit

prepare_monitoring_kafka_env() {
	local node=$1
	local dir_kafka="/opt/kafka"
	local dir_tmp="${REMOTE_DIR}/tmp_jmx"
	local jmx_export_port=8002
	
	echo "[*] Creando directorio temporal..."
	sshpass -p $PASS ssh -p $PORT $USER@$node "mkdir -p $dir_tmp"
	
	echo "[*] Copiando jmx_exporter..."
	sshpass -p $PASS scp -P $PORT ../Simulation/Monitoring/Exporters/Kafka/jmx_exporter.yml $USER@$node:$dir_tmp/
	sshpass -p $PASS scp -P $PORT ../Simulation/Monitoring/Exporters/Kafka/jmx_prometheus_javaagent-1.3.0.jar $USER$node:$dir_tmp/
	
	echo "[*] Moviendo ficheros a localizacion de Kafka..."
	echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo mv ${dir_tmp}/jmx_exporter.yml ${dir_kafka}/"
	echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo mv ${dir_tmp}/jmx_prometheus_javaagent-1.3.0.jar ${dir_kafka}/ && \
		sudo rm -r $dir_tmp"
	
	
	echo "[*] Modificando script de arranque de Kafka..."
	echo $PASS | sshpass -p $PASS ssh -p $PORT $USER@$node "echo 'export KAFKA_JMX_OPTS=\"-javaagent:${dir_kafka}/jmx_prometheus_javaagent-1.3.0.jar=${jmx_port}:${dir_kafka}/jmx_exporter.yml\"' \
		| sudo tee -a $dir_kafka/bin/kafka-server-start.sh"
}

prepare_monitoring_kafka_env "$1"
