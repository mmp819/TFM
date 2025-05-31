#!/bin/bash
source common.sh

set -o errexit

install_kafka() {
    local node=$1

    echo "[*] Instalando Apache Kafka en $USER:$node"

    echo "[*] Creando directorio de instalación..."
    echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo mkdir -p /opt/kafka"

    echo "[*] Descargando Kafka..."
    sshpass -p $PASS ssh -tt -p $PORT $USER@$node "wget https://dlcdn.apache.org/kafka/3.9.0/kafka_2.13-3.9.0.tgz -O /tmp/kafka.tgz"

    echo "[*] Desempaquetando Kafka..."
    echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo tar -xzf /tmp/kafka.tgz -C /opt/kafka --strip-components=1"
    sshpass -p $PASS ssh -p $PORT $USER@$node "rm /tmp/kafka.tgz"

    echo "[*] Añadiendo variables al sistema..."
    sshpass -p $PASS ssh -p $PORT $USER@$node "echo 'export KAFKA_HOME=/opt/kafka' >> ~/.bashrc"
    sshpass -p $PASS ssh -p $PORT $USER@$node "echo 'export PATH=\${PATH}:\${KAFKA_HOME}/bin' >> ~/.bashrc"
}

install_kafka $1 # IP

