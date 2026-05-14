from flask import Blueprint, request, jsonify
from database.db import users_collection

auth_bp = Blueprint("auth", __name__)

# ✅ SIGNUP
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    # check if user already exists
    existing_user = users_collection.find_one({"username": username})
    if existing_user:
        return jsonify({"status": "fail", "message": "User already exists"}), 400

    # insert new user
    users_collection.insert_one({
        "username": username,
        "password": password
    })

    return jsonify({"status": "success", "message": "User created"}), 201


# ✅ LOGIN
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    user = users_collection.find_one({
        "username": username,
        "password": password
    })

    if user:
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "fail", "message": "Invalid credentials"}), 401