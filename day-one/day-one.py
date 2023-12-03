total = 0

with open('day-one.in') as f:
    # for each word in the file
    for line in f:
        # iterate from the front to find the first digit
        for i in range(len(line)):
            if line[i].isdigit():
                first = i
                break

        # iterate from the back to find the last digit
        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                last = i
                break

        # combine the digits into a number
        combined = line[first] + line[last]
        
        # add the number to the total
        total += int(combined)

print(total)