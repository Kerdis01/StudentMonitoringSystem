from flask import Flask, jsonify, request
from flask_cors import CORS  # Import the CORS module

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def calculate_total_hours(attendances):
    total_hours = sum(attendances)
    return total_hours

@app.route('/calculate_total_hours', methods=['POST'])
def calculate_total_hours_route():
    data = request.json  # Assuming the data is sent as JSON
    attendances = data.get("attendances", [])
    total_hours = calculate_total_hours(attendances)
    return jsonify({"total_hours": total_hours}), total_hours

if __name__ == '__main__':
    app.run(debug=True)
