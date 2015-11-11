#!/bin/bash
set -ex

sudo yum update -y 
sudo yum groupinstall -y Base
sudo yum groupinstall -y "Development Tools"

# Corosync
sudo cp centos.repo /etc/yum.repos.d/
sudo rpm --import http://ftp.jaist.ac.jp/pub/Linux/CentOS/RPM-GPG-KEY-CentOS-7
sudo yum --disablerepo=* --enablerepo=CentOS-7-Base install -y corosync corosynclib corosynclib-devel

# Sheepdog build dependencies
sudo rpm -ivh http://ftp.riken.jp/Linux/fedora/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
sudo yum install -y userspace-rcu userspace-rcu-devel
sudo yum install -y yasm yasm-devel
sudo yum install -y fuse fuse-devel

# ZooKeeper
sudo wget -O /etc/yum.repos.d/bigtop.repo http://www.apache.org/dist/bigtop/bigtop-1.0.0/repos/centos7/bigtop.repo
sudo yum install -y zookeeper-native
