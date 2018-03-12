class Ship:
    """
    This class represents ship and his methods
    """
    def __init__(self, bow, horizontal, lenght, hit):
        self.bow = bow
        self.horizontal = horizontal
        self.__length = lenght
        self.__hit = hit[:]

    def get_cordanates(self):
        """
        Makes list with cordinates all point of ship
        :return:
        """
        letters = "ABCDEFGHIJ"
        cordinates = []
        if self.horizontal:
            for point in range(1, max(self.__length)):
                cordinates.append((self.bow[0], self.bow[1] + point))
        elif not self.horizontal:
            for point in range(1, max(self.__length)):
                cordinates.append((letters[letters.index(self.bow[0]) + point],
                                  self.bow[1]))
        return cordinates

    def shoot_at(self, cordinates):
        """
        Shoot to point of ship
        :param cordinates:
        :return:
        """
        self.__hit.append(cordinates)
