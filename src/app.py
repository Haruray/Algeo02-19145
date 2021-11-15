from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
from image_compress import *
 
app = Flask(__name__)
 
UPLOADS = 'static/uploads/'
COMPRESSED = 'static/compressed/' 
app.secret_key = "secret key"
app.config['COMPRESSED'] = COMPRESSED
app.config['UPLOADS'] = UPLOADS
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('Upload gambar gagal')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('Tidak ada gambar untuk diupload.')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOADS'], filename))
        percentage = int(request.form['compressRate'])
        runtime = img_compress(filename, percentage)
        beforename = f'{UPLOADS}{filename}'
        save = modify_file_name(filename)
        savename = f'{COMPRESSED}{save}'
        before = os.path.getsize(beforename)
        after = os.path.getsize(savename)
        pxldiff = str(round((after/before)*100))
        flash('Gambar berhasil diupload! berikut hasilnya')
        return render_template('index.html', filename=filename, runtime=runtime, pxldiff=pxldiff)
    else:
        flash('Allowed image types are - jpg, jpeg')
        return redirect(request.url)
 
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/display/compressed/<filename>')
def display_image_compressed(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='compressed/' + modify_file_name(filename)), code=301)
 
if __name__ == "__main__":
    app.run()