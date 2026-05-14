# from flask import Blueprint, jsonify
# from database.db import messages_collection

# get_messages_bp = Blueprint("get_messages", __name__)

# @get_messages_bp.route("/get-flagged", methods=["GET"])
# def get_flagged():
#     data = list(messages_collection.find({}, {"_id": 0}))
#     return jsonify(data)


from flask import Blueprint, jsonify
from database.db import messages_collection

# ✅ DEFINE BLUEPRINT (THIS IS MISSING)
get_messages_bp = Blueprint("get_messages", __name__)

@get_messages_bp.route("/get-flagged", methods=["GET"])
def get_flagged():
    try:
        data = list(messages_collection.find({}, {"_id": 0}))
        return jsonify(data)
    except Exception as e:
        print("MongoDB Fetch Error:", e)
        return jsonify([])  # prevent crash