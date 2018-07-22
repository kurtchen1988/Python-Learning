from flask import Flask

from helper import models_to_dict

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@172.16.91.1:3306/testdb'


from model import db

db.init_app(app)


@app.route("/machine")
def machine():
    # data = [
    #     {"id": 1, "ip": "192.168.88.1", "name": "test1"},
    #     {"id": 2, "ip": "192.168.88.2", "name": "test3"},
    # ]
    #
    # from flask.json import jsonify
    # return jsonify(data)

    from model import Machine
    data = Machine.query.all()
    from flask import jsonify
    return jsonify(models_to_dict(data))


@app.route("/machine/create", methods=['POST'])
def machine_create():
    from flask.json import jsonify
    from flask import request
    print(request.form)

    from model import Machine
    model = Machine()
    model.name = request.form['name']
    model.ip = request.form['ip']
    model.user = request.form['user']
    model.password = request.form['password']

    if model.ip.strip() == '':
        return jsonify({"status": False, "data": "请输入IP地址"})

    db.session.add(model)
    db.session.commit()

    return jsonify({"status": True})


@app.route("/machine/delete")
def machine_delete():
    from flask.json import jsonify
    from flask import request
    from model import Machine

    model = Machine.query.get(request.args['id'])

    db.session.delete(model)
    db.session.commit()

    return jsonify({'status': True})


@app.route('/monitor')
def monitor():
    from flask import request
    from model import Machine

    machine = Machine.query.get(request.args['id'])

    import paramiko

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


@app.after_request
def after_filter(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE,PUT,'
    allow_headers = "Referer,Accept,Origin,User-Agent"
    response.headers['Access-Control-Allow-Headers'] = allow_headers

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
