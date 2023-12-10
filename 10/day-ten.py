from collections import deque

def is_invalid(prev, next, grid):
    prev_x, prev_y = prev
    next_x, next_y = next
    prev_tile = grid[prev_x][prev_y]
    next_tile = grid[next_x][next_y]

    from_north = ['|', '7', 'F']
    from_south = ['|', 'L', 'J']
    from_east = ['-', '7', 'J']
    from_west = ['-', 'L', 'F'] 

    valid_neighbors = {
        '|': {'N': from_north, 'S': from_south},
        '-': {'E': from_east, 'W': from_west},
        'L': {'N': from_north, 'E': from_east},
        'J': {'N': from_north, 'W': from_west},
        '7': {'S': from_south, 'W': from_west},
        'F': {'S': from_south, 'E': from_east},
        'S': {'N': from_north, 'S': from_south, 'E': from_east, 'W': from_west}
    }

    if prev_x == next_x:
        direction = 'E' if prev_y < next_y else 'W'
    else:
        direction = 'S' if prev_x < next_x else 'N'

    return next_tile not in valid_neighbors.get(prev_tile, {}).get(direction, [])

def find_farthest_point(grid, s_pos):
    distances = {}
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    frontier = deque([(s_pos, 0)])

    while frontier:
        cur, dist = frontier.popleft()

        if cur not in distances:
            print(cur, dist)
            distances[cur] = dist

            for direction in directions:
                new_x, new_y = cur[0] + direction[0], cur[1] + direction[1]
                new_pos = (new_x, new_y)
                if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]) or is_invalid(cur, new_pos, grid):
                    continue
                frontier.append((new_pos, dist + 1))

    return max(distances.values())



with open("day-ten.in", "r") as f:
    grid = []
    s_pos = (0, 0)
    for line in f:
        row = []
        for char in line.strip():
            if char == "S":
                s_pos = (len(grid), len(row))
            row.append(char)
        grid.append(row)
    print(find_farthest_point(grid, s_pos))