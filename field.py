from funcs import has_ship, generate_field, ship_size, field_to_str
from ship import Ship


class Field:
    def __init__(self):
        self.data = generate_field()
        self.empty_field = dict()
        letters = "ABCDEFGHIJ"
        for let in letters:
            self.empty_field[let] = [" " for i in range(10)]

        def info_ship(data):
            shipses = []
            ships = []
            finish_ships = []
            shps = []
            for key in self.data:
                for star in range(len(data[key])):
                    if has_ship(data, (key, star)):
                        ships.append([key, star, ship_size(data, (key,
                                                                  star)),
                                      (), True])
            for ship in ships:
                if ship[2] == (1, 1):
                    shps.append(ship)
                    ships.remove(ship)

            for ship1 in ships:
                space = []
                if ship1[2][1] == 1:
                    horizontal = True
                    ship1.append(True)
                else:
                    horizontal = False
                    ship1.append(False)
                for ship2 in ships:

                    if horizontal:
                        if ship2[0] == ship1[0] and ship2[2] == ship1[2]:
                            space.append(ship2)
                    elif not horizontal:
                        if ship1[1] == ship2[1] and ship2[2] == ship1[2]:
                            space.append(ship2)
                try:
                    finish_ships.append(max(space))
                except ValueError:
                    continue
            finish_ships.extend(shps)
            fs = set(tuple(i) for i in finish_ships)
            for ship in fs:
                shp = Ship((ship[0], ship[1]), ship[4], ship[2], ship[3])
                shipses.append(shp)
            return shipses
        shs = info_ship(self.data)
        self.ships = shs

    def shoot_at(self, cordinates):
        status = False
        for ship in self.ships:
            if cordinates in ship.get_cordanates():
                status = True
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
