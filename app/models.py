#coding=utf8

import json
from flask import Flask
from flask import render_template
#from flask.ext.login import LoginManager
#from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
#login_manager = LoginManager()
#login_manager.setup_app(app)
#db = SQLAlchemy(app)


#class User(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(80), unique=True)
#    passwd = db.Column(db.String(120), unique=False)
#
#    def __init__(self, username, passwd):
#        self.username = username
#        self.secret = passwd
#
#    def __repr__(self):
#        return '<User %r>' % self.username


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/sizheninfo')
def sizheninfo():
    sizheninfoList = []
    sizheninfoList.append({})
    sizheninfoList.append({})

    sizheninfoList[0]["patientID"] = "s000001"
    sizheninfoList[0]["patientName"] = "1号病人"
    sizheninfoList[0]["connectedState"] = False
    sizheninfoList[0]["connectedAddinfoID"] = None

    sizheninfoList[1]["patientID"] = "s000002"
    sizheninfoList[1]["patientName"] = "2号病人"
    sizheninfoList[1]["connectedState"] = True
    sizheninfoList[1]["connectedAddinfoID"] = "a000002"

    return json.dumps(sizheninfoList)
