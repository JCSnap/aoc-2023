# Current bag: 12 red cubes, 13 green cubes, and 14 blue cubes

max_red_count = 12
max_green_count = 13
max_blue_count = 14

total = 0

with open('day-two.in') as f:
    for line in f:
        game_number = line[:line.find(":")].split(" ")[1]
        # Eg. 4 blue, 8 green, 5 red; 14 red, 8 blue, 1 green; 11 red, 13 green would be 3 elements in the list
        records = line[line.find(":") + 1:].split(";")
        isValid = True
        for record in records:
            red_count = 0
            green_count = 0
            blue_count = 0
            # Eg. 4 blue, 8 green, 5 red would be a list of 3 elements: "4 blue", "8 green", "5 red"
            colors = record.split(',')
            for color in colors:
                # Eg. "4 blue" would be a list of 2 elements: "4" and "blue"
                parts = color.strip().split(' ')
                number = int(parts[0])
                color_name = parts[1]
                if color_name == "red":
                    red_count += number
                elif color_name == "green":
                    green_count += number
                elif color_name == "blue":
                    blue_count += number
                else:
                    isValid = False
                    break
            if red_count > max_red_count or green_count > max_green_count or blue_count > max_blue_count:
                isValid = False
                break

        if isValid:
            total += int(game_number)
    
print(total)