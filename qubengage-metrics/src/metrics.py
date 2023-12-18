from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from datetime import datetime
import requests
import random
import time
from threading import Thread

app = Flask(__name__)
CORS(app)

# static domains
maxmin = "http://semmaxmin.esha.qpc.hal.davecutting.uk/"  
sorted = "http://semsort.esha.qpc.hal.davecutting.uk/"
totalhours = "http://totalhours-4029852.qpc.hal.davecutting.uk/calculate_total_hours"
engagementscore = "http://engagementscore-40292852.qpc.hal.davecutting.uk/calculate_engagement_score"
checkrisk = "http://failurerisk-40292852.qpc.hal.davecutting.uk/check_risk"
averagehours = "http://averagehours-40292852.qpc.hal.davecutting.uk/calculate_average_hours"

# proxy domains
proxyBaseURL = "http://proxy-40292852.qpc.hal.davecutting.uk"
proxyMaxminURL = proxyBaseURL + "/maxmin"
proxySortedURL = proxyBaseURL + "/sorted"
proxyTotalHoursURL = proxyBaseURL + "/totalhours"
proxyEngagementScoreURL = proxyBaseURL + "/engagementscore"
proxyCheckRiskURL = proxyBaseURL + "/checkrisk"
proxyAverageHoursURL = proxyBaseURL + "/averagehours"
endpoints = [proxyMaxminURL, proxySortedURL, proxyTotalHoursURL, proxyEngagementScoreURL, proxyCheckRiskURL, proxyAverageHoursURL,
             maxmin, sorted, totalhours, engagementscore, checkrisk, averagehours]

# A global dictionary to hold the status of the endpoints
endpoints_status = {endpoint: {'status': 'Unknown', 'code': None, 'message': '', 'time_checked': 'current_time'} for endpoint in endpoints}

def generate_param(max_value):
    return random.randint(0, max_value)

def monitor_service():
    while True:
        for endpoint in endpoints:
            try:
                status = ''
                error_message=''
                # Construct the parameters based on the endpoint
                if endpoint in [proxyMaxminURL, proxySortedURL, maxmin, sorted]:
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
                elif endpoint in [proxyTotalHoursURL, proxyEngagementScoreURL, totalhours, engagementscore]:
                    params = {
                        "lab": generate_param(22),
                        "lecture": generate_param(33),
                        "support": generate_param(44),
                        "canvas": generate_param(55)
                    }
                elif endpoint in [proxyCheckRiskURL, checkrisk]:
                    params = {
                        "engagementScore": generate_param(100),
                        "cutOff": generate_param(100)
                    }
                elif endpoint in [proxyAverageHoursURL, averagehours]:
                    params = {"total_hours": generate_param(154)}

                # Send request and time it
                start_time = time.time()
                response = requests.get(endpoint, params=params)
                end_time = time.time()
                response_time = end_time - start_time
                current_time = datetime.now().strftime("%H:%M:%S %d-%m-%Y")

                status_code = response.status_code
                if status_code != 200:
                    status = 'Down'
                    error_message = f"Endpoint returned a non-200 status code: {status_code}"
                else:
                    status = 'Up'

            except requests.exceptions.RequestException as e:
                status = 'Down'
                error_message = str(e)

            # Update the status of the endpoint
            endpoints_status[endpoint] = {
                'status': status,
                'code': status_code,
                'response_time': response_time,
                'message': error_message,
                'time_checked': current_time
            }

            # Log only if there is an error, otherwise log regular status
            if status == 'Down':
                print(f"\nError at Endpoint: {endpoint}, \nStatus: {status}, Status Code: {status_code}, Time Taken: {response_time:.2f} seconds, \nTime: {current_time}.\n")
            else:
                print(f"\nEndpoint: {endpoint}, \nStatus: {status}, Status Code: {status_code}, Time Taken: {response_time:.2f} seconds, \nTime: {current_time}.\n")

        # Sleep for some time before the next check
        time.sleep(5)

@app.route('/metrics', methods=['GET'])
@cross_origin()
def get_metrics():
    # This endpoint returns the current status of all services
    return jsonify(endpoints_status)

if __name__ == '__main__':
    monitor_thread = Thread(target=monitor_service)
    monitor_thread.daemon = True
    monitor_thread.start()
    app.run(debug=True, host='0.0.0.0', port=7000)
