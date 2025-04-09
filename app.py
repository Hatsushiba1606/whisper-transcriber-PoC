import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, this is your Render-deployed app!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # ← Renderが渡すPORTを取得
    app.run(host="0.0.0.0", port=port, debug=True)  # ← 0.0.0.0でバインド！
