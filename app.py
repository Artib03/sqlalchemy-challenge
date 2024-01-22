# Import the dependencies.
from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import datetime as dt

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#################################################
# Database Setup
#################################################

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)
#Base.classes.keys()

# Save references to each table
measuring_table = Base.classes.measurement
station_table = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(bind=engine)
session.commit()

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

@app.route("/api/v1.0/precipitation")
def precipitation():

    session = Session(engine)

    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(measuring_table.date, measuring_table.prcp).filter(measuring_table.date >= prev_year).all()

    session.close()

    output = []
    for record in results:
        output.append(record.prcp)

    return jsonify(output)


@app.route("/api/v1.0/stations")
def stations():

@app.route("/api/v1.0/tobs")

@app.route("/api/v1.0/<start>")

@app.route("/api/v1.0/<start>/<end>")


if __name__ == "__main__":
    app.run(debug=True)