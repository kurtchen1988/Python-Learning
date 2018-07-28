from flask import Flask, request, jsonify
from helper import models_to_dict
from flask.json import jsonify
from model import Machine, db, Monitor
import paramiko, re, json



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/testdb'
# 在此设置数据库连接
db.init_app(app)
id = None

@app.route("/machine")
def machine():
    '''
    显示机器，同时对每个机器都会进行连接操作，如果成功就显示运行中，不成功就显示不在线
    :return: 所有机器信息的json
    '''

    data = Monitor.query.all()
    server = Machine.query.all()
    dictMonitor = models_to_dict(data)
    dictServer = models_to_dict(server)

    for mon in range(0,len(dictMonitor)):

        dictMonitor[mon]['ip']=dictServer[mon]['ip']
        if(ping(getVal(dictServer[mon],'ip'),getVal(dictServer[mon],'user'),getVal(dictServer[mon],'password'))):
            dictMonitor[mon]['status']='运行中'
        else:
            dictMonitor[mon]['status'] = '不在线'

    #print(dictMonitor)
    return jsonify(dictMonitor)

def getVal(dict, key):

    return dict.get(key)

@app.route("/machine/create", methods=['POST'])
def machine_create():
    '''
    添加机器，同时在两张表里插入数据，机器的CPU，硬盘和内存是通过调用方法直接从机器中取出信息
    :return: 当IP地址没输入的时候返回报错json，成功录入返回正确json
    '''
    print(request.form)

    model = Machine()
    model.name = request.form['name']
    model.ip = request.form['ip']
    model.user = request.form['user']
    model.password = request.form['password']


    model2 = Monitor()
    model2.machine_id = request.form['name']
    model2.cpu = getCPU(request.form['ip'],request.form['user'],request.form['password'])

    model2.memory = str(getDriveMemory(request.form['ip'],request.form['user'],request.form['password']).get('memory_total'))+'M'
    model2.harddrive = getDriveMemory(request.form['ip'],request.form['user'],request.form['password']).get('hard_drive_total')


    if model.ip.strip() == '':
        return jsonify({"status": False, "data": "请输入IP地址"})


    db.session.add(model)
    db.session.add(model2)
    db.session.commit()

    return jsonify({"status": True})

def getCPU(ip, user, passwd):
    '''
    拿到CPU具体型号，使用系统命令获得并通过正则筛选数据
    :param ip: 服务器ip地址
    :param user: 服务器用户名
    :param passwd: 服务器密码
    :return: CPU具体型号的字符串
    '''
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, username=user, password=passwd, port=22)

    command = "dmidecode -s processor-version"
    stdin, stdout, stderr = ssh.exec_command(command)
    res = stdout.read().decode()
    a = re.findall('.*\n', res)[0]
    ssh.close()
    return a

def getDriveMemory(ip, user, passwd):
    '''
    复用监控代码，通过上传脚本拿到机器的硬盘和内存信息
    :param ip: 服务器ip地址
    :param user: 服务器用户名
    :param passwd: 服务器密码
    :return: 转换成字典的机器信息
    '''
    # 远程文件传输
    transport = paramiko.Transport((ip, 22))
    transport.connect(username=user, password=passwd)
    sftp = paramiko.SFTPClient.from_transport(transport)

    # 上传到远程主机
    sftp.put('./monitor.py', '/tmp/monitor.py')
    sftp.close()
    transport.close()

    # 远程主机上执行命令
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
    ssh.connect(hostname=ip, username=user, password=passwd, port=22)

    command = "python3 /tmp/monitor.py && rm -f /tmp/monitor.py"
    stdin, stdout, stderr = ssh.exec_command(command)
    res = stdout.read().decode()


    ssh.close()

    return json.loads(res)

@app.route("/machine/delete")
def machine_delete():
    '''
    删除机器信息，从机器和监控两个表中一同删除机器信息
    :return: 删除成功返回键为status，值为True的字典
    '''

    model = Machine.query.get(request.args['id'])
    model2 = Monitor.query.get(request.args['id'])

    db.session.delete(model)
    db.session.delete(model2)
    db.session.commit()

    return jsonify({'status': True})

@app.route("/machine/edit")
def machine_edit():
    '''
    修改机器信息，首先展示机器的信息在表格中，拿到机器的id号，根据id号在数据库中查询
    :return: 机器信息的json
    '''

    model = Machine.query.get(request.args['id'])


    return jsonify({'id':model.id,'name': model.name,'ip':model.ip,'user':model.user,'password':model.password})

@app.route("/machine/edit", methods=['POST'])
def machine_edit_post():
    '''
    修改机器信息，从两个表中一同修改机器信息。机器的cpu，内存以及硬盘信息重新从机器调取
    :return: 如果没输入ip地址，返回失败信息json，如果成功修改，返回成功信息json
    '''

    model = Machine.query.get(request.form['id'])
    model.name = request.form['name']
    model.ip = request.form['ip']
    model.user = request.form['user']
    model.password = request.form['password']

    model2 = Monitor.query.get(request.form['id'])
    model2.machine_id = request.form['name']
    model2.cpu = getCPU(request.form['ip'], request.form['user'], request.form['password'])

    model2.memory = str(
        getDriveMemory(request.form['ip'], request.form['user'], request.form['password']).get('memory_total')) + 'M'
    model2.harddrive = getDriveMemory(request.form['ip'], request.form['user'], request.form['password']).get(
        'hard_drive_total')

    if model.ip.strip() == '':
        return jsonify({"status": False, "data": "请输入IP地址"})

    db.session.commit()

    return jsonify({'status': True})

@app.route('/monitor')
def monitor():
    '''
    实时监控cpu使用率和内存使用率
    :return:
    '''
    machine = Machine.query.get(request.args['id'])


    # 远程文件传输
    transport = paramiko.Transport((machine.ip, 22))
    transport.connect(username=machine.user, password=machine.password)
    sftp = paramiko.SFTPClient.from_transport(transport)

    # 上传到远程主机
    sftp.put('./monitor.py', '/tmp/monitor.py')
    sftp.close()
    transport.close()

    # 远程主机上执行命令
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
    ssh.connect(hostname=machine.ip, username=machine.user, password=machine.password, port=22)

    command = "python3 /tmp/monitor.py && rm -f /tmp/monitor.py"
    stdin, stdout, stderr = ssh.exec_command(command)
    res = stdout.read().decode()
    print(res)

    ssh.close()


    return res


def ping(ip, username, password):
    '''用ssh尝试链接主机，如果没报错证明已经连接上'''
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, username=username, password=password, port=22)
    except Exception:
        return False
    else:
        return True


@app.after_request
def after_filter(response):
    '''设置允许的网页操作'''
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE,PUT,'
    allow_headers = "Referer,Accept,Origin,User-Agent"
    response.headers['Access-Control-Allow-Headers'] = allow_headers

    return response


if __name__ == '__main__':
    '''入口程序'''
    app.run(host='localhost', port=5000, debug=True)
