import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def names():
    """Return the precipitation data as json"""
    # Query all precipitation
    session = Session(engine)
    results = session.query(Measurement.prcp).all()

        # Convert list of tuples into normal list
    precip = list(np.ravel(results))
    return jsonify(precip)


@app.route("/api/v1.0/stations")
def stations():
    """Return stations data as json"""
    # Query all stations
    session = Session(engine)
    results = session.query(func.count(Station.id)).all()

    all_stations = list(np.ravel(results))
    return jsonify(results)

#@app.route("/api/v1.0/tobs")
#def temps():
    """Return a JSON list of Temperature Observations (tobs) for the previous year."""
    # Query for the dates and temperature observations from a year from the last data point.
#    session = Session(engine)
#    results = session.query(ltm_prcp = session.query(Measurement.date, Measurement.prcp).\
#        filter(Measurement.date.between(year_ago, latest_date))

    # Return a JSON list of Temperature Observations (tobs) for the previous year.

#    return jsonify(results)

if __name__ == '__main__':
    app.run()
