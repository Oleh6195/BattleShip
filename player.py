class Player:
    """
    This class represents player
    """
    num = 1

    def __init__(self, name):
        self.name = name
        self.id = Player.num
        Player.num += 1

    def read_position(self):
        """
        Give a request to enter cordinates
        :return:
        """
        letters = "ABCDEFGHIJ"
        try:
            position = input(self.name + ", enter move: ")
            x = str(position[0])
            y = int(position[1])
            if x in letters and y in range(10):
                return x, y
            else:
                print("Enter validate cordinates(example: B1)")
                return 0
        except:
            print("Enter validate cordinates(example: B1)")
            return 0
