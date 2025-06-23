#!/user/bin/python3
"""Module 4:Develop a Simple API using Python with Flask"""
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    """Define a route for the root URL (“/”)"""
    return ("Welcome to the Flask API!")

@app.route("/data")
def get_data():
    """display data"""
    return jsonify(list(users.keys()))

@app.route("/status")
def get_status():
    return ("OK"), 200

@app.route("/users/<username>")
def get_user(username):
    """display username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """Add new user"""
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == "__main__": 
    app.run(debug=True)
