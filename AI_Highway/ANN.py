import pickle

class ANN():
    def __init__(self):
        self.ANN_builder()

    def ANN_builder(self):
        with open('trained_model.pkl', 'rb') as f:  # 'rb' = read binary
            self.t_model = pickle.load(f) # deserialize using load()
    def matrixReader(self, matrix, car_pos):
        list = [value for row in matrix for value in row]
        ''' 
        list = []
        for row in matrix:
            for value in row:
                list.append(value)'''
        X = list
        for i in car_pos:
            X.append(i) #add cars positions [0,0,1]
        return self.t_model.simple_result(X)
