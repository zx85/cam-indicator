from flask import render_template, url_for, flash, redirect, request
from camctrl import app,db,States
import camcmds

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/set")
def setdb():
    device= request.args.get('device', 'audio')
    state= request.args.get('state',1)
    StatesDB=States.query.filter_by(Indicator=device).first()
    StatesDB.State=int(state)
    StatesDB=States.query.filter_by(Indicator=device).first()
    return StatesDB.Indicator+" is: "+StatesDB.State

# Reserved for cameras - returns the audio & appropriate camera state comma separated
# cam,audio
@app.route("/get/<cam>")
def getdb(cam):
    device="cam"+cam
    StatesDB=States.query.filter_by(Indicator=device).first()
    State=str(StatesDB.State)
    StatesDB=States.query.filter_by(Indicator='audio').first()
    Audio=str(StatesDB.State)
    return State+","+Audio

@app.route("/getall")
def getalldb():
    StatesDB=States.query.all())
    StatesOutput=""
    for eachIndicator in StatesDB:
        StatesOutput=StatesOutput+StatesDB.Indicator+","+str(StatesDB.State)+"|"
    return presetOutput
