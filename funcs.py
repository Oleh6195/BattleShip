def read_field(path):
    """
    (str) -> (data)
    :param path:
    :return: read file with
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
    :return: True if this cordinate has ship and False if it hasn't
    """
    return True if field[cordinates[0]][cordinates[1]-1] == '*' else False


def ship_size(data, cordinates):
    """
    (dict, tuple) -> (tuple)
    :param data:
    :param cordinates:
    :return: tuple with size of ship
    """
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
    """
    (dict) -> (bool)
    This function check whether field is validate
    :param data:
    :return:
    """
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
    This function converts a field in dictionary to string format
    """
    line = "        -----|-----|-----|-----|-----|-----|--" \
           "---|-----|-----|-----\n"
    nums_str = "          1     2     3     4     5     6  " \
               "   7     8     9     10     \n"
    field_str = ""+nums_str+line
    for key in data:
        field_str += "    "+key+"  |"
        for j in range(1, len(data[key])):
            field_str += "  " + data[key][j]+"  |"
        field_str += "\n"
        field_str += line
    return field_str
