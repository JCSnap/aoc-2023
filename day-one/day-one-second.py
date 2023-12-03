total = 0

valid_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]

string_to_int = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0"
}

max_len = max(len(word) for word in valid_digits)
with open('day-one.in') as f:
    # for each word in the file
    for line in f:
        found_first = False
        found_last = False
        for i in range(len(line)):
            if found_first:
                break
            if line[i].isdigit():
                first = line[i]
                found_first = True
            for j in range(3, max_len + 1):
                if i + j <= len(line):
                    substring = line[i:i + j]
                    if substring in valid_digits:
                        digit = string_to_int[substring]
                        first = digit
                        found_first = True


        for i in range(len(line) - 1, -1, -1):
            if found_last:
                break
            if line[i].isdigit():
                last = line[i]
                found_last = True
            for j in range(3, max_len + 1):
                if i + j <= len(line):
                    substring = line[i:i + j]
                    if substring in valid_digits:
                        digit = string_to_int[substring]
                        last = digit
                        found_last = True
    
        combined = first + last
        total += int(combined)

print(total)