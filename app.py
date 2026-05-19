from flask import Flask, request

app = Flask(__name__)

# ===== LINE WEBHOOK =====
@app.route("/callback", methods=["POST"])
def callback():
    body = request.json

    print("\n=== FULL EVENT ===")
    print(body)

    if "events" in body:
        for e in body["events"]:
            print("\n--- EVENT ---")
            print("type:", e.get("type"))

            source = e.get("source", {})
            print("source:", source)

            group_id = source.get("groupId")
            user_id = source.get("userId")

            print("groupId:", group_id)
            print("userId:", user_id)

    return "OK"

# ===== HOME TEST =====
@app.route("/", methods=["GET"])
def home():
    return "LINE BOT IS RUNNING"

# ===== IMPORTANT: FOR RENDER / CLOUD =====
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)