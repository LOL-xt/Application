from flask import Response
from flask import request
from flask import send_file
from flask import Flask
from .URLs import *
import os

app = Flask(__name__)

@app.route('/keylogger', methods=["GET", "POST"])
def check_word():
    word = request.args.get('char').lower()
    if word != 'delete':
        add_content(word)
    else:
        backspace()
        
    string_content = get_content()
    
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

def add_content(word):
    string_file = open('./string_data', 'a')
    string_file.write(word)
    string_file.close()

def delete_content():
    string_file = open('./string_data', 'w')
    string_file.write('')
    string_file.close()
    
def get_content():
    string_file = open('./string_data', 'r')
    string_content = string_file.read()
    string_file.close()
    return string_content

def override_content(string_content):
    string_file = open('./string_data', 'w')
    string_file.write(string_content)
    string_file.close()

def backspace():
    string_file = open('./string_data', 'rb+')
    string_file.seek(-1, os.SEEK_END)
    string_file.truncate()







