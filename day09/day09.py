def part_one(nb):
    i = 0
    while(i < len(nb)):
        if nb[i] == '.':
            nb[i] = nb[len(nb) - 1]
            nb.pop(len(nb) - 1)
            while (nb[len(nb) - 1] == '.'):
                nb.pop(len(nb) - 1)
        i += 1

    sum = 0
    for i, c in enumerate(nb):
        sum += i * int(c)
    print(f"Solution for Part 1: {sum}")

def get_target_info(nb, target_elem):
    j = len(nb) - 1
    while(j >= 0):
        if nb[j] != target_elem:
            j -= 1
            continue
        else:
            break

    n = 0
    for i in range(j, -1, -1):
        if nb[i] == target_elem:
            n += 1
        else:
            break
    d = len(nb)-1 - (n + len(nb)-1-j) + 1
    return d, n

def part_two(nb):
    print("Processong Part 2...")
    target = nb[len(nb) - 1]
    
    while(target >= 0):
        if target % 1000 == 0:
            print(f"{int(100 - target / 100)}% is processed.")
        target_start, target_length = get_target_info(nb, target)

        m = 0
        count = 0
        while(m < target_start):
            if nb[m] == '.':
                count += 1
            else:
                count = 0
            if count == target_length:
                break
            m += 1
        if count != target_length:
            target -= 1
            continue

        for i in range(target_length):
            nb[i + m - count + 1] = target
            nb[i + target_start] = '.'
        target -= 1

    sum = 0
    for i, c in enumerate(nb):
        if c == '.':
            continue
        sum += i * int(c)
    print(f"Solution for Part 1: {sum}")

def main():
    import copy

    file_path = "input.txt"
    with open(file_path, 'r') as file:
        num = file.read()
        number = []
        for c in num:
            number.append(int(c))
        nb = []

        for i in range(len(number)):
            if i % 2 == 0:
                for j in range(number[i]):
                    nb.append(int(i/2))
            else:
                for j in range(number[i]):
                    nb.append('.')

        nb1 = copy.deepcopy(nb)
        part_one(nb)
        part_two(nb1)

if __name__ == "__main__":
    main()