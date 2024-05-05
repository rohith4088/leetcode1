import numpy as np
import matplotlib.pyplot as plt
from scipy.special import expit
from sklearn.datasets import make_moons
class NueralNetwork():
    def __init__(self,input_size,hidden_size,output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        #define the weigghts and biases

        self.W1 = np.random.randn(hidden_size,input_size) * 0.01
        self.b1 = np.zeros((hidden_size,1))
        self.W2 = np.random.randn(output_size,hidden_size) * 0.01
        self.b2 = np.zeros((output_size,1))

    def forward_propogation(self,X):
        self.Z1 = np.dot(self.W1,X) + self.b1
        self.A1 = np.tanh(self.Z1)
        self.Z2 = np.dot(self.W2,self.A1) + self.b2
        self.A2 = expit(self.Z2)

        return self.A2
    def backward_propogation(self,X,Y):
        m = X.shape[1]

        dZ2 = self.A2 - Y
        dW2 = (1 / m) * np.dot(dZ2,self.A1.T)
        db2 = (1/m) * np.sum(dZ2,axis=1,keepdims=True)
        dZ1 = np.dot(self.W2.T , dZ2) * (1 - np.power(self.A1,2))
        dW1 = (1/m) * np.dot(self.Z1,X.T)
        db1 = (1/m) * np.sum(dZ1,axis=1,keepdims=True)

        self.W2 -= dW2
        self.b2 -= db2
        self.W1 -= dW1
        self.b1 -= db1
    def cross_entropy(self,Y,A):
        m = Y.shape[1]
        loss = -(1/m) *np.sum(Y * np.log(A) + (1-Y) * np.log(1-A))
        return loss

    def train(self,X,Y,epochs,learning_rate):
        for epoch in range(epochs):
            prediction = self.forward_propogation(X)
            loss = self.cross_entropy(Y,prediction)
            self.backward_propogation(X,Y)

            if epoch % 100 == 0:
                print(f'epoch{epoch} : loss{loss}')
X,Y = make_moons(n_samples=1000,noise=0.2,random_state=42)
X = X.T
Y = Y.reshape(1,-1)

plt.scatter(X[0,:],X[1,:],c = Y.ravel(),cmap = plt.cm.Spectral)
plt.show()

input_size = 2
hidden_size = 4
output_size = 1

model = NueralNetwork(input_size, hidden_size, output_size)
model.train(X, Y, epochs=1000, learning_rate=0.01)






