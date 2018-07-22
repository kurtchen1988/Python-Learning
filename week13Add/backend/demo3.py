import paramiko

ip = '172.16.91.166'
user = 'root'
password = 'root'
port = 22

# 远程主机上执行命令
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # 允许连接不在know_hosts文件中的主机
ssh.connect(hostname=ip, username=user, password=password, port=port)
command = "lscpu | awk '/^CPU\(s\)/{print $2}'"
stdin, stdout, stderr = ssh.exec_command(command)
res = stdout.read().decode()
print("cpu:" + res)
ssh.close()

# 远程文件传输
transport = paramiko.Transport((ip, port))
transport.connect(username=user, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

# 将当前目录中的1.txt上传到远程主机
sftp.put('./1.txt', '/tmp/2.txt')

# 从远程主机下载文件到当前目录
sftp.get('/tmp/2.txt', './3.txt')

# 列出目录
print(sftp.listdir(path='/'))

sftp.close()
transport.close()