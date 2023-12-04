# Current bag: 12 red cubes, 13 green cubes, and 14 blue cubes

total = 0

with open('day-two.in') as f:
    for line in f:
        game_number = line[:line.find(":")].split(" ")[1]
        # Eg. 4 blue, 8 green, 5 red; 14 red, 8 blue, 1 green; 11 red, 13 green would be 3 elements in the list
        records = line[line.find(":") + 1:].split(";")
        isValid = True
        smallest_red_count = 0
        smallest_green_count = 0
        smallest_blue_count = 0
        for record in records:
            # Eg. 4 blue, 8 green, 5 red would be a list of 3 elements: "4 blue", "8 green", "5 red"
            colors = record.split(',')
            for color in colors:
                # Eg. "4 blue" would be a list of 2 elements: "4" and "blue"
                parts = color.strip().split(' ')
                number = int(parts[0])
                color_name = parts[1]
                if color_name == "red":
                    if number > smallest_red_count:
                        smallest_red_count = number
                elif color_name == "green":
                    if number > smallest_green_count:
                        smallest_green_count = number
                elif color_name == "blue":
                    if number > smallest_blue_count:
                        smallest_blue_count = number
                else:
                    isValid = False
                    break
        power = smallest_red_count * smallest_blue_count * smallest_green_count
        total += power

print(total)

