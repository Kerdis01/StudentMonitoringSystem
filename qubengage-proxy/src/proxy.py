from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import threading
from pathlib import Path
import json
import os
import time
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
CORS(app)

# This will store our service routes
service_routes = {}
config_path = Path(__file__).resolve().parent.parent / 'config.json'

# Load the configuration from a file
def load_configuration():
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        service_routes.update(config)
    except FileNotFoundError:
        print("Configuration file not found.")

# Watch for changes in the configuration file and reload if necessary
def watch_configuration():
    last_mtime = None
    while True:
        try:
            mtime = os.path.getmtime(config_path)
            if mtime != last_mtime:
                print("Configuration has changed. Reloading...")
                load_configuration()
                last_mtime = mtime
        except FileNotFoundError:
            print("Configuration file not found.")
        time.sleep(5)  # check every 5 seconds

# This thread will watch for configuration changes
config_watcher_thread = threading.Thread(target=watch_configuration, daemon=True)
config_watcher_thread.start()

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    # Extract the base path to find the service mapping
    base_path = '/' + path.split('/')[0]
    if base_path in service_routes:
        # Get the actual service URL from the config
        service_url = service_routes[base_path].get(request.method)
        if service_url:
            try:
                # Forward the request to the service and get the response
                headers = {key: value for (key, value) in request.headers if key != 'Host'}
                service_response = requests.request(
                    method=request.method,
                    url=service_url + path[len(base_path):],  # Append the rest of the path
                    headers=headers,
                    params=request.args,
                    data=request.get_data(),
                    allow_redirects=False
                )
                # Return the response received from the service
                response = app.response_class(
                    response=service_response.content,
                    status=service_response.status_code,
                    headers=dict(service_response.headers)
                )
                return response
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                return jsonify({'error': 'Internal server error'}), 500
        else:
            return jsonify({'error': 'Method not allowed'}), 405
    else:
        return jsonify({'error': 'Service not found'}), 404

# Custom error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

if __name__ == '__main__':
    load_configuration()  # Initial configuration load
    app.run(host='0.0.0.0', debug=True, port=9000)
