#!/bin/bash

ifconfig enp0s8 down
ifconfig enp0s9 down
modprobe igb_uio
dpdk-devbind.py -b igb_uio 00:08.0
dpdk-devbind.py -b igb_uio 00:09.0
sleep 2


pktgen=/usr/local/bin/pktgen
echo 256 > /sys/devices/system/node/node0/hugepages/hugepages-2048kB/nr_hugepages
#${pktgen} -l 1-3 -n 2 --proc-type auto --file-prefix pg2 -- -T -P -j -m "[2].0"
${pktgen} -l 1-5 -n 2 --proc-type auto --file-prefix pg2 -- -T -P -j -m "[2-4].0,[3-5].1"