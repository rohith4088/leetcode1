import tensorflow as tf
from tensorflow import keras
from keras import layers , models

def CreateConvolutionaLayer(filter,kernelsize,activation = 'relu',input_shape = None):
    if input_shape:
        return layers.Conv2D(filters=filter,kernel_size=kernelsize,activation=activation,input_shape = input_shape)
    else:
        return layers.Conv2D(filters=filter,kernel_size=kernelsize,activation=activation)
def create_MaxPool(self,poolsize):
    return layers.MaxPool2D(pool_size=poolsize)

def CreateDenseLayer(units,activation):
    return layers.Dense(units=units,activation=activation)
def build_network(inputshape):
    model = models.Sequential()
    model.add(CreateConvolutionaLayer(32,(3,3),activation='relu',input_shape = inputshape))
    model.add(create_MaxPool(3,3))
    model.add(CreateConvolutionaLayer(64,(3,3),activation='relu'))
    model.add(create_MaxPool(2,2))
    model.add(CreateConvolutionaLayer(64,(3,3),activation='relu'))
    model.add(layers.Flatten())
    model.add(CreateDenseLayer(64,activation='relu'))
    model.add(CreateDenseLayer(10,activation='softmax'))
    model.compile(optimizer='adam',loss = 'categorical_crossentropy',metrics=['accuracy'])
    return model
(train_images,train_labels),(test_images,test_labels) = tf.keras.datasets.fashion_mnist.load_data()
train_images = train_images.reshape((60000,28,28,1)).astype('float32')/255
test_images = test_images.reshape((10000,28,28,1)).astype('float32')/255
train_labels = tf.keras.utils.to_categorical(train_labels)
test_labels = tf.keras.utils.to_categorical(test_labels)
num_classes = 10
input_shape = (28,28,1)
model = build_network(input_shape)
model.fit(train_images,train_labels,epochs = 10,batch_size=32,validation_split=0.2)



