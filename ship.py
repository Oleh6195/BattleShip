class Ship:
    def __init__(self, bow, horizontal, lenght, hit):
        self.bow = bow[:]
        self.horizontal = horizontal
        self.length = lenght
        self.hit = hit[:]

    def get_cordanates(self):
        letters = "ABCDEFGHIJ"
        cordinates = []
        if self.horizontal:
            for point in range(1, max(self.length)):
                cordinates.append((self.bow[0], self.bow[1] + point))
        elif not self.horizontal:
            for point in range(1, max(self.length)):
                cordinates.append(letters[letters.index(self.bow[0]) + point],
                                  self.bow[1])
        return cordinates

    def shoot_at(self, cordinates):
        tuple(list(self.hit).append(cordinates))
