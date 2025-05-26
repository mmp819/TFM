#!/bin/bash

USER="vm-1"
PASS="root"
REMOTE_DIR="/home/$USER/tfm"
SSH_OPTS="-o StrictHostKeyChecking=no"
PORT=3022

for_each_node() {
    while read node; do
        echo -e "\n[*] Ejecutando en $node"
        "$@" "$node"
    done < nodes.txt
}
