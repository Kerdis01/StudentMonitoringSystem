from flask import Flask, request, jsonify, make_response
from flask_bcrypt import Bcrypt #this does work, vscode just says it doesn't /shrug
from flask_cors import CORS
import uuid

# Initialize Flask App
app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)

# Predefined hardcoded admin credentials (password should be hashed using bcrypt)
admin_username = 'admin'
admin_password_hash = bcrypt.generate_password_hash('adminpassword').decode('utf-8')  # Replace 'adminpassword' with a strong password of your choice.

# Simple in-memory 'database' with a hardcoded admin user
users_db = {
    admin_username: {'password': admin_password_hash, 'id': str(uuid.uuid4())}
}

@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users_db.get(username)
    if user and bcrypt.check_password_hash(user['password'], password):
        # Authentication successful
        return make_response(jsonify({'message': 'Authentication successful', 'user_id': user['id']}), 200)
    else:
        # Authentication failed
        return make_response(jsonify({'message': 'Invalid username or password'}), 401)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7001)
