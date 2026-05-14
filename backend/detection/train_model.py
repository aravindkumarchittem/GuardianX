


import pandas as pd
import joblib
import sys
import os
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.calibration import CalibratedClassifierCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.text_cleaner import clean_text

# 📂 Load dataset
data = pd.read_csv("../../dataset/social_engineering_messages.csv")

# 🧹 Clean text
data["message"] = data["message"].astype(str).apply(clean_text)

X = data["message"]
y = data["label"]

# ✂️ Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 🧠 TF-IDF
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    max_features=6000,
    min_df=2,
    max_df=0.9,
    sublinear_tf=True
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 🤖 MODEL 1: SVM (calibrated)
svm = LinearSVC(class_weight="balanced")
svm_model = CalibratedClassifierCV(svm)
svm_model.fit(X_train_vec, y_train)

# 🤖 MODEL 2: Logistic Regression
lr_model = LogisticRegression(max_iter=1000, class_weight="balanced")
lr_model.fit(X_train_vec, y_train)

# 🔥 ENSEMBLE FUNCTION
def ensemble_predict(X):
    svm_probs = svm_model.predict_proba(X)
    lr_probs = lr_model.predict_proba(X)
    return (svm_probs + lr_probs) / 2

# 📊 Evaluation
probs = ensemble_predict(X_test_vec)
y_pred = np.argmax(probs, axis=1)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# 💾 Save everything
joblib.dump(svm_model, "svm_model.pkl")
joblib.dump(lr_model, "lr_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\n✅ Ensemble model trained & saved successfully!")

