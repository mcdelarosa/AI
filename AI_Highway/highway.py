from map import generate_random_list
from singleton_meta import SingletonMeta


class Highway(metaclass=SingletonMeta):

    CAR = 1
    OBSTACLES = 1
    NOTHING = 0

    def __init__(self, window_length):
        self.window_length = window_length

    def load(self):
        with open('map.txt') as f:
            for line in f:
                row = [int(num) for num in line.strip().split(',')]
                self.full_highway.append(row)
        print(self.full_highway)

    def load_dynamic(self, num_rows):
        self.full_highway = generate_random_list(num_rows)

    def reset(self):
        self.full_highway = []
        # self.load()
        self.load_dynamic(100)
        self.offset = 0
        self.create_window()
        #self.lengthY = len(self.highway)
        #self.lengthX = len(self.highway[0])

    def create_window(self):
        # get from max length of full_matrix - offset - window_length
        if self.offset == 0:
            self.road = [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]]  # this creates the matrix of the highway

        else:
            self.road.pop(3)
            self.road.insert(0, self.full_highway[self.offset - 1])


    def move_highway(self):
        self.offset += 1
        self.create_window()

    def is_finished(self):
        return self.offset == len(self.full_highway)

