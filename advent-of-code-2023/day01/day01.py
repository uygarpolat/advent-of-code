
words_to_numbers = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def is_num_or_strnum(line, reverse=False):
    buffer = ""
    if reverse:
        line = line[::-1]
    
    for char in line:
        if char.isdigit():
            return int(char)
        buffer += char
        for word, number in words_to_numbers.items():
            if (word[::-1] if reverse else word) in buffer:
                return number
    return 0

def main():

    num = 0

    with open("input.txt", "r") as file:
        for line in file:
            for char in line:
                if char.isdigit():
                    num += int(char) * 10
                    break
            for char in reversed(line):
                if char.isdigit():
                    num += int(char)
                    break
        print(f"Calibration values are {num}")
        file.seek(0)
        num = 0
        for line in file:
            num += is_num_or_strnum(line) * 10
            num += is_num_or_strnum(line, True)
            continue
        print(f"Calibration values are {num}")

if __name__ == "__main__":
    main()
