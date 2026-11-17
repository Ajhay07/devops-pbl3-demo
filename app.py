from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "v1")

COLORS = {
    "blue": "#1e3a8a",
    "green": "#166534",
}
BG_COLOR = COLORS.get(APP_VERSION, "#333333")

@app.route("/")
def home():
    hostname = socket.gethostname()
    html = f"""
    <html>
      <head><title>PBL-3 Demo - {APP_VERSION.upper()}</title></head>
      <body style="background-color:{BG_COLOR}; color:white;
                   font-family:sans-serif; text-align:center; padding-top:15%;">
        <h1 style="font-size:3em;">Hello from the DevOps PBL-3 demo app!</h1>
        <h2>Version: {APP_VERSION.upper()}</h2>
        <p>Served by: {hostname}</p>
      </body>
    </html>
    """
    return html

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
