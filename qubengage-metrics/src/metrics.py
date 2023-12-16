from flask import Flask, jsonify
from flask_cors import CORS
import requests
import random
import time
from threading import Thread

app = Flask(__name__)
CORS(app)

proxyBaseURL = "http://proxy-40292852.qpc.hal.davecutting.uk"
maxminURL = proxyBaseURL + "/maxmin"
sortedURL = proxyBaseURL + "/sorted"
totalHoursURL = proxyBaseURL + "/totalhours"
engagementScoreURL = proxyBaseURL + "/engagementscore"
checkRiskURL = proxyBaseURL + "/checkrisk"
averageHoursURL = proxyBaseURL + "/averagehours"
endpoints = [maxminURL, sortedURL, totalHoursURL, engagementScoreURL, checkRiskURL, averageHoursURL]

# A global dictionary to hold the status of the endpoints
endpoints_status = {endpoint: {'status': 'Unknown', 'code': None, 'message': ''} for endpoint in endpoints}

def generate_param(max_value):
    return random.randint(0, max_value)

def monitor_service():
    while True:
        for endpoint in endpoints:
            try:
                status = ''
                error_message=''
                # Construct the parameters based on the endpoint
                if endpoint in [maxminURL, sortedURL]:
                    params = {
                        "item_1": "Lecture sessions",
                        "attendance_1": generate_param(22),
                        "item_2": "Lab sessions",
                        "attendance_2": generate_param(33),
                        "item_3": "Support sessions",
                        "attendance_3": generate_param(44),
                        "item_4": "Canvas activities",
                        "attendance_4": generate_param(55)
                    }
                elif endpoint == totalHoursURL or endpoint == engagementScoreURL:
                    params = {
                        "lab": generate_param(22),
                        "lecture": generate_param(33),
                        "support": generate_param(44),
                        "canvas": generate_param(55)
                    }
                elif endpoint == checkRiskURL:
                    params = {
                        "engagementScore": generate_param(100),
                        "cutOff": generate_param(100)
                    }
                elif endpoint == averageHoursURL:
                    params = {"total_hours": generate_param(154)}

                # Send request and time it
                start_time = time.time()
                response = requests.get(endpoint, params=params)
                end_time = time.time()
                response_time = end_time - start_time

                status_code = response.status_code
                if status_code != 200:
                    status = 'Down'
                    error_message = f"Endpoint returned a non-200 status code: {status_code}"

            except requests.exceptions.RequestException as e:
                status = 'Down'
                error_message = str(e)

            # Update the status of the endpoint
            endpoints_status[endpoint] = {
                'status': status,
                'code': status_code,
                'message': error_message
            }

            # Log only if there is an error, otherwise log regular status
            if status == 'Down':
                print(f"\nError at Endpoint: {endpoint}, Status Code: {status_code}, Time Taken: {response_time:.2f}, Error: {error_message}")
            else:
                print(f"\nEndpoint: {endpoint}, Status: {status}, Status Code: {status_code}, Time Taken: {response_time:.2f} seconds")

        # Sleep for some time before the next check
        time.sleep(5)

@app.route('/metrics', methods=['GET'])
def get_metrics():
    # This endpoint returns the current status of all services
    return jsonify(endpoints_status)

if __name__ == '__main__':
    monitor_thread = Thread(target=monitor_service)
    monitor_thread.daemon = True
    monitor_thread.start()
    app.run(debug=True, host='0.0.0.0', port=7000)
