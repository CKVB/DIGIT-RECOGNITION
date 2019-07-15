from PIL import Image
import numpy as np
from keras.models import load_model
model=load_model("digits.h5")
def predict2(img):
		img=Image.open(img).convert("1")
		img = img.resize((28,28))
		im2arr = np.array(img)
		im2arr = im2arr.reshape(1,28,28,1)
		y_pred = model.predict_classes(im2arr,verbose=0)
		return(y_pred)
