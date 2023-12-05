import re

seeds = []

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

min = float('inf')

for seed in seeds:
    cur_location = seed
    for map in all_maps:
        for tuple in map:
            destination, source, length = tuple
            if source <= cur_location < source + length:
                cur_location = cur_location - source + destination
                break
        if map == humidity_to_location:
            if cur_location < min:
                min = cur_location

print(min)