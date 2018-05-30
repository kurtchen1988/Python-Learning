import os

cmd="D:/Python35/python.exe D:/Python35/yzm/YDMPythonDemo.py"
r=os.popen(cmd)
captcha_value=r.read()
print(captcha_value)