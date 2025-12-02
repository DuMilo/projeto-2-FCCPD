from flask import Flask, jsonify

app = Flask(__name__)

users_db = [
    {"id": 1, "name": "Milo Castro", "email": "milocastro@email.com"},
    {"id": 2, "name": "Giullia Lima", "email": "giullialima@email.com"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users_db)

@app.route('/health', methods=['GET'])
def health():
    return "Users Service OK", 200

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5001)