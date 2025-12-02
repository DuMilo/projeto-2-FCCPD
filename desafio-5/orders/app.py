from flask import Flask, jsonify

app = Flask(__name__)

orders_db = [
    {"id": 101, "item": "Celular Samsung", "price": 2000, "user_id": 1},
    {"id": 102, "item": "Computador Roubado", "price": 500, "user_id": 2}
]

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders_db)

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5002)