from flask import Flask, request

app = Flask(__name__)

@app.route("/callback", methods=["POST"])
def callback():
    body = request.get_json()

    print("\n=== FULL EVENT ===")
    print(body)

    if body and "events" in body:
        for e in body["events"]:
            print("\n--- EVENT ---")
            print("type:", e.get("type"))

            source = e.get("source", {})
            print("groupId:", source.get("groupId"))

    return "OK", 200


@app.route("/", methods=["GET"])
def home():
    return "LINE BOT IS RUNNING", 200


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
