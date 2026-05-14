from flask import Blueprint, request, jsonify

from detection.rule_engine import rule_based_analysis
from detection.risk_score import decide_risk_level
from detection.ml_model import ml_predict

# ✅ NEW: import MongoDB
from database.db import messages_collection

analyze_bp = Blueprint("analyze", __name__)

@analyze_bp.route("/analyze-message", methods=["POST"])
def analyze_message():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Message text is required"}), 400

    message_text = data["message"]

    # Rule-based analysis
    rule_score, rule_reasons = rule_based_analysis(message_text)

    # ML-based analysis
    ml_label, ml_confidence = ml_predict(message_text)

    # Combine logic
    final_score = rule_score
    reasons = rule_reasons.copy()

    if ml_label == 1 and ml_confidence > 0:
        final_score += 3
        reasons.append("ML model detected harmful intent")

    risk_level = decide_risk_level(final_score)

    # ✅ NEW: Save to MongoDB (only risky messages)
    if risk_level in ["suspicious", "danger"]:
        try:
            messages_collection.insert_one({
                "message": message_text,
                "risk_level": risk_level,
                "score": final_score,
                "reasons": list(set(reasons)),
                "ml_confidence": round(float(ml_confidence), 2)
            })
        except Exception as e:
            print("MongoDB Error:", e)

    return jsonify({
        "message": message_text,
        "risk_level": risk_level,
        "final_score": final_score,
        "reasons": list(set(reasons)),
        "ml_confidence": round(float(ml_confidence), 2)
    }), 200





# from flask import Blueprint, request, jsonify

# from detection.rule_engine import rule_based_analysis
# from detection.risk_score import decide_risk_level
# from detection.ml_model import ml_predict

# analyze_bp = Blueprint("analyze", __name__)

# @analyze_bp.route("/analyze-message", methods=["POST"])
# def analyze_message():
#     data = request.get_json()

#     if not data or "message" not in data:
#         return jsonify({"error": "Message text is required"}), 400

#     message_text = data["message"]

#     # Rule-based analysis
#     rule_score, rule_reasons = rule_based_analysis(message_text)

#     # ML-based analysis
#     ml_label, ml_confidence = ml_predict(message_text)

#     # Combine logic
#     final_score = rule_score
#     reasons = rule_reasons.copy()

#     if ml_label == 1 and ml_confidence > 0:
#         final_score += 3
#         reasons.append("ML model detected harmful intent")

#     risk_level = decide_risk_level(final_score)

#     return jsonify({
#         "message": message_text,
#         "risk_level": risk_level,
#         "final_score": final_score,
#         "reasons": list(set(reasons)),
#         "ml_confidence": round(float(ml_confidence), 2)
#     }), 200
