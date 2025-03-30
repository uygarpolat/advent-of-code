def evaluate(numbers, operators):
    import math
    result = numbers[1]
    for i in range(len(numbers) - 2):
        if operators[i] == "+":
            result += numbers[i+2]
        elif operators[i] == "*":
            result *= numbers[i+2]
        elif operators[i] == '|':
            num_digits = len(str(numbers[i+2]))
            result = result * (10 ** num_digits) + numbers[i+2]
        if result > numbers[0]:
           return result
    return result

def main():

    from itertools import product
    store = ["+*", "+*|"]
    for i in range(2):
        ops = store[i]
        result = 0
        with open("input.txt", 'r') as file:
            for line in file:
                input = line.split(":")

                numbers = [int(input[0])]
                numbers.extend(map(int, input[1].split()))
                operator_combinations = list(product(ops, repeat=len(numbers) - 2))

                for operators in operator_combinations:
                    eval = evaluate(numbers, operators)

                    if eval == numbers[0]:
                        result += eval
                        break
            print(f"Part {i+1} solution is {result}")

if __name__ == "__main__":
    main()