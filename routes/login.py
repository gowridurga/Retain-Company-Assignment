import sqlite3
from flask import Blueprint, request, jsonify
from models.db import get_db_connection
from werkzeug.security import check_password_hash
from utils.jwt_helper import generate_token

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    print("🚨 LOGIN ROUTE TRIGGERED")

    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    print("📩 Received:", email, password)

    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    conn = get_db_connection()
    conn.row_factory = sqlite3.Row  # ✅ Ensure dict-style access
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()

    if user:
        user_dict = dict(user)
        print("👤 DB User:", user_dict)
        print("🔐 Stored Hash:", user_dict['password'])
        print("🔑 Comparing with:", password)

        if check_password_hash(user_dict['password'], password):
            print("✅ Password Match")
            token = generate_token(user_dict['id'])
            return jsonify({"status": "success", "token": token}), 200
        else:
            print("❌ Password Mismatch")
            return jsonify({"status": "failed", "message": "Invalid credentials"}), 401
    else:
        print("🚫 User not found")
        return jsonify({"status": "failed", "message": "Invalid credentials"}), 401
