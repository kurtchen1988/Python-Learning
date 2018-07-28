from flask import Flask, request, jsonify
from helper import models_to_dict
from flask.json import jsonify
from model import Machine, db, Monitor
import paramiko



app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/testdb'

'''
# 初始化role 并插入数据库
test_role1 = role(6, 'supervisol', '超超超超级管理员哦')
test_role2 = role(7, 'your try', '你试试哦')
db.session.add(test_role1)
db.session.add(test_role2)
db.session.commit()

#查询数据库
db.session.query(role).filter_by(id=2).first()  # 查询role表中id为2的第一个匹配项目，用".字段名"获取字段值
db.session.query(role).all()  # 得到一个list，返回role表里的所有role实例
db.session.query(role).filter(role.id == 2).first() # 结果与第一种一致
# 获取指定字段，返回一个生成器 通过遍历来完成相关操作, 也可以强转为list
db.session.query(role).filter_by(id=2).values('id', 'name', 'name_cn')
# 模糊查询
db.session.query(role).filter(role.name_cn.endswith('管理员')).all()  # 获取role表中name_cn字段以管理员结尾的所有内容
# 修改数据库内容
user = db.session.query(role).filter_by(id=6).first()  # 将role表中id为6的name改为change
user.name = 'change'
db.session.commit()
'''

db.init_app(app)


@app.route("/machine")
def machine():
# 展示所有机器
    #server = Machine.query.all()
    data = Monitor.query.all()
    server = Machine.query.all()
    #data2 = Monitor.query.filter_by("machine_id").values('ip')
    #data3 = Monitor.query.all()
    #print(models_to_dict(data)[0].get('id'))
    #print(models_to_dict(data3))

    #data = Monitor.query.all()
    print(server)
    if(ping(server.ip,server.user,server.password)):
        status = '运行中'
    else:
        status = '不在线'
    print(data)
    data = data['status'] = status

    d = models_to_dict(data)
    print(d)
    return jsonify(models_to_dict(data))


@app.route("/machine/create", methods=['POST'])
def machine_create():
# 添加机器
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
    model2 = Monitor.query.get(request.args['id'])

    db.session.delete(model)
    db.session.delete(model2)
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
