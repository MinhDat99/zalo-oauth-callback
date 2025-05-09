from flask import Flask, request

app = Flask(__name__)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    return f"<h1>Received code: {code}</h1><p>Copy mã code này để lấy access_token</p>", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
