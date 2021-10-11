
##Importing the libraries
from flask import Flask, render_template, request
import numpy as np
import os
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model

##load model
model = load_model("cott_plant_disease2.h5")
print("model loaded")

def pred_cot_disease(cott_plant):
  test_image = load_img(cott_plant, target_size = (150,150))
  print("Got the image for prediction")
  test_image = img_to_array(test_image)/255
  test_image =np.expand_dims(test_image, axis=0)
  result = model.predict(test_image).round(3)
  print("Raw Result: ", result)
  preds = np.argmax(result)
  if preds==0:
    preds="The leaf is diseased cotton leaf"
    return preds
  elif preds==1:
    preds="The leaf is diseased cotton plant"
    return preds
  elif preds==2:
    preds="The leaf is fresh cotton leaf"
    return preds
  else:
    preds="The leaf is fresh cotton plant"
    return preds

from flask_ngrok import run_with_ngrok
from werkzeug.utils import secure_filename
##Create Flask App
app = Flask(__name__)
#render index2.html
@app.route("/", methods=["GET"])
def home():
  return render_template("index2.html")

#get input image and then predict class
@app.route("/predict", methods=["POST"])
def predict():
   if request.method == 'POST':
     # Get the file from post request
     f = request.files['file']
     filename = f.filename
     print("file name: ", filename)
     # Save the file to ./uploads
     basepath = os.path.dirname(__file__)
     file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
     f.save(file_path)

     # Make prediction
     pred = pred_cot_disease(cott_plant=file_path)
     return pred



if __name__ == '__main__':
    app.run(debug=True)