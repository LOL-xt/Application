from flask import Response
from flask import request
from flask import json
from .user import User
from .database import db, app


@app.route('/test')
def index():
    return "you are logged in"


@app.route('/update', methods=["POST"])
def update():
    ip = request.form['ip']
    name = request.form['name']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    country = request.form['country']
    city = request.form['city']
    mac = request.form['mac']
    try:
        db.session.query(User).filter(User.mac == mac).one()
        return Response("Device is already in database", status=200, mimetype='application/json')
    except:
        new_user = User(1, mac, ip, name, int(latitude), int(longitude), country, city)
        db.session.add(new_user)
        db.session.commit()
        return Response("Welcome " + name, status=200, mimetype='application/json')



