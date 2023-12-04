import re

total = 0

def extract_number(line):
    match = re.search(r"Card\s+(\d+):", line)
    if match:
        return int(match.group(1))
    else:
        return None
    
with open("day-four.in") as f:
    for line in f:
        number = extract_number(line)
        winning_numbers, hand_numbers = line[line.find(":") + 1:].split('|')
        winning_numbers = [int(num) for num in winning_numbers.split() if num.isdigit()]
        hand_numbers = [int(num) for num in hand_numbers.split() if num.isdigit()]
        # count the number of matches in winning_numbers that are also in hand_numbers
        count = 0
        for num in winning_numbers:
            if num in hand_numbers:
                count += 1
        # point is two to the power of count
        point = 0 if count == 0 else 2 ** (count - 1)
        total += point

print(total)