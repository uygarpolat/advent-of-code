def part_one(nb):
    i = 0
    while(i < len(nb)):
        if nb[i] == '.':
            nb[i] = nb[len(nb) - 1]
            nb.pop(len(nb) - 1)
            while (nb[len(nb) - 1] == '.'):
                nb.pop(len(nb) - 1)
        i += 1
    # for i in nb:
    #     print(i, end="")
    # print("")
    sum = 0
    for i, c in enumerate(nb):
        sum += i * int(c)
    print(sum)

def last_elem_count(nb, target_elem):
    j = len(nb) - 1
    while(j >= 0):
        if nb[j] != target_elem:
            j -= 1
            continue
        else:
            break
    print(f"j is {j} and len(nb) is {len(nb)}")
    n = 0
    for i in range(j, -1, -1):
        if nb[i] == target_elem:
            n += 1
        else:
            break
    # print(f"n is {n}")
    return n, nb[:-n - (len(nb) - 1 - i - 1)]

def dot_count(nb, k):
    while (k < len(nb)):
        if nb[k] != '.':
            k += 1
            continue
        else:
            break
    n = 0
    for i in range(k, len(nb)):
        if nb[i] == nb[k]:
            n += 1
        else:
            break
    return n+k, n

def part_two(nb):
    i = 0
    target = nb[len(nb) - 1]
    test = 0
    # while (target >= 0):
    while(test < 2):
        i, d = dot_count(nb, i) # index of the next first non-dot. and the dot count
        e, nb_temp = last_elem_count(nb, target)
        print(f"i and d: {i} and {d}. And e: {e}")

        if (d < e):
            target -= 1
            continue
        for k in range(e):
            nb_temp[i - d + k] = target
        nb = nb_temp
        target -= 1
        print(d)
        print(e)
        print(nb)
        test += 1

def main():
    import copy

    file_path = "input2.txt"
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
        print(nb)

        nb1 = copy.deepcopy(nb)
        part_one(nb)
        part_two(nb1)

if __name__ == "__main__":
    main()