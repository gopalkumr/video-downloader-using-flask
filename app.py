from pytube import YouTube
from flask import Flask, request, send_file, jsonify
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def index():
    return '''
        <h1>Welcome to the YouTube Video Downloader</h1>
        <p>Use the /download endpoint to download videos.</p>
    '''

@app.route("/download", methods=["POST"])
def download():
    data = request.get_json()
    if 'url' not in data:
        return jsonify({"error": "URL is required"}), 400

    video_url = data['url']
    
    try:
        buffer = BytesIO()
        url = YouTube(video_url)
        video = url.streams.get_by_itag(18)
        video.stream_to_buffer(buffer)
        buffer.seek(0)

        return send_file(
            buffer,
            as_attachment=True,
            attachment_filename="downloaded-video.mp4",
            mimetype="video/mp4",
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
