from math import gcd

with open("day-eight.in", "r") as f:
    lines = f.read().strip().split('\n\n')
    sequence = lines[0]
    nodes = lines[1].split('\n')
    left_dict = {}
    right_dict = {}
    for node in nodes:
        name = node[0:3]
        left_child = node[7:10]
        right_child = node[12:15]
        left_dict[name] = left_child
        right_dict[name] = right_child

    START = "AAA"
    TARGET = "ZZZ"
    cur_name = START
    count = 0
    seq_len = len(sequence)
    cur_pos = 0
    while cur_name != TARGET:
        # loop the sequence
        if cur_pos >= seq_len:
            cur_pos = 0
        cur_char = sequence[cur_pos]
        if cur_char == "L":
            cur_name = left_dict[cur_name]
        else:
            cur_name = right_dict[cur_name]
        cur_pos += 1
        count += 1

    print("Part 1:", count)

    # Part 2
    starts = []
    # append all the nodes that ends with A into starts
    for name in left_dict:
        end = name[-1]
        if end == "A":
            starts.append(name)
    
    counts = []
    for start in starts:
        count = 0
        cur_name = start
        cur_pos = 0
        while True:
            if cur_pos >= seq_len:
                cur_pos = 0
            count += 1
            cur_char = sequence[cur_pos]
            if cur_char == "L":
                cur_name = left_dict[cur_name]
            else:
                cur_name = right_dict[cur_name]
            cur_pos += 1
            if cur_name[-1] == "Z":
                break
        counts.append(count)

    k = 1
    for i in counts:
        k = k * i // gcd(k, i)
    print("Part 2:", k)
        