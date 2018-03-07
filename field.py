from funcs import has_ship, ship_size, field_to_str, is_valid
from ship import Ship
import random


class Field:
    """
    This class representts field
    """
    def __init__(self):
        self.empty_field = dict()
        self.score = 0
        letters = "ABCDEFGHIJ"
        for let in letters:
            self.empty_field[let] = [" " for i in range(10)]
        shipses = []

        def generate():
            """
            () -> (tuple)
            :return: tuple of field with dictionary and list
            """
            ships = []
            direc = ''
            field, ship = {}, {4: [1], 3: [1, 1], 2: [1, 1, 1],
                               1: [1, 1, 1, 1]}
            direction, letters = "vh", 'ABCDEFGHIJ'
            for letter in letters:
                field[letter] = []
                for i in range(10):
                    field[letter].append(' ')
                field[letter].append('\n')
            for key in ship:
                while ship[key] != []:

                    cordinates = ()
                    while cordinates == ():
                        y = random.choice(letters)
                        x = random.randint(0, 9)
                        direc = random.choice(direction)
                        horizontal = field[y]
                        if y == "A":
                            hor_down = field[letters[letters.index(y) + 1]]
                            hor_up = []
                        elif y == "J":
                            hor_up = field[letters[letters.index(y) - 1]]
                            hor_down = []
                        else:
                            hor_up = field[letters[letters.index(y) - 1]]
                            hor_down = field[letters[letters.index(y) + 1]]
                        vertical = [field[key][x] for key in field]
                        vertical_up = [field[key][x - 1] for key in field]
                        vertical_down = [field[key][x + 1] for key in field]
                        if direc == "h":
                            if '*' not in field[y][
                                          x: x + 2 + key] and x <= 10 - key:
                                try:
                                    work1 = horizontal[:x]
                                    work2 = horizontal[x + 1:]
                                    if work1[-1] == "*":
                                        continue
                                    elif work2[0] == "*":
                                        continue
                                    wor1 = hor_up[x - 1:x + key + 1]
                                    wor2 = hor_down[x - 1:x + key + 1]
                                    if "*" in wor1:
                                        continue
                                    if "*" in wor2:
                                        continue
                                    else:
                                        cordinates = (x, y)
                                except IndexError:
                                    pass
                        if direc == "v":
                            if "*" not in vertical[letters.index(y):
                                                   letters.index(y) +
                                                   2 + key] and \
                                                   letters.index(y) <= 10\
                                                   - key:
                                try:
                                    work1 = horizontal[:x]
                                    work2 = horizontal[x + 1:]
                                    if work1[-1] == "*":
                                        continue
                                    elif work2[0] == "*":
                                        continue
                                    wor1 = \
                                        vertical_up[letters.index(y) -
                                                    1:letters.index(
                                            y) + key + 1]
                                    wor2 = vertical_down[letters.index(y) -
                                                         1:letters.index(
                                        y) + key + 1]
                                    if "*" in wor1:
                                        continue
                                    if "*" in wor2:
                                        continue
                                    else:
                                        cordinates = (x, y)
                                except IndexError:
                                    continue
                    if direc == "v":

                        ship[key].remove(1)
                        for keys in range(letters.index(y),
                                          letters.index(y) + key):
                            field[letters[keys]][x] = "*"
                    elif direc == "h":

                        ship[key].remove(1)
                        for elements in range(x + 1, x + 1 + key):
                            field[y][elements] = '*'
                    if direc == "v":
                        ships.append(((y, x), (1, key), False, []))
                    elif direc == "h":
                        ships.append(((y, x), (key, 1), True, []))

            return field, ships

        def generate_field():
            """
            Call generate while field won't be valid
            """
            field = generate()
            while not is_valid(field[0]):
                field = generate()
            return field
        field = generate_field()
        self.data = field[0]
        for ship in field[1]:
            shp = Ship(ship[0], ship[2], ship[1], ship[3])
            shipses.append(shp)

        self.ships = shipses

    def shoot_at(self, cordinates):
        """
        :param cordinates:
        Change point which user shooted in
        """
        status = False
        for ship in self.ships:
            if cordinates in ship.get_cordanates():
                status = True
                self.score += 1
                ship.shoot_at(cordinates)
        if status:
            self.empty_field[cordinates[0]][cordinates[1]] = \
                '\033[1;31mX\033[1;m'
            self.data[cordinates[0]][cordinates[1]] = \
                '\033[1;31mx\033[1;m'

        else:
            self.empty_field[cordinates[0]][cordinates[1]] = 'X'
            self.data[cordinates[0]][cordinates[1]] = 'X'
        return status

    def field_with_ships(self):
        return field_to_str(self.data)

    def field_without_ships(self):
        return field_to_str(self.empty_field)

    def winner(self):
        lst = []
        for ship in self.ships:
            if ship.length == len(ship.hit):
                lst.append(True)
        if len(lst) == 10:
            return True
        return False
