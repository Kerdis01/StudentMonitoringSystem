from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def calculate_total_hours(attendances):
    attendances = [int(value) for value in attendances]
    total_hours = sum(attendances)
    return total_hours

@app.route('/calculate_total_hours', methods=['POST'])
def calculate_total_hours_route():
    data = request.json
    attendances = data.get("attendances", [])
    total_hours = calculate_total_hours(attendances)
    
    return jsonify({"total_hours": total_hours}), 200

if __name__ == '__main__':
    app.run(debug=True)
