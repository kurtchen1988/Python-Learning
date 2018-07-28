#!/usr/bin/python3

# apt install -y python3-pip && pip3 install psutil
import json, psutil, re
# 用来查看硬件信息的脚步。此处的硬盘只能查看有误差的信息，因为用户有可能没把所有空间分区挂载。
res = {}

res['cpu_count'] = psutil.cpu_count()
res['memory_total'] = int(psutil.virtual_memory().total / 1024 / 1024)
res['hard_drive_total'] = str(int(int(psutil.disk_usage('/')[0])/1024/1024/1024))+'G'
res['cpu_percent'] = psutil.cpu_percent(1)
res['memory_percent'] = psutil.virtual_memory().percent

print(json.dumps(res))
