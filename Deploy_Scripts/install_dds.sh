#!/bin/bash
source common.sh

RTI_WORKSPACE_DIR="/home/$USER/rti_workspace/7.5.0"

install_dds() {
    local node=$1

    echo "[*] Instalando en $USER:$node"

    # Configurar repositorio RTI
    echo "[*] Descargando claves del repositorio de RTI..."
    echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo curl -sSL -o /usr/share/keyrings/rti-official-archive.gpg https://packages.rti.com/deb/official/repo.key"
    echo "[*] Añadiendo repositorio APT..."
    echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "echo 'deb [arch=$(dpkg --print-architecture), signed-by=/usr/share/keyrings/rti-official-archive.gpg] https://packages.rti.com/deb/official jammy main' | sudo tee /etc/apt/sources.list.d/rti.list > /dev/null"

    # Aceptar licencia y actualizar
    echo "[*] Actualizando repositorios..."
    echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo apt-get update"
    echo "[*] Instalando RTI Connext..."
    echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo apt-get install -y rti-connext-dds-7.5.0 curl gnupg git cmake build-essential default-jdk"

    # Crear carpeta de trabajo
    echo "[*] Creando Workspace..."
	sshpass -p $PASS ssh -p $PORT $USER@$node "mkdir -p $RTI_WORKSPACE_DIR"

    # Copiar licencia si existe
    echo "[*] Copiando licencia..."
    sshpass -p $PASS scp -P $PORT ./rti_license.dat $USER@$node:$RTI_WORKSPACE_DIR/

    # Clonar y compilar Gateway
    echo "[*] Clonando Gateway..."
    echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "sudo git clone --recurse-submodule https://github.com/rticommunity/rticonnextdds-gateway.git /opt/rti.com/rti_connext_dds-7.5.0/rticonnextdds-gateway"

    echo "[*] Compilando Gateway y librerias..."
    echo $PASS | sshpass -p $PASS ssh -tt -p $PORT $USER@$node "cd /opt/rti.com/rti_connext_dds-7.5.0/rticonnextdds-gateway && sudo mkdir -p build && cd build && sudo cmake .. -DCONNEXTDDS_DIR=/opt/rti.com/rti_connext_dds-7.5.0  -DCMAKE_INSTALL_PREFIX=../install && sudo cmake --build . --target install"
    
    # Establecer variables de entorno
    echo "[*] Estableciendo variable DDSHOME"
    sshpass -p $PASS ssh -tt -p $PORT $USER@$node "echo 'export NDDSHOME=/opt/rti.com/rti_connext_dds-7.5.0' >> ~/.bashrc"
    echo "[*] Estableciendo variables de entorno para librerias..."
    sshpass -p $PASS ssh -p $PORT $USER@$node "echo 'export LD_LIBRARY_PATH=\$NDDSHOME/rticonnextdds-gateway/install/lib:\$NDDSHOME/lib/x64Linux4gcc7.3.0:\$LD_LIBRARY_PATH' >> ~/.bashrc"
    echo "[*] Añadiendo RTI al PATH..."
	sshpass -p $PASS ssh -p $PORT $USER@$node "echo 'export PATH=\${PATH}:/opt/rti.com/rti_connext_dds-7.5.0/bin' >> ~/.bashrc"
    
}

for_each_node install_dds
