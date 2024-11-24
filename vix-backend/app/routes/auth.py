from flask import Blueprint, request, jsonify
from services.database import get_database

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route("/api/register", methods=["POST"])
def register():
    data = request.json
    db = get_database()
    user = {"username": data["username"], "password": data["password"]}
    db.users.insert_one(user)
    return jsonify({"message": "User registered successfully!"})

@auth_blueprint.route("/api/login", methods=["POST"])
def login():
    data = request.json
    db = get_database()
    user = db.users.find_one({"username": data["username"], "password": data["password"]})
    if user:
        return jsonify({"message": "Login successful!"})
    return jsonify({"message": "Invalid credentials"}), 401
