# read the file from day-three.in and print out all unique characters in the file
with open("day-three.in", 'r') as file:
    map = [list(line.strip()) for line in file]
    unique_characters = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] not in unique_characters:
                unique_characters.append(map[i][j])
    
    
    unique_characters = list(filter(lambda x: not x.isdigit(), unique_characters))

    print(unique_characters)