from keras.models import load_model
from keras.datasets import mnist
from keras.utils import np_utils
model=load_model("digits.h5")
(xtrain,ytrain),(xtest,ytest)=mnist.load_data()
xtest=xtest.reshape(xtest.shape[0],28,28,1)
ytest=np_utils.to_categorical(ytest,10)
x=model.evaluate(xtest,ytest)
print("Test Score    : ",x[0])
print("Test Accuracy : ",x[1])