#coding=utf8

from app import app
from flask import render_template
import json


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
