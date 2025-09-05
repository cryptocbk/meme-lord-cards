from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "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"  # вставь сюда ключ
MODEL = "deepseek/deepseek-r1"

@app.route("/")
def home():
    return {"status": "ok", "msg": "DeepSeek API Proxy работает!"}

@app.route("/deepseek", methods=["POST"])
def deepseek():
    user_prompt = request.json.get("prompt", "")
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": user_prompt}],
    }
    r = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
