from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
users ={}

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
    data = request.get_json()
    users[data["username"]] = {
            "name": data["name"],
            "age": data["age"],
            "city": data["city"]
            }
    return jsonify(data)

if __name__ == "__main__":
    app.run()
