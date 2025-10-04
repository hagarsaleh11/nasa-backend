from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load both CSV files
df_combined = pd.read_csv("combined_countries.csv")
df_filtered = pd.read_csv("filtered_countries.csv")

@app.route("/")
def home():
    return "NASA Backend with multiple datasets is running! 🚀"

@app.route("/combined")
def get_combined():
    return jsonify(df_combined.to_dict(orient="records"))

@app.route("/filtered")
def get_filtered():
    return jsonify(df_filtered.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
