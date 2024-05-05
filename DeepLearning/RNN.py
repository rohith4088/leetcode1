import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import SimpleRNN , Dense , Embedding
from keras.preprocessing import sequence
from keras.datasets import imdb

maxfeatures = 10000
maxlen = 500

(input_train , ytrain) , (input_test,ytest) = imdb.load_data(num_words=maxfeatures)
input_train = sequence.pad_sequences(input_train , maxlen = maxlen)
input_test = sequence.pad_sequences(input_test , maxlen = maxlen)
model = Sequential()
model.add(Embedding(maxfeatures , 32))
model.add(SimpleRNN(32))
model.add(Dense(1,activation='relu'))
model.compile(optimizer = 'rmsprop' , loss = 'binary_crossentropy' , metrics = ['acc'])
model.fit(input_train,ytrain,epochs = 10,batch_size = 32,validation_split = 0.2)
score = model.evaluate(input_test,ytest)
print(f'loss{score[0]}')
print(f'test loss {score[1]}')
