
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

    # Part 2 (brute force)
    # convert the integers in times to a single int by appending them, eg. [1, 2, 3] -> 123
    time = int("".join([str(i) for i in times]))
    distance = int("".join([str(i) for i in distances]))

    count = 0
    for i in range(time):
        time_moving = time - i
        distance_moving = get_distance(i, time_moving)
        print(f"time_moving: {time_moving}  distance: {distance_moving}  count: {count}")
        if distance_moving > distance:
            count += 1

    print("Part 2:", count)

# 35961505
# You can also do it the math way, solving the quadratic equation to find the range of values for which the distance moving is greater than the distance
