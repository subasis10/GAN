from flask import Flask,render_template, request,url_for,redirect
import os
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from keras.preprocessing.image import save_img
from numpy import load
from numpy import expand_dims
from matplotlib import pyplot

# load an image
def load_image(filename, size=(256,256)):
  # load image with the preferred size
  pixels = load_img(filename, target_size=size)

  # convert to numpy array
  pixels = img_to_array(pixels)
  # scale from [0,255] to [-1,1]
  pixels = (pixels - 127.5) / 127.5
  # reshape to 1 sample
  pixels = expand_dims(pixels, 0)
  return pixels

#MODEL
### load model
model = load_model('5.h5')
### generate image from source

### scale from [-1,1] to [0,1]
##

UPLOAD_FOLDER = 'uploads/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")

def index():
    
    return render_template('index.html')

@app.route('/success/')
def success():
   return render_template('success.html')

@app.route('/predict',methods=['POST'])
def predict():
        
   
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    src_image = load_image(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    gen_image = model.predict(src_image)
    gen_image = (gen_image + 1) / 2.0
 
    save_img('test.jpg', gen_image[0])
    return redirect(url_for('success'),url="test.jpg")

if __name__ == "__main__":
    app.run(debug = True)
