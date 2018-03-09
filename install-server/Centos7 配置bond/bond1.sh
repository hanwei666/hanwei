#!/bin/bash

IP1=114.80.23.131
GATE=114.80.23.129
ETH1=enp8s0f0
ETH2=enp8s0f1


modprobe bonding
systemctl stop NetworkManager.service
systemctl disable NetworkManager.service

cat <<EOF> /etc/sysconfig/network-scripts/ifcfg-bond0
DEVICE=bond0
TYPE=Bond
NAME=bond0
BONDING_MASTER=yes
BOOTPROTO=static
USERCTL=no
ONBOOT=yes
IPADDR=$IP1
PREFIX=29
GATEWAY=$GATE
BONDING_OPTS="mode=1 miimon=100"
EOF



cat <<EOF> /etc/sysconfig/network-scripts/ifcfg-$ETH1
TYPE=Ethernet
BOOTPROTO=none
DEVICE=$ETH1
ONBOOT=yes
MASTER=bond0
SLAVE=yes
EOF

cat <<EOF> /etc/sysconfig/network-scripts/ifcfg-$ETH2
TYPE=Ethernet
BOOTPROTO=none
DEVICE=$ETH2
ONBOOT=yes
MASTER=bond0
SLAVE=yes
EOF



systemctl restart network
ping $GATE -c 1
reboot
