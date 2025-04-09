from flask import Flask, request, render_template_string
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

HTML = """
<!doctype html>
<title>音声文字起こしアプリ</title>
<h1>音声ファイルをアップロードしてください</h1>
<form method=post enctype=multipart/form-data>
  <input type=file name=audio_file>
  <input type=submit value=アップロード>
</form>
{% if result %}
<h2>文字起こし結果：</h2>
<pre>{{ result }}</pre>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        file = request.files["audio_file"]
        if file:
            transcript = openai.Audio.transcribe("whisper-1", file)
            result = transcript["text"]
    return render_template_string(HTML, result=result)

# ✅ Render用に必須のブロック
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Renderが指定するポートを使用
    app.run(host="0.0.0.0", port=port, debug=False)  # 外部アクセス可
