from flask import render_template, url_for, flash, redirect, request
from cam_indicator import app,db,States

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/set")
def setdb():
    device= request.args.get('device', 'audio')
    state= request.args.get('state',1)
# Clear down the current ones
    if state=="1" and "cam" in device:
        ZeroCandidates=States.query.filter(States.Indicator.like('cam%')).all()
        for eachIndicator in ZeroCandidates:
            eachIndicator.State=0
# Then update the new one
    StatesDB=States.query.filter_by(Indicator=device).first()
    StatesDB.State=int(state)
    db.session.commit()
    StatesDB=States.query.filter_by(Indicator=device).first()
    return StatesDB.Indicator+" is: "+str(StatesDB.State)

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
    StatesDB=States.query.all()
    StatesOutput=""
    for eachIndicator in StatesDB:
        StatesOutput=StatesOutput+eachIndicator.Indicator+","+str(eachIndicator.State)+"|"
    return StatesOutput
