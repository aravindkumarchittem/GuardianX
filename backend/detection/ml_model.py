


import joblib
import os
import sys
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.text_cleaner import clean_text

BASE_DIR = os.path.dirname(__file__)

SVM_PATH = os.path.join(BASE_DIR, "svm_model.pkl")
LR_PATH = os.path.join(BASE_DIR, "lr_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "vectorizer.pkl")

# 🔄 Load models once
svm_model = joblib.load(SVM_PATH)
lr_model = joblib.load(LR_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def ml_predict(message):
    try:
        cleaned = clean_text(message)
        vector = vectorizer.transform([cleaned])

        # 🔥 Ensemble probabilities
        svm_probs = svm_model.predict_proba(vector)[0]
        lr_probs = lr_model.predict_proba(vector)[0]

        final_probs = (svm_probs + lr_probs) / 2

        prediction = int(np.argmax(final_probs))
        confidence = float(final_probs[prediction])

        # 🔥 Confidence threshold
        if confidence < 0.50:
            return prediction, 0.0

        return prediction, round(confidence, 3)

    except Exception as e:
        print("ML Error:", e)
        return 0, 0.0


