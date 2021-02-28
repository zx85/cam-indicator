from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy,event
from sqlalchemy import create_engine

# Do setup in case it's needed
dbFilename = "indicator.db"
sqliteString="sqlite:///"+dbFilename
app = Flask(__name__)
app.config['SECRET_KEY'] = '1628bb0b13ce0c676dfde280ba24a579'
app.config['SQLALCHEMY_DATABASE_URI'] = sqliteString
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class States(db.Model):
    Indicator = db.Column(db.String(20), unique=True, primary_key=True)
    State = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return ("Presets("+str(self.id)+", '"+str(self.Label)+"')")

# if the DB isn't there create it
if not os.path.isfile("cam_indicator/"+dbFilename) :
    print ("Creating DB")
    db.create_all()
    db.session.add(States(Indicator="audio",State=0))
    for eachCam in range(1, 6):
        db.session.add(States(Indicator="cam"+str(eachCam),State=0))
    db.session.commit()

from cam_indicator import routes