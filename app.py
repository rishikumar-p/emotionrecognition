import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from predictEmotion import getEmotion
from predictDistraction import getDistraction
from predictWorkload import getWorkload

UPLOAD_FOLDER = '/Users/rishi/Documents/MSCS/Fall 23/MC/mood_recognition_server/images'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/emotion', methods=['POST'])
def emotion():
    print(request.files)
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'image not provided'}), 400
        image = request.files['image']
        if image.filename =='':
            return jsonify({'error': 'no image selected'}), 400 
        if image:
            filename = secure_filename(image.filename)
            result = getEmotion()
            return jsonify({'prediction': result}), 200
    except:
        return jsonify({'error': 'something went wrong'}), 500
    

@app.route('/distraction', methods=['POST'])
def distraction():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'image not provided'}), 400
        image = request.files['image']
        if image.filename =='':
            return jsonify({'error': 'no image selected'}), 400
        if image:
            filename = secure_filename(image.filename)
            result = getDistraction()
            return jsonify({'prediction': result}), 200
    except:
        return jsonify({'error': 'something went wrong'}), 500

@app.route('/workload', methods=['POST'])
def workload():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'image not provided'}), 400
        image = request.files['image']
        if image.filename =='':
            return jsonify({'error': 'no image selected'}), 400
        if image:
            filename = secure_filename(image.filename)
            result = getWorkload()
            return jsonify({'prediction': result}), 200
    except:
        return jsonify({'error': 'something went wrong'}), 500

    
if __name__ == '__main__':
    app.run(debug=True)