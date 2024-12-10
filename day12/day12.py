def main():
    file_path = "input2.txt"
    with open(file_path, 'r') as file:
        for line in file:
            part1, part2 = line.split()
            nums = list(map(int, part2.split(",")))
            print(nums)


if __name__ == "__main__":
    main()