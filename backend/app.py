from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import random
import time

from behavior_store import ip_attempts, user_attempts
from reset_store import reset_otp
from otp_store import otp_data, logs, failed_attempts, blocked_users

app = Flask(__name__)
CORS(app)

# Dummy user
users = {
    "admin": "vicky",
    "user1": "1234",
    "test": "pass"
}
# Settings
MAX_ATTEMPTS = 3
BLOCK_TIME = 60  # seconds

# 🧠 AI detection
def detect_threat(username, ip):
    score = 0
    current_time = time.localtime().tm_hour

    # 🚨 1. Multiple attempts from same IP
    ip_attempts[ip] = ip_attempts.get(ip, 0) + 1
    if ip_attempts[ip] > 5:
        score += 1

    # 🚨 2. Multiple attempts by user
    user_attempts[username] = user_attempts.get(username, 0) + 1
    if user_attempts[username] > 3:
        score += 1

    # 🚨 3. Unusual login time
    if current_time < 6 or current_time > 23:
        score += 1

    return 0 if score >= 2 else 1


# 🤖 ML API
def check_threat(data):
    try:
        res = requests.post("http://127.0.0.1:5000/predict", json=data)
        return res.json()
    except:
        return {"prediction": 1}


# 📊 Logs
def add_log(user, status):
    logs.append({
        "user": user,
        "status": status
    })


@app.route("/")
def home():
    return "🚀 Server Running"


# 🔐 LOGIN (ONLY ONE — FIXED)
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    current_time = time.time()

    # 🚨 Check block
    if username in blocked_users:
        if current_time < blocked_users[username]:
            return jsonify({
                "status": "blocked",
                "message": "🚨 Too many attempts! Try later"
            })
        else:
            del blocked_users[username]
            failed_attempts[username] = 0

    # ❌ Wrong login
    if username not in users or users[username] != password:
        failed_attempts[username] = failed_attempts.get(username, 0) + 1
        add_log(username, "wrong_password")

        if failed_attempts[username] >= MAX_ATTEMPTS:
            blocked_users[username] = current_time + BLOCK_TIME
            add_log(username, "blocked")

            return jsonify({
                "status": "blocked",
                "message": "🚨 Account blocked for 1 minute"
            })

        return jsonify({
            "status": "fail",
            "message": f"❌ Wrong password ({failed_attempts[username]})"
        })

    # ✅ Reset attempts
    failed_attempts[username] = 0

    # 🔥 🧠 AI DETECTION (ADDED HERE)
    ip = request.remote_addr
    ai_result = detect_threat(username, ip)

    if ai_result == 0:
        add_log(username, "ai_blocked")
        return jsonify({
            "status": "blocked",
            "message": "🚨 AI detected suspicious behavior"
        })

    # 🤖 ML check
    ml_data = {
        "duration": 0,
        "src_bytes": 200,
        "dst_bytes": 300
    }

    result = check_threat(ml_data)

    if result.get("prediction") == 0:
        add_log(username, "attack_detected")
        return jsonify({
            "status": "blocked",
            "message": "🚨 Attack detected"
        })

    # 🔐 OTP
    otp = random.randint(1000, 9999)
    otp_data[username] = otp

    print(f"OTP for {username}: {otp}")
    add_log(username, "otp_sent")

    return jsonify({
        "status": "otp_required",
        "message": "OTP sent"
    })


# 🔐 VERIFY OTP
@app.route("/verify-otp", methods=["POST"])
def verify_otp():
    data = request.get_json()
    username = data.get("username")
    user_otp = int(data.get("otp"))

    if otp_data.get(username) == user_otp:
        add_log(username, "login_success")
        return jsonify({
            "status": "success",
            "message": "✅ Login success"
        })
    else:
        add_log(username, "wrong_otp")
        return jsonify({
            "status": "wrong",
            "message": "❌ Wrong OTP"
        })


# 📊 LOGS
@app.route("/logs", methods=["GET"])
def get_logs():
    return jsonify(logs)


# 🔐 FORGOT PASSWORD
@app.route("/forgot-password", methods=["POST"])
def forgot_password():
    data = request.get_json()
    username = data.get("username")

    if username not in users:
        return {"status": "fail", "message": "User not found"}

    otp = random.randint(1000, 9999)
    reset_otp[username] = otp

    print("RESET OTP:", otp)

    return {"status": "otp_sent", "message": "OTP sent"}


# 🔐 RESET PASSWORD
@app.route("/reset-password", methods=["POST"])
def reset_password():
    data = request.get_json()

    username = data.get("username")
    otp = int(data.get("otp"))
    new_password = data.get("new_password")

    if reset_otp.get(username) == otp:
        users[username] = new_password
        return {"status": "success", "message": "Password updated"}
    else:
        return {"status": "fail", "message": "Wrong OTP"}


if __name__ == "__main__":
    app.run(port=8000, debug=True)