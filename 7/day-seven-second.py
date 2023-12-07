hands = []
hand_to_bid_map = {}

ranks = "AKQT98765432J"

def replace(char, hand):
    # remove all Js from hand
    temp = hand.replace("J", "")
    if temp == "":
        return hand
    # get the char with the max frequency in one line
    max_char = max(set(temp), key=temp.count)
    # replace all instances of "J" with max_char
    hand = hand.replace(char, max_char)
    return hand

def weaker_than_pivot(hand, pivot):
    if hand == pivot:
        return False
    hand_original = hand
    pivot_original = pivot
    # count the number of distinct cards in hand
    hand_set = set(hand)
    pivot_set = set(pivot)
    if "J" in hand_set:
        # replace J in the hand set with the character with the max frequency
        hand = replace("J", hand)
        hand_set = set(hand)
    if "J" in pivot_set:
        pivot = replace("J", pivot)
        pivot_set = set(pivot)
    hand_count = len(hand_set)
    pivot_count = len(pivot_set)
    if hand_count > pivot_count:
        return True
    elif hand_count < pivot_count:
        return False
    else:
        max_hand_count = max([hand.count(card) for card in set(hand)])
        max_pivot_count = max([pivot.count(card) for card in set(pivot)])
        if max_hand_count != max_pivot_count:
            return max_hand_count < max_pivot_count
        else:
            for i in range(len(hand)):
                if ranks.index(hand_original[i]) == ranks.index(pivot_original[i]):
                    continue
                return ranks.index(hand_original[i]) > ranks.index(pivot_original[i])
            return False

def partition(hands, low, high):
    pivot = hands[high]
    i = low - 1
    for j in range(low, high):
        if weaker_than_pivot(hands[j], pivot):
            i += 1
            hands[i], hands[j] = hands[j], hands[i]
    hands[i + 1], hands[high] = hands[high], hands[i + 1]
    return i + 1

def quicksort(hands, low, high):
    if low >= high:
        return
    p = partition(hands, low, high)
    quicksort(hands, low, p - 1)
    quicksort(hands, p + 1, high)

with open("day-seven.in", "r") as f:
    lines = f.read().strip().split('\n')
    parts = [line.split() for line in lines]
    for part in parts:
        hands.append(part[0])
        hand_to_bid_map[part[0]] = part[1]
    
    quicksort(hands, 0, len(hands) - 1)
    total = 0
    # enumerate hands with index
    print("rank hand bid")
    for i, hand in enumerate(hands):
        rank = i + 1
        bid = int(hand_to_bid_map[hand])
        print(f"{rank} {hand} {bid}")
        total += rank * bid
    
    print("Part 2:", total)

# 250384185
