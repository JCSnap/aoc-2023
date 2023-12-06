
def get_distance(speed, time):
    return speed * time

with open("day-six.in", "r") as f:
    # Part 1
    lines = f.read().strip().split('\n')

    times = [int(time) for time in lines[0].split()[1:]]
    distances = [int(distance) for distance in lines[1].split()[1:]]

    total = 1
    for i in range(len(times)):
        count = 0
        for j in range(times[i]): # j represents the seconds spent holding the button
            time_moving = times[i] - j
            distance = get_distance(j, time_moving) # speed is the number of seconds spent holding the button
            if distance > distances[i]:
                count += 1

        total *= count

    print("Part 1:", total)

