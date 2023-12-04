import re

total = 0

def extract_number(line):
    match = re.search(r"Card\s+(\d+):", line)
    if match:
        return int(match.group(1))
    else:
        return None
    
cards = [1] * 223

with open("day-four.in") as f:
    for line in f:
        number = extract_number(line)
        index = number - 1
        winning_numbers, hand_numbers = line[line.find(":") + 1:].split('|')
        winning_numbers = [int(num) for num in winning_numbers.split() if num.isdigit()]
        hand_numbers = [int(num) for num in hand_numbers.split() if num.isdigit()]
        copies = cards[index]
        count = 0
        for num in winning_numbers:
            if num in hand_numbers:
                count += 1
        for i in range(index + 1, index + count + 1, 1):
            cards[i] += 1 * (copies)
    for i in range(len(cards)):
        total += cards[i]

print(total)