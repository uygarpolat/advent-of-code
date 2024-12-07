def parse_file(file_path, file):
    seeds = []
    local = []
    general = []
    in_first_section = True

    for line in file:
        line = line.strip()

        if line == "":
            in_first_section = False
            continue
        
        if in_first_section:
            parts = line.split(':')
            seeds = list(map(int, parts[1].split()))
        else:
            if not line[0].isdigit():
                if local:
                    general.append(local)
                    local = []
                continue
            numbers = list(map(int, line.split()))
            local.append(numbers)
    if local:
        general.append(local)
    
    return seeds, general

def lowest_location(seed, maps):
    payload = seed
    for x in range(len(maps)):
        for y in range(len(maps[x])):
            if (payload >= maps[x][y][1] and payload < maps[x][y][1] + maps[x][y][2]):
                payload = maps[x][y][0] + (payload - maps[x][y][1])
                break
    return payload

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        seeds, maps = parse_file(file_path, file)
        lowest_loc = 100000000000
        for seed in seeds:
            seed_loc = lowest_location(seed, maps)
            if lowest_loc > seed_loc:
                lowest_loc = seed_loc
        print(lowest_loc)

        lowest_loc = 100000000000
        for i, seed in enumerate(seeds):
            if (i % 2 != 0):
                continue
            else:
                for j in range(seeds[i + 1]):
                    seed_loc = lowest_location(seed + j, maps)
                    if lowest_loc > seed_loc:
                        lowest_loc = seed_loc
            print(f"Seed {i + 1} is done")
        print(lowest_loc)

if __name__ == "__main__":
    main()