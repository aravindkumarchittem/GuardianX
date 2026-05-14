# GuardianX
# 🛡️ GuardianX  
**AI-Powered Cyberbullying & Social Engineering Detection System**

---

## 📌 Overview
GuardianX is a real-time cybersecurity system designed to detect **cyberbullying, phishing, and social engineering attacks** in chat platforms such as WhatsApp Web.

The system uses a **hybrid detection approach** combining:
- Rule-based analysis (explainable logic)
- Machine learning (text classification)
- Real-time browser monitoring

---

## 🚀 Features

- 🔍 Real-time message monitoring using Chrome Extension  
- 🧠 Hybrid detection system:
  - Rule-based engine (patterns like urgency, threats, secrecy)
  - Machine learning model (TF-IDF + Ensemble)  
- ⚠️ Risk classification:
  - Safe  
  - Suspicious  
  - Danger  
- 🎨 Live UI highlighting in chat interface  
- 📊 Dashboard for flagged messages  
- 🗄️ MongoDB storage for analysis  

---

## 🏗️ System Architecture
WhatsApp Web
↓
Chrome Extension (content.js)
↓
Flask Backend API
↓
Detection Engine (Rule + ML)
↓
MongoDB Database
↓
Dashboard UI




---

## 🧠 Machine Learning Model

- TF-IDF Vectorization (n-grams: 1–2)
- Models used:
  - Linear SVM (Calibrated)
  - Logistic Regression
- Ensemble approach:



Final Probability = (SVM + LR) / 2



- Confidence threshold applied to reduce false positives

---

## ⚙️ Tech Stack

- **Backend:** Flask (Python)  
- **Machine Learning:** Scikit-learn, Pandas, NumPy  
- **Database:** MongoDB Atlas  
- **Frontend:** HTML, CSS, JavaScript  
- **Extension:** Chrome Manifest V3  

---

## 📁 Project Structure



guardianx/
│── backend/
│ ├── detection/
│ ├── routes/
│ ├── database/
│ ├── utils/
│ ├── app.py
│
│── extension/
│── dashboard/
│── dataset/
│── docs/
│── README.md



---

## ⚡ Setup Instructions

### 1️⃣ Clone Repository
git clone https://github.com/your-username/GuardianX.git
cd GuardianX/backend



---

### 2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate


---

### 3️⃣ Install Dependencies
pip install flask flask-cors pymongo pandas scikit-learn joblib numpy python-dotenv


---

### 4️⃣ Train Model
cd detection
python train_model.py
---

### 5️⃣ Configure MongoDB

Create a `.env` file in backend folder:
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/guardianx_db


⚠️ Make sure:
- IP whitelist includes `0.0.0.0/0`
- Password has no special characters or is URL-encoded

---

### 6️⃣ Run Backend Server

python app.py

---

### 7️⃣ Load Chrome Extension

1. Open Chrome → `chrome://extensions/`  
2. Enable **Developer Mode**  
3. Click **Load Unpacked**  
4. Select `extension/` folder  

---

### 8️⃣ Test the System

- Open WhatsApp Web  
- Send messages like:
  - “send me your otp”
  - “don’t tell anyone”
  - “i will hurt you”

✅ You will see:
- 🔴 Danger (Red)
- 🟠 Suspicious (Orange)

---

## 📊 Output

- Real-time detection in chat UI  
- Highlighted messages  
- Stored flagged messages in database  
- Dashboard visualization  

---

## 📈 Performance

- Accuracy: ~90%  
- Balanced precision and recall  
- Improved stability using ensemble model  

---

## 🔮 Future Improvements

- Deep learning models (BERT, LSTM)  
- Multilingual detection  
- Voice & image-based threat detection  
- Behavioral analysis and user profiling  

---

## 👨‍💻 Author

**Aravind Kumar CH**

---

## 📜 License
This project is developed for academic and research purposes.

---

## ⭐ Summary

GuardianX demonstrates how combining:
- Rule-based intelligence  
- Machine learning  
- Real-time systems  

can create an **effective, explainable, and deployable cybersecurity solution**.


