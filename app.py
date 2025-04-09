from flask import Flask, request, jsonify
import openai
import os

# Flaskアプリを作成
app = Flask(__name__)

# .envに書かれたAPIキーを環境変数から読み込む
openai.api_key = os.getenv("OPENAI_API_KEY")

# エンドポイント（APIの入り口）を作成
@app.route("/transcribe", methods=["POST"])
def transcribe():
    try:
        audio_file = request.files["file"]  # "file" という名前のファイルを受け取る
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return jsonify({"text": transcript["text"]})  # 結果を返す
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 開発用サーバー起動（Render用には後で書き換えます）
if __name__ == "__main__":
    app.run(debug=True)
