#!/usr/bin/python3
"""API Security and Authentication Techniques"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity
)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "ta_cle_secrete_tres_longue"
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Utilisateurs en mémoire
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Vérifie les identifiants Basic Auth"""
    if username in users and \
            check_password_hash(users[username]["password"], password):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Route protégée par Basic Auth"""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    log = verify_password(username, password)

    if log is None:
        return jsonify({"error": "invalid credentials"}), 401
    else:
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": users[username]["role"]})
        return jsonify(access_token=access_token)


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Route protégée avec JWT"""
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Route réservée aux admins"""
    current_user = get_jwt_identity()
    user_data = users.get(current_user)

    if not user_data or user_data.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    else:
        return "Admin Access: Granted"

# Gestion des erreurs JWT


@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_fresh_token_required(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
