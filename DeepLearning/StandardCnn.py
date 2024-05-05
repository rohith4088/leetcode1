import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense,MaxPooling2D,Conv2D,Flatten
from keras.utils import to_categorical
from keras.datasets import mnist

(train_images , train_labels) , (test_images,test_labels) = mnist.load_data()
train_images = train_images.reshape(60000,28,28,1).astype('float32')/255
test_images = test_images.reshape(10000,28,28,1).astype('float32')/255
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
model = Sequential()
model.add(Conv2D(32,(3,3),activation='relu',input_shape = (28,28,1)))
model.add(MaxPooling2D(2,2))
model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D(2,2))
model.add(Conv2D(64,(3,3),activation='relu'))
model.add(Flatten())
model.add(Dense(62,activation='relu'))
model.add(Dense(10,activation='softmax'))
model.compile(optimizer='adam',loss = 'categorical_crossentropy',metrics = ['acc'])
model.fit(train_images,train_labels,epochs = 10,batch_size = 32,validation_split = 0.2)