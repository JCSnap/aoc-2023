import re

seeds = []
expanded_seeds = []

current_section = None

seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

all_maps = [
    seed_to_soil,
    soil_to_fertilizer,
    fertilizer_to_water,
    water_to_light,
    light_to_temperature,
    temperature_to_humidity,
    humidity_to_location
]

with open("day-five.in", 'r') as f:
    pattern = r"seeds:\s*((?:\d+\s*)+)"
    for line in f:
        match = re.search(pattern, line)
        if match:
            seeds = [int(num) for num in match.group(1).split()]
            break

expanded_seeds = [(seeds[2 * i], seeds[2 * i + 1]) for i in range(len(seeds) // 2)]

print("Finished parsing seeds")

sections = {
    "seed-to-soil map:": seed_to_soil,
    "soil-to-fertilizer map:": soil_to_fertilizer,
    "fertilizer-to-water map:": fertilizer_to_water,
    "water-to-light map:": water_to_light,
    "light-to-temperature map:": light_to_temperature,
    "temperature-to-humidity map:": temperature_to_humidity,
    "humidity-to-location map:": humidity_to_location
}

with open("day-five.in", 'r') as file:
    for line in file:
        line = line.strip()
        if line in sections:
            current_section = sections[line]
        elif current_section is not None and line:
            numbers = tuple(map(int, line.split()))
            current_section.append(numbers)

cur_location = 0
has_not_found_min = True
while has_not_found_min:
    temp = cur_location
    # iterate maps in reverse order
    for map in reversed(all_maps):
        for tuple in map:
            destination, source, length = tuple
            # find source from destination
            if destination <= temp < destination + length:
                temp = temp - destination + source
                break
    
    for seed, length in expanded_seeds:
        if seed <= temp < seed + length:
            has_not_found_min = False
            break
    
    if has_not_found_min:
        print(f"cur_location: {cur_location}")
        cur_location += 1

print(cur_location)
# 17729182
