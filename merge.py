#!/usr/bin/python3

import datetime as dt
import requests
from datetime import timedelta, datetime

d = datetime.today() - timedelta(days=30)

current_mounth = dt.datetime.today()
current_mounth = current_mounth.strftime("%Y_%m")
before_mounth = d.strftime("%Y_%m")

print(current_mounth, before_mounth)

urlvm = 'http://victoriametrics:8248/'
merge = requests.post(f"{urlvm}/internal/force_merge?partition_prefix={before_mounth}", auth=('user', '********'))
merge = requests.post(f"{urlvm}/internal/force_merge?partition_prefix={current_mounth}", auth=('user', '********'))
print(merge)
