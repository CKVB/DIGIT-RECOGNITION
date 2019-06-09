from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Activation,Dropout,Flatten
from keras.layers.convolutional import Conv2D,MaxPooling2D
from keras.optimizers import Adam
from keras.utils import np_utils
import numpy as np 
import matplotlib.pyplot as plt

np.random.seed(1)
EPOCHS=15
OPTIMIZER=Adam()
VALIDATION_SPLIT=0.2
CLASSESS=10
DROP_OUT=0.2
BATCH_SIZE=150

(xtrain,ytrain),(xtest,ytest)=mnist.load_data()
xtrain=xtrain.reshape(xtrain.shape[0],xtrain.shape[1],xtrain.shape[2],1)
xtest=xtest.reshape(xtest.shape[0],xtest.shape[1],xtest.shape[2],1)
xtrain=xtrain/255
xtest=xtest/255
ytrain=np_utils.to_categorical(ytrain,CLASSESS)
ytest=np_utils.to_categorical(ytest,CLASSESS)
INPUT_SHAPE=(xtrain.shape[1],xtrain.shape[2],1)

model=Sequential()
model.add(Conv2D(50,(5,5),input_shape=INPUT_SHAPE))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(50,(4,4)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(DROP_OUT))
model.add(Flatten())
model.add(Dense(CLASSESS))
model.add(Activation("softmax"))

model.compile(loss="categorical_crossentropy",optimizer=OPTIMIZER,metrics=["accuracy"])

temp=model.fit(xtrain,ytrain,epochs=EPOCHS,batch_size=BATCH_SIZE,validation_split=VALIDATION_SPLIT)

model.save("digits.h5")
plt.plot(temp.history["acc"])
plt.plot(temp.history["val_acc"])
plt.legend(["ACCURACY","VAL_ACC"])
plt.title("ACCURACY")
plt.xlabel("EPOCHS")
plt.show()