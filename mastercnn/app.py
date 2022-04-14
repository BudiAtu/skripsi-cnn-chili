# Import libraries

# Flask 
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array

import numpy as np
import os
import sys
import glob
import re
import h5py

import PIL
from PIL import Image

# Buat flask instance
app = Flask(__name__)


# Load model

MODEL_ARCHITECTURE =  'model/model_plant_disease_1.json'   
MODEL_WEIGHTS = 'model/model_plant_disease_weight.h5'

json_file = open(MODEL_ARCHITECTURE)
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)

model.load_weights(MODEL_WEIGHTS)
print('@@ Model loaded. Check http://127.0.0.1:5000/')



def model_predict(img_path, model):
  test_image = load_img(img_path, target_size = (128, 128)) # load image 
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 # normalisasi dan ubah ke array
  test_image = np.expand_dims(test_image, axis = 0) 
  
  
  result = model.predict(test_image) # prediksi 
  
  pred = np.argmax(result, axis=1) # ambil indexnya



# 3/4/6/10/14/17/19/22/23/24/27/37
           
  if   pred == 1: #Apple___Apple_scab
      return 'Tanamanmu Sakit', 'virus_gemini.html' # sudah diisi   
  elif pred == 2: #Apple___Cedar_apple_rust
      return 'Tanamanmu Sakit', 'virus_kerupuk.html'  
  else:
      return "Tanamanmu Sehat", 'healthy_plant.html'
    
    


# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')
    
# ambil input gambar lalu prediksi dan menampilkan halaman .html 
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = model_predict(file_path, model)
              
        return render_template(output_page, pred_output = pred, user_image = file_path)
    
# for local system & cloud
if __name__ == "__main__":
    app.run(threaded=False,) 
    
    