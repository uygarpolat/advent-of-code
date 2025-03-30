def calculate_total(matches):
    counter = 0
    for x in matches:
        num1, num2 = map(int, x.removeprefix("mul(").removesuffix(")").split(","))
        counter = counter + num1 * num2
    return counter

def main():
    import re

    with open("input.txt", "r") as file:
        content = file.read()
        matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", content)
        matches_with_enabler = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", content)
        matches_with_enabler_removed = []
        flag = 0
        for y in matches_with_enabler:
            if (y != "don't()"):
                if (flag == 0 and y != "do()"):
                    matches_with_enabler_removed.append(y)
                elif (y == "do()"):
                    flag = 0
            else:
                flag = 1

    print(f"Solution without enabler is {calculate_total(matches)}")
    print(f"Solution with enabler is {calculate_total(matches_with_enabler_removed)}")

if __name__ == "__main__":
    main()