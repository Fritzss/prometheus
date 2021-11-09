#!/usr/bin/python3

import requests
import socket

hostname = socket.gethostname()
urlprom = socket.gethostbyname(hostname)

urlvm = 'http://victoriametrics:8248/'
snapshot = (requests.post(f"http://{urlprom}/api/v1/admin/tsdb/snapshot", auth=('user', '********')).json())
snapshot = snapshot['data']['name']
snapshot = f'/opt/prometheus/data/snapshots/{snapshot}/'

print(snapshot)
