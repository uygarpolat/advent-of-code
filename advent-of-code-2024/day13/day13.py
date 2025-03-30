from math import lcm

def calculate_cost(button_a, button_b, prize, extra):
    prize = (prize[0] + extra, prize[1] + extra)
    lcm_of_b = lcm(button_b[0], button_b[1])
    multiplier_of_a0 = int(lcm_of_b / button_b[0])
    multiplier_of_a1 = int(lcm_of_b / button_b[1])
    a_compound = multiplier_of_a0 * button_a[0] - multiplier_of_a1 * button_a[1]
    press_a = (prize[0] * multiplier_of_a0 - prize[1] * multiplier_of_a1) / a_compound
    press_b = (prize[0] - (button_a[0] * press_a)) / button_b[0]

    if press_a % 1 != 0 or press_b % 1 != 0:
        return 0
    else:
        return int(press_a * 3 + press_b)

def parse_file(file_path):
    from collections import defaultdict

    machines = defaultdict(list)
    with open(file_path, 'r') as file:
        for line_count, line in enumerate(file):
            if line_count % 4 < 2:
                x_plus, y_plus = line.lstrip("ButtonAB: ").split(',')
                x_value = int(x_plus.lstrip("X+ "))
                y_value = int(y_plus.lstrip("Y+ "))
                data = (x_value, y_value)
            elif line_count % 4 == 2:
                x_prize_plus, y_prize_plus = line.lstrip("Prize: ").split(',')
                x_prize_value = int(x_prize_plus.lstrip("X= "))
                y_prize_value = int(y_prize_plus.lstrip("Y= "))
                data = (x_prize_value, y_prize_value)
            else:
                continue
            machines[line_count // 4].append(data)
    return machines

def main():
    file_path = "input.txt"
    machines = parse_file(file_path)
    extra = 10000000000000
    for i in range(0, extra + 1, extra):
        total_cost = 0
        for _, values in machines.items():
            button_a, button_b, prize = values
            single_cost = calculate_cost(button_a, button_b, prize, i)
            total_cost += single_cost
        print(f"Solution for Part {i // extra + 1}: {total_cost}")

if __name__ == "__main__":
    main()