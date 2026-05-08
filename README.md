# 🛡️ Cybersecurity AI Threat Detection System

An AI-powered Cybersecurity Threat Detection System using Machine Learning and Flask to detect cyber attacks, suspicious login behavior, and brute-force attempts in real time.

---

# 🚀 Features

- 🔐 Secure Login System
- 📧 OTP Verification
- 🚨 Brute Force Detection
- 🤖 AI Behavior Analysis
- 🧠 Machine Learning Attack Detection
- 📊 Admin Dashboard
- 🌍 IP & Activity Tracking
- ⚡ Automatic Response System
- 📁 Security Logs & Alerts

---

# 🧠 Attack Types Detected

- DoS (Denial of Service)
- Probe Attacks
- R2L (Remote to Local)
- U2R (User to Root)
- Normal Traffic

---

# 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML/CSS
- Jupyter Notebook

---

# 📂 Project Structure

# 📂 Project Structure

```bash
V_______K/
│
├── backend/                      # 🔐 Flask backend
│   ├── app.py
│   │
│   ├── ai/                      # 🤖 AI logic
│   │   ├── ml_api.py
│   │   ├── detector.py
│   │   ├── action_handler.py
│   │   └── __init__.py
│   │
│   ├── store/                   # 📦 Storage
│   │   ├── otp_store.py
│   │   ├── alert_store.py
│   │   ├── behavior_store.py
│   │   ├── reset_store.py
│   │   └── __init__.py
│   │
│   ├── utils/
│   │   └── __init__.py
│   │
│   └── requirements.txt
│
├── ml/                          # 🧠 Machine Learning
│   ├── models/
│   │   └── threat_detector_rf.pkl
│   │
│   ├── src/
│   │   ├── train.py
│   │   ├── preprocess.py
│   │   ├── predict.py
│   │   └── deploy.py
│   │
│   ├── data/
│   ├── notebooks/
│   └── requirements.txt
│
├── frontend/                    # 🌐 Frontend
│   ├── index.html
│   ├── dashboard.html
│   ├── otp.html
│   ├── reset.html
│   └── style.css
│
├── .env
├── README.md
└── requirements.txt
```

⚙️ Machine Learning Model
Algorithm: Random Forest
Dataset: NSL-KDD
Features: 41 Network Features
Output: Attack Prediction

Example Output:

{
  "prediction": "dos",
  "confidence": 0.92
}

🔐 Security Features
Basic Security
Password Hashing
OTP Verification
Forgot Password System
Brute Force Protection
3 Attempts → Warning
5 Attempts → Alert
10 Attempts → Block
AI Behavior Detection
IP Change Detection
Device Change Detection
Suspicious Login Time Detection

⚡ Automatic Response System
Attack Type	Action
DoS	Block
U2R	Block
R2L	OTP Verification
Probe	Warning
Normal	Allow

📊 Dashboard Features
Attack Monitoring
Login Activity
Alert Management
IP Tracking
User Logs

▶️ Installation
Clone Repository
git clone https://github.com/Anu-km/cybersecurity-ai-threat-detection.git
Install Requirements
pip install -r requirements.txt
Run Backend
cd backend
python app.py

📈 Future Improvements
Deep Learning Integration
Real-Time Monitoring
Cloud Deployment
SIEM Integration

👨‍💻 Author
Vicky Kumar
B.Tech CSE Student
Cybersecurity & AI Enthusiast
