import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(message="Hello, CI/CD!", version=os.getenv("APP_VERSION", "1.0.0"))


@app.get("/health")
def health():
    return jsonify(status="healthy")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
