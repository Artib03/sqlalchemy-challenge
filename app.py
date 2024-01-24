# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import datetime as dt
import numpy as np
import pandas as pd
from flask import Flask, jsonify
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect = True)

# Save references to each table
measuring_table = Base.classes.measurement
station_table = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
        return (
            f"/api/v1.0/precipitation"
            f"/api/v1.0/stations"
            f"/api/v1.0/tobs"
            f"/api/v1.0/<start>"
            f"/api/v1.0/<start>/<end>"
        )

#@app.route("/api/v1.0/precipitation")
#def precipitation():

    #session = Session(engine)
    #prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #results = session.query(measuring_table.date, measuring_table.prcp).filter(measuring_table.date >= prev_year).all()
    #precipitation_dict = {date: prcp for date, prcp in results}
    #return jsonify(precipitation_dict)

#@app.route("/api/v1.0/stations")
#def stations():
     #results2 = session.query(station_table.station).all()
     #stations = list(results2)
     #return jsonify (stations = stations)

#@app.route("/api/v1.0/tobs")
#def temp():
    #prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #results3 = session.query(measuring_table.tobs).\
    #filter(measuring_table.station == 'USC00519281').\
    #filter(measuring_table.date >= prev_year).all()
    #temperature = list((results3))
    #return jsonify(temperature = temperature)

#@app.route("/api/v1.0/<start>")
#@app.route("/api/v1.0/<start>/<end>")
#def statistics(start=None, end=None):

    #station_id = [func.min(measuring_table.tobs), func.avg(measuring_table.tobs), func.max(measuring_table.tobs)]
    #if not end:
        #results = session.query(station_id).\
            #filter(measuring_table.date >= start).\
            #filter(measuring_table.date <= end).all()
        #temps = list((results))
        #return jsonify(temps)
    #results = session.query(station_id).\
        #filter(measuring_table.date >= start).\
        #filter(measuring_table.date <= end).all()
    #temps = list((results))
    #return jsonify(temps=temps)
    
if __name__ == "__main__":
    app.run(debug=True)