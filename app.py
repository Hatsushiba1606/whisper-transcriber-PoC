import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import openai
from dotenv import load_dotenv

# .envファイルからAPIキーを読み込む
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Flaskアプリケーションの初期化
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp'

@app.route('/', methods=['GET'])
def index():
    return 'Flask app is running on Render!'

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({'error': '音声ファイルが見つかりません'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'ファイル名が空です'}), 400

    try:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        with open(filepath, 'rb') as audio_file:
            transcript = openai.Audio.transcribe("whisper-1", audio_file)

        return jsonify({'transcript': transcript['text']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 🔥 Render対応の起動設定（PORTとhostを必ず指定）
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

