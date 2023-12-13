from Neuron import Neuron

class Layer():
    '''
    Layer is modeling a layer in the fully-connected-feedforward neural network architecture.
    It will play the role of connecting everything together inside and will be doing the backpropagation
    update.
    '''

    def __init__(self, num_neuron, is_output_layer=False):

        # Will create that many neurons in this layer
        self.is_output_layer = is_output_layer
        self.neurons = []
        for i in range(num_neuron):
            # Create neuron
            neuron = Neuron(i, is_output_neuron=is_output_layer)
            self.neurons.append(neuron)

    def attach(self, layer):
        '''
        This function attaches the neurons from this layer to another one.
        This is needed for the backpropagation algorithm.
        '''
        # Iterate over the neurons in the current layer and attach
        # them to the next layer
        for in_neuron in self.neurons:
            in_neuron.attach_to_output(layer.neurons)

    def init_layer(self, num_input):
        '''
        This will initialize the weights of each neuron in the layer.
        By giving the right num_input, it will spawn the right number of weights.
        '''

        # Iterate over each of the neurons and initialize
        # the weights that connect with the previous layer
        for neuron in self.neurons:
            neuron.init_weights(num_input)

    def predict(self, row):
        '''
        This will calculate the activations for the full layer given the row of data
        streaming in.
        '''
        activations = [neuron.predict(row) for neuron in self.neurons]
        # The output of each neuron of the list self.neurons will be calculated. The result of each neurons will be saved as a list.
        return activations
