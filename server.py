from flask import Response
from flask import request
from flask import json
from user import User
from database import db, app


@app.route('/test')
def index():
    return "you are logged in"


if __name__ == '__main__':
    app.run()
