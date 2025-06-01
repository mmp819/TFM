#!/bin/bash
source common.sh

set -o errexit

install_monitoring() {
    local node=$1

    echo "[*] Instalando Prometheus y Grafana en $USER@$node"

    # Prometheus
    echo "[*] Descargando e instalando Prometheus..."
    sshpass -p $PASS ssh -tt -p $PORT $USER@$node "wget https://github.com/prometheus/prometheus/releases/download/v2.53.4/prometheus-2.53.4.linux-amd64.tar.gz -O /tmp/prometheus.tar.gz"
    echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo mkdir -p /opt/prometheus"
    echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo tar -xzf /tmp/prometheus.tar.gz -C /opt/prometheus --strip-components=1"
    sshpass -p $PASS ssh -p $PORT $USER@$node "rm /tmp/prometheus.tar.gz"

    echo "[*] Añadiendo Prometheus al PATH..."
    sshpass -p $PASS ssh -p $PORT $USER@$node "echo 'export PROMETHEUS_HOME=/opt/prometheus' >> ~/.bashrc"
    sshpass -p $PASS ssh -p $PORT $USER@$node "echo 'export PATH=\$PATH:\$PROMETHEUS_HOME' >> ~/.bashrc"
    sshpass -p $PASS scp -P $PORT ../Simulation/Monitoring/Prometheus/prometheus.yml $USER@$node:/home/$USER/
    echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo mv /home/$USER/prometheus.yml /opt/prometheus/"

    # Grafana
    echo "[*] Añadiendo repositorio de Grafana..."
	echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo apt-get install -y apt-transport-https software-properties-common wget"

	echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo mkdir -p /etc/apt/keyrings"

	echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "wget -q -O - https://apt.grafana.com/gpg.key | gpg --dearmor | sudo tee /etc/apt/keyrings/grafana.gpg > /dev/null"

	echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "echo 'deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main' | sudo tee -a /etc/apt/sources.list.d/grafana.list"

	echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo apt-get update"

	echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo apt-get install -y grafana"

    echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo grafana-cli plugins install hamedkarbasi93-kafka-datasource"
}

install_monitoring $1 # IP

