import random


def read_field(path):
    """
    (str) -> (data)
    :param path:
    :return:
    """
    letters = 'ABCDEFGHIJ'
    field = {}
    with open(path, encoding='utf-8', errors='ignore') as content:
        data = content.readlines()
        for letter in letters:
            field[letter] = field.setdefault(letter,
                                             list(data[letters.index(letter)].
                                                  strip('\n')))
            while len(field[letter]) != 10:
                field[letter].append('')
            field[letter].append('\n')

    return field


def has_ship(field, cordinates):
    """
    (data, tuple) -> (bool)
    :return:
    """
    return True if field[cordinates[0]][cordinates[1]-1] == '*' else False


def ship_size(data, cordinates):
    letters = 'ABCDEFGHIJ'
    size = 1
    position = cordinates[1] - 1
    vertecal = []
    horisontal = data[cordinates[0]]
    workspace = horisontal[:position]
    workspace.reverse()
    if data[cordinates[0]][position] != "*":
        return 0, 0
    for point in workspace:
        if point == "*":
            size += 1
        else:
            break
    workspace1 = horisontal[position + 1:]

    for point in workspace1:
        if point == "*":
            size += 1
        else:
            break
    for key in data:
        vertecal.append(data[key][position])
    if size > 1:
        horisontal = True
    else:
        horisontal = False
    workspace = vertecal[:letters.index(cordinates[0])]
    workspace.reverse()
    workspace1 = vertecal[letters.index(cordinates[0])+1:]
    for point in workspace:
        if point == "*":
            size += 1
        else:
            break
    for point in workspace1:
        if point == "*":
            size += 1
        else:
            break
    if horisontal:
        return size, 1
    return 1, size


def is_valid(data):
    size_lst = []
    for key in data:
        for point in range(len(data[key])):
            cord = (key, point)

            size = max(ship_size(data, cord))
            size_lst.append(size)
    one = 0
    two = 0
    three = 0
    four = 0
    for elements in size_lst:
        if elements == 4:
            four += 1
        elif elements == 3:
            three += 1
        elif elements == 2:
            two += 1
        elif elements == 1:
            one += 1
    if [one, two/2, three/3, four/4] == [4, 3, 2, 1]:
        return True
    return False


def field_to_str(data):
    """
    (data) -> (str)
    This function converts a field in list of lists format(matrix)
    to string format
    """
    line = "        -----|-----|-----|-----|-----|-----|--" \
           "---|-----|-----|-----\n"
    nums_str = "          1     2     3     4     5     6  " \
               "   7     8     9     10     \n"
    field_str = ""+nums_str+line
    letters = "ABCDEFGHIJ"
    for key in data:
        field_str += "    "+key+"  |"
        for j in range(1, len(data[key])):
            field_str += "  " + data[key][j]+"  |"
        field_str += "\n"
        field_str += line
    return field_str


def generate():
    field, ship = {}, {4: [1], 3: [1, 1], 2: [1, 1, 1], 1: [1, 1, 1, 1]}
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
                    hor_up = field[letters[letters.index(y)-1]]
                    hor_down = []
                else:
                    hor_up = field[letters[letters.index(y) - 1]]
                    hor_down = field[letters[letters.index(y) + 1]]
                vertical = [field[key][x] for key in field]
                vertical_up = [field[key][x-1] for key in field]
                vertical_down = [field[key][x+1] for key in field]
                if direc == "h":
                    if '*' not in field[y][x: x + 2 + key] and x <= 10 - key:
                        try:
                            work1 = horizontal[:x]
                            work2 = horizontal[x + 1:]
                            if work1[-1] == "*":
                                continue
                            elif work2[0] == "*":
                                continue
                            wor1 = hor_up[x-1:x+key+1]
                            wor2 = hor_down[x-1:x+key+1]
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
                                           letters.index(y) + 2 + key] and \
                                           letters.index(y) <= 10 - key:
                        try:
                            work1 = horizontal[:x]
                            work2 = horizontal[x + 1:]
                            if work1[-1] == "*":
                                continue
                            elif work2[0] == "*":
                                continue
                            wor1 =\
                                vertical_up[letters.index(y) -
                                            1:letters.index(y)+key+1]
                            wor2 = vertical_down[letters.index(y) -
                                                 1:letters.index(y)+key+1]
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
                for keys in range(letters.index(y), letters.index(y) + key):
                    field[letters[keys]][x] = "*"
            elif direc == "h":
                ship[key].remove(1)
                for elements in range(x + 1, x + 1 + key):
                    field[y][elements] = '*'
    return field


def generate_field():
    field = generate()
    while not is_valid(field):
        field = generate()
    return field
