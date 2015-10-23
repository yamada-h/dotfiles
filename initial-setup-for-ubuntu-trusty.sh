#!/bin/bash
set -ex

#sudo apt-get update
#sudo apt-get upgrade -y 
#sudo apt-get remove -y nano
#sudo apt-get install -y vim 
#sudo apt-get install -y build-essential

# Sheepdog build dependencies
#sudo apt-get install -y yasm autoconf dh-autoreconf pkg-config
#sudo apt-get install -y liburcu-dev libzookeeper-mt-dev
#sudo apt-get install -y libcorosync-dev
sudo apt-get install -y dh-systemd devscripts
