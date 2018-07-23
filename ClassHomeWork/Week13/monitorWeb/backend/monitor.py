#!/usr/bin/python3

# apt install -y python3-pip && pip3 install psutil
import json, psutil, re

res = {}

res['cpu_count'] = psutil.cpu_count()
res['memory_total'] = int(psutil.virtual_memory().total / 1024 / 1024)
res['hard_drive_total'] = int(int(re.findall('total=(.*?),',str(psutil.disk_usage('/')))[0])/ 1024 / 1024)
res['cpu_percent'] = psutil.cpu_percent(1)
res['memory_percent'] = psutil.virtual_memory().percent

print(json.dumps(res))
