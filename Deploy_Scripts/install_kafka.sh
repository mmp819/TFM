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
    echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo apt-get update"
    echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo apt-get install -y default-jdk"

    echo "[*] Desempaquetando Kafka..."
    echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo tar -xzf /tmp/kafka.tgz -C /opt/kafka --strip-components=1"
    sshpass -p $PASS ssh -p $PORT $USER@$node "rm /tmp/kafka.tgz"

    echo "[*] Añadiendo variables al sistema..."
    sshpass -p $PASS ssh -p $PORT $USER@$node "echo 'export KAFKA_HOME=/opt/kafka' >> ~/.bashrc"
    sshpass -p $PASS ssh -p $PORT $USER@$node "echo 'export PATH=\${PATH}:\${KAFKA_HOME}/bin' >> ~/.bashrc"

    echo "[*] Añadiendo ajustes..."
    echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node"
    echo 'listeners=PLAINTEXT://0.0.0.0:9092' | sudo tee -a /opt/kafka/config/server.properties
    echo 'advertised.listeners=PLAINTEXT://10.0.3.10:9092' | sudo tee -a /opt/kafka/config/server.properties
"
}

install_kafka $1 # IP

