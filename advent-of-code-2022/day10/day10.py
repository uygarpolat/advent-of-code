def main():
    filepath = "input2.txt"
    instructions = []
    with open(filepath, "r") as f:
        for line in f:
            instructions.append(line.strip().split())

    x = 1
    cycle = 0
    signal_sum = 0
    crt = []

    def tick():
        nonlocal cycle, signal_sum
        cycle += 1
        col = (cycle - 1) % 40
        crt.append("#" if abs(col - x) <= 1 else ".")
        if cycle in (20, 60, 100, 140, 180, 220):
            signal_sum += cycle * x

    for inst in instructions:
        if inst[0] == "noop":
            tick()
        else:
            tick()
            tick()
            x += int(inst[1])

    print(f"Solution for Part 1: {signal_sum}")

    for i, c in enumerate(crt):
        print(c, end="")
        if (i + 1) % 40 == 0:
            print()


if __name__ == "__main__":
    main()
