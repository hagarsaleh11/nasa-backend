from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "NASA Backend with multiple datasets is running! 🚀"


from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "NASA Backend with multiple datasets is running! 🚀"

# Route for combined_countries.csv
@app.route("/combined")
def get_combined():
    df = pd.read_csv("combined_countries.csv")
    return df.to_json(orient="records")

# Route for filtered_countries.csv
@app.route("/filtered")
def get_filtered():
    df = pd.read_csv("filtered_countries.csv")
    return df.to_json(orient="records")

if __name__ == "__main__":
    app.run(debug=True)
