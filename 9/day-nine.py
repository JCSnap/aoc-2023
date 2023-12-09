
with open("day-nine.in", "r") as f:
    total_one = 0
    total_two = 0
    for line in f:
        sequence = line.strip()
        numbers = sequence.split(' ')
    
        numbers_original = [int(num) for num in numbers]
        numbers = numbers_original.copy()

        # Part 1
        last_nums = []
        all_zeros = False
        while not all_zeros:
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
        total_one += sum(last_nums)

        # Part 2
        numbers = numbers_original.copy()
        first_nums = []
        all_zeros = False
        while not all_zeros:
            print(numbers)
            all_zeros = True
            new_nums = []
            for i, num in enumerate(numbers):
                if i == 0:
                    first_nums.append(num)
                if i > 0:
                    new_num = numbers[i] - numbers[i-1]
                    all_zeros = all_zeros and new_num == 0
                    new_nums.append(new_num)
            numbers = new_nums
        
        last = 0
        for num in first_nums[::-1]:
            last = num - last
        total_two += last

    print("Part 1:", total_one)
    print("Part 2:", total_two)
