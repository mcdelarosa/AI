class Car():
    pos = 1
    MAX_POS = 2
    l_pos = [0,1,0]
    def __init__(self, MAX_POS):
        self.MAX_POS = MAX_POS
    def moveCar(self, ANN_output):
        print(f"AI_output=[{ANN_output}]  {type(ANN_output)}")
        if ANN_output == 0:
            print('left')
            self.left()
        elif ANN_output == 1:
            print('right')
            self.right()
        elif ANN_output == 0.5:
            self.stay()
        self.pos_simulation()

    def left(self):
        self.pos -= 1
        #if self.pos > 0:


    def right(self):
        self.pos += 1
        #if self.pos > self
        # .MAX_POS:
    def stay(self):
        self.pos = self.pos

    def reset(self):
        self.pos = 1
    def pos_simulation(self):
        if self.pos == 0:
            self.l_pos = [1,0,0]
        elif self.pos == 1:
            self.l_pos = [0,1,0]
        elif self.pos == 2:
            self.l_pos = [0,0,1]

