hands = []
hand_to_bid_map = {}

# rank the hands from A to 2
ranks = "AKQJT98765432"
def weaker_than_pivot(hand, pivot):
    if hand == pivot:
        return False
    # count the number of distinct cards in hand
    hand_count = len(set(hand))
    pivot_count = len(set(pivot))
    if hand_count > pivot_count:
        return True
    elif hand_count < pivot_count:
        return False
    else:
        # when the number of distinct cards is the same, either:
        # 1. they have the same class
        # 2. four of a kind and full house
        # 3. three of a kind and two pair
        # return true if the max count of set(pivot) is greater than the max count of set(hand)
        max_hand_count = max([hand.count(card) for card in set(hand)])
        max_pivot_count = max([pivot.count(card) for card in set(pivot)])
        if max_hand_count != max_pivot_count:
            return max_hand_count < max_pivot_count
        else:
            # same class, start comparing from first card, rank is A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2
            for i in range(len(hand)):
                if ranks.index(hand[i]) == ranks.index(pivot[i]):
                    continue
                return ranks.index(hand[i]) > ranks.index(pivot[i])
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
    
    print("Part 1:", total)

# 87929769 too low