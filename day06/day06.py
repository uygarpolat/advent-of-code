# Time:        42     68     69     85
# Distance:   284   1005   1122   1341

# Time:      71530
# Distance:  940200

import math

# Slow, iterative method. Not used.
def method_one(store):
    total = 1
    for i in range(len(store)):
        count = 0
        for j in range(int(store[i][0])):
            if (j * (store[i][0] - j) > store[i][1]):
                count += 1
        total *= count
    return total

def beat_record(store):
    total = 1
    for i in range(len(store)):
        count = 0
        if store[i][0] % 2 != 0:
            target = round(math.sqrt(((store[i][0] - 1) / 2) * ((store[i][0] + 1) / 2) - store[i][1]))
            sum = target * 2
        else:
            target = round(math.sqrt((store[i][0] / 2) ** 2 - store[i][1]) - 0.5)
            sum = target * 2 + 1
        total *= sum
    return total

def main():
    total = 1
    store = [[42, 284], [68, 1005], [69,1122], [85,1341]]
    store2 = [[42686985, 284100511221341]]
    total = beat_record(store)
    print(f"Solution for part 1: {total}")
    total = beat_record(store2)
    print(f"Solution for part 2: {total}")

if __name__ == "__main__":
    main()