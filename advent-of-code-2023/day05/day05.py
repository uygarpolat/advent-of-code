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
                    local.sort(key=lambda x: x[1])
                    general.append(local)
                    local = []
                continue
            numbers = list(map(int, line.split()))
            local.append(numbers)
    if local:
        local.sort(key=lambda x: x[1])
        general.append(local)
    
    return seeds, general

def get_mapped_range(start, length, ranges):
    results = []
    end = start + length
    current = start
    
    for dest_start, src_start, range_len in ranges:
        src_end = src_start + range_len
        
        if current >= src_end:
            continue
            
        if current < src_start:
            gap_end = min(src_start, end)
            results.append((current, gap_end - current))
            current = gap_end
            
        if current >= end:
            break
            
        if current >= src_start:
            overlap_end = min(src_end, end)
            mapped_start = dest_start + (current - src_start)
            results.append((mapped_start, overlap_end - current))
            current = overlap_end
            
        if current >= end:
            break
    
    if current < end:
        results.append((current, end - current))
        
    return results

def process_ranges(ranges, maps):
    current_ranges = ranges
    
    for map_ranges in maps:
        next_ranges = []
        for start, length in current_ranges:
            mapped = get_mapped_range(start, length, map_ranges)
            next_ranges.extend(mapped)
        current_ranges = next_ranges
        
    return min(start for start, _ in current_ranges)

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        seeds, maps = parse_file(file_path, file)
        
        seed_ranges = [(seed, 1) for seed in seeds]
        lowest_loc = process_ranges(seed_ranges, maps)
        print(f"Solution for part 1: {lowest_loc}")

        seed_ranges = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
        lowest_loc = process_ranges(seed_ranges, maps)
        print(f"Solution for part 2: {lowest_loc}")

if __name__ == "__main__":
    main()