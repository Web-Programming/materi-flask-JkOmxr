from flask import Flask, jsonify, request 
import os # Diperlukan untuk menyimpan file
import time # Diperlukan untuk membuat timestamp


UPLOAD_FOLDER = 'static/uploads'
# Allowed Extention = {'png', 'jpg','jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return 'file Upload Demo'

@app.route('/uploadfile', methods = ['Get', 'POST'])
def uploadfile():
    foto = request.files['foto']
    if foto:
        # Mengambil timestamp saat ini untuk menambahkan ke nama file
        timestamp = str(int(time.time()))
        # Mengambil ekstensi file asli
        ext = foto.filename.split('-')[-1]
        # menambah ekstensi ke nama file unik
        unique_filename = f"{timestamp}.{ext}"
        # Menyimpan file dengan nama unik
        foto_path = os.path.join(app.config['UPLOAD_FOLDER'],
        unique_filename)
        foto.save(foto_path)
        # Menyimpan path relatif dengan menggunakan
        foto_path = f"uploads/{unique_filename}"
        data = {
            "status" : "success",
            "message" : "file Upload",
        }
        return jsonify(data)
    else:
        foto_path = None
        data = {
            "status" : "failed",
            "message" : "file upload failed",
        }
        return jsonify(data)
    
    # json empty
    data = {
        "status" : "sucsses",
        "message" : "Pick a foto uplod",
    }
    return jsonify(data)

# tambahkan depedensi flask-restful
# pip install flask_restful

# temp this as is
if __name__ == '__main__':
    app.run(debug=True, port=4999)