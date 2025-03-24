import os
import requests
from flask import Flask, request, redirect, jsonify
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

FB_CLIENT_ID = os.getenv("FB_CLIENT_ID")
FB_CLIENT_SECRET = os.getenv("FB_CLIENT_SECRET")
REDIRECT_URI = os.getenv("BACKEND_URL") + "/callback"

user_tokens = {}

@app.route("/login")
def login():
    auth_url = (
        f"https://www.facebook.com/v18.0/dialog/oauth?"
        f"client_id={FB_CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=email,public_profile,user_posts"
    )
    return redirect(auth_url)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return "Authorization failed", 400

    token_url = (
        f"https://graph.facebook.com/v18.0/oauth/access_token?"
        f"client_id={FB_CLIENT_ID}&redirect_uri={REDIRECT_URI}&client_secret={FB_CLIENT_SECRET}&code={code}"
    )

    response = requests.get(token_url)
    data = response.json()

    if "access_token" not in data:
        return jsonify({"error": "Failed to get access token"}), 400

    access_token = data["access_token"]
    user_tokens["user"] = access_token

    return jsonify({"message": "Logged in successfully!", "access_token": access_token})

@app.route("/fetch-data", methods=["GET"])
def fetch_data():
    token = user_tokens.get("user")
    if not token:
        return jsonify({"error": "User not authenticated"}), 401

    url = f"https://graph.facebook.com/v18.0/me?fields=id,name,email&access_token={token}"
    response = requests.get(url)
    return jsonify(response.json())

@app.route("/delete-data", methods=["DELETE"])
def delete_data():
    token = user_tokens.get("user")
    if not token:
        return jsonify({"error": "User not authenticated"}), 401

    delete_url = f"https://graph.facebook.com/v18.0/me/permissions?access_token={token}"
    response = requests.delete(delete_url)

    if response.status_code == 200:
        return jsonify({"message": "User data deleted successfully!"})
    return jsonify({"error": "Failed to delete data", "details": response.json()}), 400

if __name__ == "__main__":
    app.run(debug=True)
