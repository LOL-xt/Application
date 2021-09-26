from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yvfctofzlacjco:9bfd0804305d837b8319bc12af8e0c156e8af3f148b7f93c7d556e174ffa608c@ec2-54-216-48-43.eu-west-1.compute.amazonaws.com:5432/d2lgih4j5md8qu'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_POOL_SIZE"] = 20
db = SQLAlchemy(app)
