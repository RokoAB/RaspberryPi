import numpy as np
import threading
from flask import Flask, request, jsonify

# === FLASK SERVER ===
app = Flask(__name__)

#using POST method to receive messages from clients 
@app.route('/trigger', methods=['POST'])
def receive_trigger():
    global laptop_trigger
    data = request.get_json()
    if data and "trigger" in data and data.get("source") == "laptop":
        with lock:
            laptop_trigger = bool(data["trigger"])
            print(f" Laptop trigger received: {laptop_trigger}")
        return jsonify({"status": "received"}), 200
    return jsonify({"error": "Invalid data"}), 400

def run_server():
    app.run(host='0.0.0.0', port=5432)

#start Flask server in background thread
#allows multithreading if the code needs to do something else while listening in this thread 
server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()