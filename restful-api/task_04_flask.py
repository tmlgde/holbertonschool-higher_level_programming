from flask import Flask
from flask import jsonify
from flash import request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    users = {
            "Toto": {
                "name": "Toto",
                "age": 15,
                "city": "Paris"
                }
            }
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    data = {"status": "ok"}
    return jsonify(data)

@app.route('/add_user', methods=["POST"])
def add_user():

if __name__ == "__main__":
    app.run()
