GEAR_SYMBOL = "*"
total = 0

def fill(i, j, map, tree_map):
    while j < len(map[0]) and map[i][j].isdigit():
        tree_map[i][j] = 1
        j += 1

def get_digit_position(i, j, map):
    initial_j = j
    # it is possible that we hit the middle of the number, in which case we want to go back to the beginning of the number
    while initial_j >= 0 and map[i][initial_j].isdigit():
        initial_j -= 1
    while j < len(map[0]) and map[i][j].isdigit():
        j += 1
    
    return i, (initial_j + 1, j)

def explored(position):
    a, b = position
    j1, j2 = b
    while j1 < j2:
        if tree_map[a][j1] == 1:
            return True
        j1 += 1
    return False

def get_gear_pair(i, j, map, tree_map):
    if tree_map[i][j] == 1:
        return 0
    directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
    pair_count = 0
    pair_count_positions = []
    number = 0
    position = ()
    for dx, dy in directions:
        x, y = i + dx, j + dy
        if 0 <= x < len(map) and 0 <= y < len(map[0]):
            if map[x][y].isdigit():
                temp_number = get_number(x, y, map)
                temp_position = get_digit_position(x, y, map)
                if temp_number == 0 or explored(temp_position):
                    continue
                if temp_position not in pair_count_positions:
                    pair_count_positions.append(temp_position)
                    pair_count += 1
                number = temp_number
                position = temp_position
            
    return number, position if pair_count == 1 else 0
                
    
def get_gear_ratio(i, j, map, tree_map):
    if tree_map[i][j] == 1:
        return 0
    if map[i][j].isdigit():
        cur_number = get_number(i, j, map)
        a, b = get_digit_position(i, j, map)
        fill(i, j, map, tree_map)
        pair_count = 0
        gear_pair = 0
        gear_pair_positions = []
        for x in range(a - 1, a + 2):
            for y in range(b[0] - 1, b[1] + 1):
                if 0 <= x < len(map) and 0 <= y < len(map[0]):
                    if map[x][y] != GEAR_SYMBOL:
                        continue
                    temp, gear_pair_position = get_gear_pair(x, y, map, tree_map)
                    if temp == 0 or gear_pair_position == 0:
                        continue
                    if gear_pair_position not in gear_pair_positions:
                        gear_pair_positions.append(gear_pair_position)
                        pair_count += 1
                    gear_pair = temp
        if pair_count == 1:
            print(f"cur_number: {cur_number}  gear pair: {gear_pair}  gear_pair_positions: {gear_pair_positions}")
        return cur_number * gear_pair if pair_count == 1 else 0
    return 0

def get_number(i, j, map):
    # increment j until the first non-digit character is found
    # Eg. if map[i][j] is "4", map[i][j + 1] is "5", map[i][j + 2] is " ", then return "45"
    number = ""
    # it is possible that we hit the middle of the number, in which case we want to go back to the beginning of the number
    while j >= 0 and map[i][j].isdigit():
        j -= 1
    j += 1
    while j < len(map[0]) and map[i][j].isdigit():
        number += map[i][j]
        j += 1
    return int(number)

with open("day-three.in", 'r') as file:
    map = [list(line.strip()) for line in file]
    # to keep track of numbers examined
    tree_map = [[0 for i in range(len(map[0]))] for j in range(len(map))]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j].isdigit():
                gear_ratio = get_gear_ratio(i, j, map, tree_map)
                total += gear_ratio

print(total)
