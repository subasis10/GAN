from tkinter import *
  
# loading Python Imaging Library 
from PIL import ImageTk, Image 
  
# To get the dialog box to open when required  
from tkinter import filedialog


from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img,save_img
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

# load model
model = load_model('5.h5')
# generate image from source
#gen_image = model.predict(src_image)



# Create a windoe 
root = Tk()
def open_img(): 
	# Select the Imagename from a folder 
	x = openfilename()
	src_image = load_image(x)
	gen_image = model.predict(src_image)
	gen_image = (gen_image + 1) / 2.0
	save_img('test.jpg', gen_image[0])
	# opens the image 
	img = Image.open(x) 
	
	# resize the image and apply a high-quality down sampling filter 
	img = img.resize((256, 256), Image.ANTIALIAS)
	save_img('test.jpg', gen_image[0])
	# PhotoImage class is used to add image to widgets, icons etc 
	img = ImageTk.PhotoImage(img) 

	# create a label 
	panel = Label(root, image = img) 
	
	# set the image as img 
	panel.image = img 
	panel.grid(row = 2,column = 0 )

def convert(): 

	img = Image.open('test.jpg') 
	
	# resize the image and apply a high-quality down sampling filter 
	img = img.resize((256, 256), Image.ANTIALIAS) 

	# PhotoImage class is used to add image to widgets, icons etc 
	img = ImageTk.PhotoImage(img) 

	# create a label 
	panel = Label(root, image = img) 
	
	# set the image as img 
	panel.image = img 
	panel.grid(row = 2,column = 1)
	
def openfilename(): 

	# open file dialog box to select image 
	# The dialogue box has a title "Open" 
	filename = filedialog.askopenfilename(title ='"pen') 
	return filename 

# Set Title as Image Loader 
root.title("Map generator")

root.geometry("600x600")

# Set the resolution of window 
# Allow Window to be resizable 
root.resizable(width = True, height = True) 
placeholder = Image.open('placeholder.gif')
placeholder = ImageTk.PhotoImage(placeholder) 
# Create a button and place it into the window using grid layout 
btn = Button(root, text ='open image', command = open_img).grid(row = 0, column = 0)
btn = Button(root, text ='convert', command = convert).grid(row = 0, column = 1)
panel1 = Label(root, image = placeholder) 
panel1.grid(row = 2,column = 1)
panel1.image = placeholder 
panel2 = Label(root, image = placeholder) 
panel2.grid(row = 2,column = 0)
panel2.image = placeholder 
root.mainloop() 



