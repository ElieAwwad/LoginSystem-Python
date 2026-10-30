import os
from flask import Flask, request, jsonify
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

load_dotenv() 
app = Flask(__name__)

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


@app.route("/auth", methods=["POST"])
def auth():

    data = request.get_json()

    username = data["username"]
    password = data["password"]
    action = data["action"]

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if action == "register":

        # Check if username already exists
        cursor.execute(
            "SELECT id FROM users WHERE username = %s",
            (username,)
        )

        if cursor.fetchone():
            cursor.close()
            conn.close()

            return jsonify({
                "success": False,
                "message": "Username already exists"
            })

        # Hash password
        hashed_password = generate_password_hash(password)

        # Insert user
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, hashed_password)
        )

        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({
            "success": True,
            "message": "User registered successfully"
        })


    elif action == "login":

        cursor.execute(
            "SELECT * FROM users WHERE username = %s",
            (username,)
        )

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user is None:
            return jsonify({
                "success": False,
                "message": "Invalid username or password"
            })

        if check_password_hash(user["password"], password):
            return jsonify({
                "success": True,
                "message": "Login successful",
                "username": user["username"]
            })

        return jsonify({
            "success": False,
            "message": "Invalid username or password"
        })


if __name__ == "__main__":
    app.run(debug=True)