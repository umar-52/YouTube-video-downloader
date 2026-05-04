from flask import Flask, render_template_string, request, send_file
import yt_dlp
import os

app = Flask(__name__)

# सुंदर डिजाइन (HTML/CSS)
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Umar Bhai Video Downloader</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0f0c29; background: linear-gradient(to right, #24243e, #302b63, #0f0c29); color: white; text-align: center; padding-top: 50px; }
        .container { background: rgba(255, 255, 255, 0.1); padding: 30px; border-radius: 15px; display: inline-block; box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37); backdrop-filter: blur(4px); border: 1px solid rgba(255, 255, 255, 0.18); }
        input { padding: 12px; width: 300px; border-radius: 5px; border: none; margin-bottom: 10px; }
        button { padding: 12px 25px; background: #e91e63; color: white; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; }
        button:hover { background: #ad1457; }
    </style>
</head>
<body>
    <div class="container">
        <h1>YouTube Downloader</h1>
        <p>URL पेस्ट करें और डाउनलोड करें</p>
        <form method="POST" action="/download">
            <input type="text" name="url" placeholder="https://youtube.com/..." required><br>
            <button type="submit">वीडियो डाउनलोड करें</button>
        </form>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'video.mp4',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return send_file('video.mp4', as_attachment=True)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
