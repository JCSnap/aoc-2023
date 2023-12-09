
with open("day-nine.in", "r") as f:
    total = 0
    for line in f:
        sequence = line.strip()
        numbers = sequence.split(' ')
        print(numbers)
    
        numbers = [int(num) for num in numbers]
        last_nums = []
        all_zeros = False
        while not all_zeros:
            print(numbers)
            all_zeros = True
            new_nums = []
            for i, num in enumerate(numbers):
                if i == len(numbers) - 1:
                    last_nums.append(num)
                if i > 0:
                    new_num = numbers[i] - numbers[i-1]
                    all_zeros = all_zeros and new_num == 0
                    new_nums.append(new_num)
            numbers = new_nums
        # sum up everything in last_nums
        print(last_nums)
        total += sum(last_nums)

    print("Part 1:", total)

    # 939801360 too low