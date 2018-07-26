from flask import Flask, request, jsonify
from helper import models_to_dict
from flask.json import jsonify
from model import Machine, db, Monitor
import paramiko



app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/testdb'




db.init_app(app)


@app.route("/machine")
def machine():
# 展示所有机器


    #data = Machine.query.all()
    data = Monitor.query.all()
    return jsonify(models_to_dict(data))


@app.route("/machine/create", methods=['POST'])
def machine_create():
# 这里才是主控程序
    print(request.form)

    model = Machine()
    model.name = request.form['name']
    model.ip = request.form['ip']
    model.user = request.form['user']
    model.password = request.form['password']

    model2 = Monitor()
    model2.machine_id = request.form['ip']
    #model2.cpu = request.form['ip']
    #model2.memory = request.form['ip']
    #model2.harddrive = request.form['ip']


    if model.ip.strip() == '':
        return jsonify({"status": False, "data": "请输入IP地址"})

    db.session.add(model)
    db.session.commit()

    return jsonify({"status": True})


@app.route("/machine/delete")
def machine_delete():


    model = Machine.query.get(request.args['id'])

    db.session.delete(model)
    db.session.commit()

    return jsonify({'status': True})


@app.route('/monitor')
def monitor():


    machine = Machine.query.get(request.args['id'])
    #???


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
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE,PUT,'
    allow_headers = "Referer,Accept,Origin,User-Agent"
    response.headers['Access-Control-Allow-Headers'] = allow_headers

    return response


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
