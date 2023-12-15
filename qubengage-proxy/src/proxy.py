from flask import Flask, request, jsonify, redirect
from pathlib import Path
import os
import requests
import threading
import json
import time

app = Flask(__name__)

# This will store our service routes
service_routes = {}

# Load the configuration from a file
def load_configuration():
    # Construct the path to the config.json file relative to the current file
    config_path = Path(__file__).parent.parent / 'config.json'
    with open(config_path, 'r') as f:
        config = json.load(f)
    service_routes.update(config)

# Watch for changes in the configuration file and reload if necessary
def watch_configuration():
    last_mtime = None
    while True:
        try:
            # Check for modification time
            with open('config.json', 'r') as f:
                mtime = time.ctime(os.path.getmtime('config.json'))
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
            # Forward the request to the service and get the response
            service_response = requests.request(
                method=request.method,
                url=service_url,
                headers=request.headers,
                params=request.args,
                data=request.form
            )
            # Return the response received from the service
            return jsonify(service_response.json()), service_response.status_code
        else:
            return jsonify({'error': 'Method not allowed'}), 405
    else:
        return jsonify({'error': 'Service not found'}), 404


if __name__ == '__main__':
    load_configuration()  # Initial configuration load
    app.run(debug=True, port=8000)
