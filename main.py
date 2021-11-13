#FILE UTAMA UNTUK BACKEND
#MASIH DICOMMENT UNTUK KEPENTINGAN TESTING
"""from flask import Flask, render_template, flash, redirect, request,session

app = Flask(__name__)

@app.route('/')
def about():
	return "tes"
	"""

from image_compress import *

img_compress("src/static/uploads/sana.jpg",50)
