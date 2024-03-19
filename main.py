from flask import Flask, request, jsonify, render_template
import json
from flask_cors import CORS
from threading import Thread
import time

app = Flask(__name__)
CORS(app)

# Data dummy
data = []


def post_data_thread(req_data):
  if req_data:  # Check if data exists to prevent unnecessary writes
    data.append(req_data)
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
  return jsonify({"data": data})


@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)  # Bind to all interfaces
