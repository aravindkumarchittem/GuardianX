from flask import Flask, jsonify
from flask_cors import CORS

from routes.analyze import analyze_bp
from routes.get_messages import get_messages_bp
from routes.auth import auth_bp   # ✅ NEW

# ✅ Create app FIRST
app = Flask(__name__)
CORS(app)

# ✅ Register all blueprints
app.register_blueprint(analyze_bp)
app.register_blueprint(get_messages_bp)
app.register_blueprint(auth_bp)   # ✅ NEW

@app.route("/")
def home():
    return jsonify({
        "status": "GuardianX backend running",
        "message": "Backend + MongoDB + Dashboard + Auth ready"
    })

if __name__ == "__main__":
    app.run(debug=True)