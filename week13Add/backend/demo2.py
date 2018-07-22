from flask import Flask, jsonify, request

from helper import models_to_dict
from model import db, Machine

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@172.16.91.1:3306/testdb'
db.init_app(app)


@app.route("/machine")
def machine():
    # data = [
    #    {'id': 1, 'ip': '192.168.8.8', 'name': 'root', 'password': '1234'},
    #    {'id': 2, 'ip': '192.168.8.9', 'name': 'root', 'password': '1234'},
    #    {'id': 3, 'ip': '192.168.8.10', 'name': 'root', 'password': '1234'},
    # ]

    data = Machine.query.all()

    return jsonify(models_to_dict(data))


@app.route("/machine/create", methods=['POST'])
def machine_create():
    print(request.form)

    model = Machine()
    model.name = request.form['name']
    model.ip = request.form['ip']
    model.user = request.form['user']
    model.password = request.form['password']

    if model.ip.strip() == '':
        return jsonify({"status": False, "data": "请输入IP"})

    db.session.add(model)
    db.session.commit()

    return jsonify({"status": True, "data": ""})


@app.route("/machine/delete")
def machine_delete():

    mid = request.args['id']
    model = Machine.query.get(mid)

    db.session.delete(model)
    db.session.commit()

    return jsonify({"status": True, "data": ""})


@app.route('/monitor')
def monitor():
    res = {
        'cpu_count': 1,
        'cpu_percent': '10',
        'memory_total': '1024',
        'memory_percent': '70',
    }

    return jsonify(res)


@app.after_request
def after_filter(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE,PUT,'
    allow_headers = "Referer,Accept,Origin,User-Agent"
    response.headers['Access-Control-Allow-Headers'] = allow_headers

    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
