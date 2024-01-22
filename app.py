# Import the dependencies.
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# reflect an existing database into a new model

# reflect the tables

# Save references to each table

# Create our session (link) from Python to the DB

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def systems():
        return (
            f"/api/v1.0/precipitation"
            f"/api/v1.0/stations"
            f"/api/v1.0/tobs"
            f"/api/v1.0/<start>"
            f"/api/v1.0/<start>/<end>"
        )


@app.route("/api/v1.0/precipitation")

@app.route("/api/v1.0/stations")

@app.route("/api/v1.0/<start>")

@app.route("/api/v1.0/<start>/<end>")


if __name__ == "__main__":
    app.run(debug=True)