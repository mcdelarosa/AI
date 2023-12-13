import time

from singleton_meta import SingletonMeta
from highway import Highway
from ANN import ANN
from car import Car

class Game(metaclass=SingletonMeta):
    def __init__(self):
        self.running = True
        self.car = Car(2)
        self.high_way = Highway(3)
        self.reset()
        self.player = ANN()
    def reset(self):
        self.car.reset()
        self.high_way.reset()
        self.running = True

    def play(self):
        while self.running and not self.high_way.is_finished():
            next_move = self.player.matrixReader(self.high_way.road, self.car.l_pos)
            self.car.moveCar(next_move)
            self.high_way.move_highway()
            time.sleep(2)
            self.print_highway()



    def print_highway(self):
        for y in range(self.high_way.window_length+1):
            for x in range(self.high_way.window_length):
                if self.check_collision(x, y):
                    self.highwayBuilder("*")
                    self.running = False
                elif self.car.pos == x and y == self.high_way.window_length:
                    self.highwayBuilder("8")
                elif self.high_way.road[y][x] == self.high_way.NOTHING:
                    self.highwayBuilder("¦")
                else:
                    self.highwayBuilder(self.high_way.road[y][x])
                if x == 2:  # to begin a new line
                    print("")
        print('-'*self.high_way.window_length*3)
        '''
        if(gameOver == True):
            exit()'''


    def highwayBuilder(self, toPrint):
        print(f"|{toPrint}|", end="")


    def check_collision(self, x, y):
        if self.car.pos == x and y == 3 and self.high_way.road[y][x] == 1:
            return True
        elif self.car.pos < 0 or self.car.pos > 2:
            return True
        else:
            return False


highwayGame = Game()

if highwayGame.running == True:
    highwayGame.play()



