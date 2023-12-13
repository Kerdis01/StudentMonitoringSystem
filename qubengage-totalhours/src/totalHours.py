from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def calculate_total_hours(attendances):
    attendances = [int(value) for value in attendances]
    total_hours = sum(attendances)
    return total_hours

@app.route('/calculate_total_hours', methods=['GET'])
def calculate_total_hours_route():
    lecture = request.args.get('lecture', type=int, default=0)
    lab = request.args.get('lab', type=int, default=0)
    support = request.args.get('support', type=int, default=0)
    canvas = request.args.get('canvas', type=int, default=0)

    attendances = [lecture, lab, support, canvas]
    total_hours = calculate_total_hours(attendances)

    return jsonify({"total_hours": total_hours}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
