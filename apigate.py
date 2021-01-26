from flask import Flask, request, jsonify
from PIL import Image
from stegano import lsb
import os


app = Flask(__name__)

@app.route("/steg", methods=["POST"])
def process_image():
    file = request.files['image']
    try:
        img = Image.open(file.stream)
        msg ="sucess"
        mmsg = lsb.reveal(img)
    except:
        msg = "error"
        mmsg = "Something went wrong. Maybe you are not sending a picture"

    return jsonify({'status': msg, 'message': mmsg})

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
