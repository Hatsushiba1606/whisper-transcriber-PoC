from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Flask app is running on Render!"

# 必ずこのブロックが必要です👇
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Renderが提供するポート番号を使う
    app.run(host='0.0.0.0', port=port, debug=False)  # 外部アクセス可能にする
