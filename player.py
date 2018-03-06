class Player:
    num = 1

    def __init__(self, name):
        self.name = name
        self.id = Player.num
        Player.num += 1

    def read_position(self):
        position = input(self.name + ", enter move: ")
        x = str(position[0])
        y = int(position[1])
        return x, y
