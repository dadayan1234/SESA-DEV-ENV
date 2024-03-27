from flask import Flask, request, jsonify, render_template
from datetime import datetime
import json
from flask_cors import CORS
from threading import Thread
import time

app = Flask(__name__)
CORS(app)

# Data dummy
data = []

@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html")
  
@app.route("/dashboard")
def dashboard():
  return render_template("dashboard.html")

@app.route("/dashboard_adv")
def dashboard_adv():
  return render_template("advanced.html")
  
def post_data_thread(req_data):
  if req_data:  # Check if data exists to prevent unnecessary writes
      with open("data.json", "r") as f:
          data = json.load(f)
      req_data["timestamp"] = datetime.now().isoformat()
      data["data"].append(req_data)  # Menambahkan data ke dalam "data" array
      with open("data.json", "w") as f:
          json.dump(data, f)
      print(f"Data received and saved: {req_data}")

@app.route("/post", methods=["POST"])
def post_data():
  req_data = request.get_json()
  thread = Thread(target=post_data_thread, args=(req_data, ))
  thread.start()
  return jsonify({"success": True})

@app.route("/get", methods=["GET"])
def get_data():
  with open("data.json", "r") as f:
      data = json.load(f)
  return jsonify(data)  # Mengembalikan seluruh data dari "data.json"

@app.route("/get_data", methods=["GET"])
def get_data_2():
    with open("data.json", "r") as f:
        data = json.load(f)

    # Mengambil data terakhir dari data.json
    latest_data = data["data"][-1] if data["data"] else {}

    return jsonify(latest_data)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)  # Bind to all interfaces
