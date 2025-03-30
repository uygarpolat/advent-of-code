def main():
    file_path = "input.txt"
    local_total = 0
    highest = 0
    top_three = [0, 0, 0]
    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip():
                for i in range(3):
                    if top_three[i] < local_total:
                        top_three.insert(i, local_total)
                        break
                local_total = 0
            else:
                local_total += int(line.strip())

    print(f"Solution for Part 1: {top_three[0]}")
    print(f"Solution for Part 2: {sum(top_three[:3])}")

if __name__ == "__main__":
    main()