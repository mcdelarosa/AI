import random
from Layer import Layer

class MultiLayerPerceptron():
    '''
    We will be creating the multi-layer perceptron with only two layers:
    an input layer, a perceptrons layer, and a one-neuron output layer which does binary classification.
    '''

    def __init__(self, learning_rate=0.01, num_iteration=1000):

        # Layers
        self.layers = []

        # Training parameters
        self.learning_rate = learning_rate
        self.num_iteration = num_iteration

    def add_output_layer(self, num_neuron):
        '''
        This helper function will create a new output layer and add it to the architecture.
        '''
        self.layers.insert(0, Layer(num_neuron, is_output_layer=True)) # puts the outputlayer in the front

    def add_hidden_layer(self, num_neuron):
        '''
        This helper function will create a new hidden layer, add it to the architecture,
        and finally attach it to the front of the architecture.
        '''
        # Create a hidden layer
        hidden_layer = Layer(num_neuron)
        # Attach the last added layer to this new layer
        hidden_layer.attach(self.layers[0]) #first time outputlayer and second time the first hiddenlayer
        # Add this layer to the architecture as first
        self.layers.insert(0, hidden_layer) #first time hiddenlayer and output, and second time new hiddenlayer, hiddenlayer and output

    def update_layers(self, target):
        '''
        Will update all the layers by calculating the updated weights and then updating
        the weights all at once when the new weights are found.
        '''
        # Iterate over each of the layers in reverse order
        # to calculate the updated weights
        for layer in reversed(self.layers):

            # Calculate update the hidden layer
            for neuron in layer.neurons:
                neuron.calculate_update(self.learning_rate, target)

        # Iterate over each of the layers in normal order
        # to update the weights
        for layer in self.layers:
            for neuron in layer.neurons:
                neuron.update_neuron()

    def fit(self, X, y):
        '''
        Main training function of the neural network algorithm. This will make use of backpropagation.
        It will use stochastic gradient descent by selecting one row at random from the dataset and
        use predict to calculate the error. The error will then be backpropagated and new weights calculated.
        Once all the new weights are calculated, the whole network weights will be updated.
        '''
        num_row = len(X)
        num_feature = len(X[0])  # Here we assume that we have a rectangular matrix
                                 # Because of the inputs (inputlayer)
        # Init the weights throughout each of the layers
        self.layers[0].init_layer(num_feature)

        for i in range(1, len(self.layers)):
            num_input = len(self.layers[i-1].neurons)
            self.layers[i].init_layer(num_input) #initializes each weight of the remaining layers

        # Launch the training algorithm
        for i in range(self.num_iteration):
            for dset_index in range(num_row):
                row = X[dset_index]
                self.predict(row)
                target = y[dset_index]
                # Update the layers using backpropagation
                self.update_layers(target)

            # At every 1000 iterations, we calculate the error
            # on the whole training set
            if i % 1000 == 0:
                total_error = 0
                for r_i in range(num_row):
                    row = X[r_i] # row = all the inputs of the ANN
                    yhat = self.predict(row)
                    error = (y[r_i] - yhat)
                    total_error = total_error + error**2
                mean_error = total_error / num_row
                print(f"Iteration {i} with error = {mean_error}")
    def result(self,X):
        yhat =[]
        num_row = len(X)
        for dset_index in range(num_row):
            row = X[dset_index]
            yhat.append(self.simple_result(row))
        return yhat

    def simple_result(self,row):
        return self.predict(row)

    def predict(self, row):
        '''
        Prediction function that will take a row of input and give back the output
        of the whole neural network.
        '''

        # Gather all the activations in the hidden layer
        activations = self.layers[0].predict(row) # the output of the first hiddenlayer neurons are calculated
        for i in range(1, len(self.layers)):
            activations = self.layers[i].predict(activations) #output of the next layers until hiddenlayer

        outputs = []

        for activation in activations:
            #Decide if the output is 0, 0.5 or 1
            if activation <= 0.25:
                outputs.append(0)
            elif activation >= 0.75:
                outputs.append(1)
            else:
                outputs.append(0.5)

        # We currently have only one output allowed
        return outputs[0]
