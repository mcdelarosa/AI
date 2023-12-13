import sys

from MultiLayer import MultiLayerPerceptron
import pickle

X = []
y = []
def read_txt_file(file_name, max=16):

    try:
        with open(file_name, 'r') as file:
            for line in file:
                values = line.strip().split(',')
                if len(values) == max:
                    as_X_int =[float(x) if x.isdigit() else float(x) for x in values[:15]] # ==  as_X_int =[float(x) for x in values[:15]]
                    X.append(as_X_int)
                    y.append(float(values[max-1]))
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")

    return X, y


def training(serialize=False):
    # Call the function with the name of your .txt file
    file_name = 'training.txt'
    X, y = read_txt_file(file_name)
    # Init the parameters for the network
    clf = MultiLayerPerceptron(learning_rate = 0.056, num_iteration = 30000)
    # Create the architecture backward
    clf.add_output_layer(num_neuron = 1)
    clf.add_hidden_layer(num_neuron = 3)

    # Train the network
    clf.fit(X,y)

    if serialize:
        print("... saving model")
        with open('trained_model.pkl', 'wb') as f:  # create a text file    'wb'= write binary
            pickle.dump(clf, f) # serialize the class of the ANN
        f.close()


def test():

    with open('trained_model.pkl', 'rb') as f:

        t_model = pickle.load(f) # deserialize using load()
        #put new inputs
        X, y = read_txt_file('test.txt')
        print(t_model.result(X))
        print('...end test')


def main(argv):

    print(f" executing ... {argv[1]}")

    if len(argv) > 2:
        serialize_model = argv[2].lower() == "true"
        print(f"serialize model = {serialize_model} ")

    if argv[1] == 'training':
        training(serialize_model)
    else:
        test()

# reference: https://machinelearningmastery.com/command-line-arguments-for-your-python-script/
if __name__ == '__main__':
    main(sys.argv)