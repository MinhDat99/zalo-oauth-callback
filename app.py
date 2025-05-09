from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Zalo Webhook is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("📥 Webhook nhận được:")
    print(data)
    return "ok", 200

