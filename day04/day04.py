def main():
    filepath = "input.txt"
    result1 = 0
    result2 = 0
    with open(filepath, 'r') as file:
        for line in file:
            workload = [int(x) for x in line.replace("-", " ").replace(",", " ").split()]
            res1, res2 = is_it_overlapping(workload)
            result1 += res1
            result2 += res2
    print(f"Solution for Part 1: {result1}")
    print(f"Solution for Part 2: {result2}")

def is_it_overlapping(workload):
    res1 = 0
    res2 = 0
    new_workload = [x - min(workload[0], workload[2]) for x in workload]
    if new_workload[0] == 0:
        if new_workload[3] <= new_workload[1]:
            res1 = 1
        if new_workload[1] >= new_workload[2]:
            res2 = 1
    if new_workload[2] == 0:
        if new_workload[3] >= new_workload[1]:
            res1 = 1
        if new_workload[3] >= new_workload[0]:
            res2 = 1
    return res1, res2

if __name__ == "__main__":
    main()