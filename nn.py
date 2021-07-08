import numpy as np


class NeuralNetwork():

    def __init__(self, layer_sizes):

        # TODO
        # layer_sizes example: [4, 10, 2]
        self.W1 = np.random.normal(size=(layer_sizes[1], layer_sizes[0])) 
        self.b1 = np.random.normal(size=(layer_sizes[1], 1)) 

        self.W2 = np.random.normal(size=(layer_sizes[1], layer_sizes[2]))         
        self.b2 = np.random.normal(size=(layer_sizes[2], 1)) 

    def activation(self, x, function):
        
        # TODO
        if function == "sigmoid":
            return 1 / (1 + np.exp(-x))

        elif function == "tanh":
            return np.tanh(x)

        elif function == "Leaky-relu":
            return np.where(x > 0, x, x * 0.01) 

    def forward(self, x):
        
        # TODO
        # x example: np.array([[0.1], [0.2], [0.3]])
        Z1 = self.W1 @ x + self.b1
        A1 = self.activation(Z1, "Leaky-relu")

        Z2 = self.W2 @ A1 + self.b2
        A2 = self.activation(Z2, "tanh")
        return A2
