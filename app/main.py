from flask import Flask, jsonify

app = Flask(__name__)

videos = [
    {"id": 1, "title": "Película de Acción", "duration": 90},
    {"id": 2, "title": "Documental sobre Naturaleza", "duration": 60},
    {"id": 3, "title": "Serie de Comedia - Episodio 1", "duration": 30}
]

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})

@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'Bienvenido a la API de VODs!'})

@app.route('/videos', methods=['GET'])
def list_videos():
    return jsonify(videos)

@app.route('/videos/<int:video_id>', methods=['GET'])
def get_video(video_id):
    video = next((v for v in videos if v['id'] == video_id), None)  # Busca el video en la lista
    if video:
        return jsonify(video)
    else:
        return jsonify({'message': 'Video no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
