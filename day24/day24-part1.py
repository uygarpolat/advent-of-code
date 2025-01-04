from itertools import combinations

def main():
    info = {}
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        for line in file:
            tally = []
            left, right = line.strip().split('@')
            tally.extend([int(x.strip()) for x in left.strip().split(',')])
            tally.extend([int(x.strip()) for x in right.strip().split(',')])
            info[len(info)] = tally

    length = len(info)
    count = 0
    minimum = 200000000000000
    maximum = 400000000000000
    pairs = list(combinations(range(0, length), 2))
    for pair in pairs:
        x, y, past_or_future = calculate_intersection(info, pair[0], pair[1])
        
        if past_or_future and x != None and y != None and x >= minimum and x<=maximum and y >= minimum and y <=maximum:
            count += 1
    print(f"Solution for Part 1: {count}")

def calculate_intersection(info, index1, index2):

    x1 = info[index1][0]
    y1 = info[index1][1]
    m1_x = info[index1][3]
    m1_y = info[index1][4]
    m1 = m1_y / m1_x

    x2 = info[index2][0]
    y2 = info[index2][1]
    m2_x = info[index2][3]
    m2_y = info[index2][4]
    m2 = m2_y / m2_x

    if m1 == m2:
        return None, None, False

    x = (m1*x1 - y1 - m2*x2 + y2)/(m1 - m2)
    y = m1 * ((m1*x1 - y1 - m2*x2 + y2)/(m1 - m2)) - m1*x1 + y1

    return x, y, past_or_future(info, index1, index2, x, y)

def past_or_future(info, index1, index2, x, y):

    x1 = info[index1][0]
    m1_x = info[index1][3]
    m1_y = info[index1][4]

    x2 = info[index2][0]
    m2_x = info[index2][3]
    m2_y = info[index2][4]

    res1 = False
    res2 = False

    if m1_x > 0:
        if x >= x1:
            res1 = True
    else:
        if x <= x1:
            res1 = True

    if m2_x > 0:
        if x >= x2:
            res2 = True
    else:
        if x <= x2:
            res2 = True

    return res1 and res2

if __name__ == "__main__":
    main()