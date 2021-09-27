from flask import Response
from flask import request
from flask import json
from .user import User
from .database import db, app


@app.route('/test')
def index():
    return "you are logged in"


@app.post('/update')
def update():
    data = request.json
    ip = data['ip']
    name = data['name']
    latitude = data['latitude']
    longitude = data['longitude']
    country = data['country']
    city = data['city']
    mac = data['mac']
    try:
        db.session.query(User).filter(User.mac == mac).one()
        return Response("Device is already in database", status=200, mimetype='application/json')
    except:
        new_user = User(mac, ip, name, latitude, longitude, country, city)
        db.session.add(new_user)
        db.session.commit()
        return Response("Welcome " + name, status=200, mimetype='application/json')
