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
Base.prepare(autoload_with=engine)

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
            "Available Routes:"
            f"/api/v1.0/precipitation"
            f"/api/v1.0/stations"
            f"/api/v1.0/tobs"
            f"/api/v1.0/<start>"
            f"/api/v1.0/<start>/<end>"
        )

@app.route("/api/v1.0/precipitation")
def precipitation():

    session = Session(engine)
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(measuring_table.date, measuring_table.prcp).filter(measuring_table.date >= prev_year).all()
    precipitation_dict = {date: prcp for date, prcp in results}
    return jsonify(precipitation_dict)
#"To see all the prcp data from 2016 run the link http://127.0.0.1:5000/api/v1.0/precipitation in the browser"

@app.route("/api/v1.0/stations")
def stations():
     station_names = session.query(station_table.station).all()
     stations = list(np.ravel(station_names))
     return jsonify (station_names = stations)
#"To get the name of the stations run the link http://127.0.0.1:5000/api/v1.0/stations"

@app.route("/api/v1.0/tobs")
def temp():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    temp_results= session.query(measuring_table.tobs).\
    filter(measuring_table.station == 'USC00519281').\
    filter(measuring_table.date >= prev_year).all()
    temperature = list(np.ravel(temp_results))
    return jsonify(temperature = temperature)
#"To see the temperature values run the link http://127.0.0.1:5000//api/v1.0/tobs"

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def statistics(start, end=None):
    session = Session(engine)
#Start Route
    sel = [func.min(measuring_table.tobs), func.avg(measuring_table.tobs), func.max(measuring_table.tobs)]
    if not end:
        # When only the start date is provided
        results = session.query(*sel).filter(measuring_table.date >= start).all()
    else:
        # When both the start and end dates are provided
        results = session.query(*sel).filter(measuring_table.date >= start).filter(measuring_table.date <= end).all()
    
    session.close()
    
    # Convert results to a list
    temps = list(np.ravel(results)) if results else []
    return jsonify(temps=temps)
#run link: http://127.0.0.1:5000/api/v1.0/2017-08-01/2017-08-05 for example, it gives the min,average and max prcp results respectively
#last date in the set = 2017, 8, 23
 
if __name__ == "__main__":
    app.run(debug=True)