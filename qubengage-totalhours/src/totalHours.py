from flask import Flask, jsonify, request
from flask_cors import CORS  # Import the CORS module

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def calculate_total_hours(items, attendances):
    total_hours = sum(attendances)
    return total_hours

@app.route('/calculate_total_hours', methods=['POST'])
def calculate_total_hours_route():
    data = request.json  # Assuming the data is sent as JSON
    items = data.get("items", [])
    attendances = data.get("attendances", [])

    if len(items) != len(attendances):
        return jsonify({"error": "Mismatched number of items and attendances"}), 400

    total_hours = calculate_total_hours(items, attendances)

    return jsonify({"total_hours": total_hours})

if __name__ == '__main__':
    app.run(debug=True)
