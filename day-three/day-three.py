symbols = ["%", "/", "@", "*", "+", "$", "&", "=", "-", "#"]

total = 0

def check_is_symbol(i, j, map, tree_map, is_same_row):
    if map[i][j].isdigit() and is_same_row:
        return check_has_symbols(i, j, map, tree_map)
    else:
        # return true if the character is a symbol in symbols
        return map[i][j] in symbols
    
def check_has_symbols(i, j, map, tree_map):
    # if a number has already been examined, we do not want to double count it
    if tree_map[i][j] == 1:
        return False
    has_symbol = False
    tree_map[i][j] = 1
    directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
    has_symbol = False
    for dx, dy in directions:
        x, y = i + dx, j + dy
        is_same_row = False
        # we want to differentiate whether the digit belongs to the same number if its adjacent to it
        # it only belongs to the same number if its in the same row
        if i == x:
            is_same_row = True
        if 0 <= x < len(map) and 0 <= y < len(map[0]):
            has_symbol = has_symbol or check_is_symbol(x, y, map, tree_map, is_same_row)
    return has_symbol

def get_number(i, j, map):
    # increment j until the first non-digit character is found
    # Eg. if map[i][j] is "4", map[i][j + 1] is "5", map[i][j + 2] is " ", then return "45"
    number = ""
    while j < len(map[0]) and map[i][j].isdigit():
        number += map[i][j]
        j += 1
    
    print(number)
    return int(number)

with open("day-three.in", 'r') as file:
    map = [list(line.strip()) for line in file]
    # to keep track of numbers examined
    tree_map = [[0 for i in range(len(map[0]))] for j in range(len(map))]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j].isdigit():
                has_symbol = check_has_symbols(i, j, map, tree_map)
                if has_symbol:
                    number = get_number(i, j, map)
                    total += number
print(total)
