#!/bin/bash
snap=$(./sync.py)
thread=$(nproc)
echo $snap
/opt/prometheus/vmctl prometheus --vm-concurrency=$thread --vm-addr=http://victoriametrics:8248/ --vm-user="vmuser" --vm-password="Password"  --prom-snapshot=$snap -s
/usr/bin/rm -rf /opt/prometheus/data/snapshots/*
