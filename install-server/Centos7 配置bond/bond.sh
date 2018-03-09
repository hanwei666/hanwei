#!/bin/bash

IP1=192.168.80.100
IP2=192.168.80.101
GATE=192.168.80.1
ETH1=eno16777736
ETH2=eno33554960
ETH3=eno50332184
ETH4=eno67109408

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
PREFIX=24
GATEWAY=$GATE
BONDING_OPTS="mode=1 miimon=100"
EOF

cat <<EOF> /etc/sysconfig/network-scripts/ifcfg-bond1
DEVICE=bond1
TYPE=Bond
NAME=bond1
BONDING_MASTER=yes
BOOTPROTO=static
USERCTL=no
BOOTPROTO=none
IPADDR=$IP2
PREFIX=29
ONBOOT=yes
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
DEVICE=$ETH4
ONBOOT=yes
MASTER=bond0
SLAVE=yes
EOF

cat <<EOF> /etc/sysconfig/network-scripts/ifcfg-$ETH3
TYPE=Ethernet
BOOTPROTO=none
DEVICE=$ETH2
ONBOOT=yes
MASTER=bond1
SLAVE=yes
EOF

cat <<EOF> /etc/sysconfig/network-scripts/ifcfg-$ETH4
TYPE=Ethernet
BOOTPROTO=none
DEVICE=$ETH3
ONBOOT=yes
MASTER=bond1
SLAVE=yes
EOF

systemctl restart network
ping $GATE -c 1
reboot
