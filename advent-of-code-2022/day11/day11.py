from operator import mul, add, floordiv, pow
from math import prod
import copy


def parse_file(filepath):
    with open(filepath, "r") as f:
        ledger = f.read()
    monkeys = ledger.split("\n\n")
    lookup = [
        "",
        "  Starting items: ",
        "  Operation: new = old ",
        "  Test: divisible by ",
        "    If true: throw to monkey ",
        "    If false: throw to monkey ",
    ]
    ops = {"*": mul, "+": add}
    relief_coefficient = 3
    records = []
    for monkey in monkeys:
        bucket = []
        for j, m in enumerate(monkey.split("\n")[1:], start=1):
            m = m[len(lookup[j]) :]
            if j == 1:
                payload = list(map(int, m.split(",")))
            elif j == 2:
                op, m = m.split()
                op = ops[op]
                if m == "old":
                    op = pow
                    m = 2
                m = int(m)
                payload = [[op, m], [floordiv, relief_coefficient]]
            else:
                payload = int(m)
            bucket.append(payload)
        records.append(bucket)
    return records


def execute(records, idx, iter, mod=None):
    record = records[idx]
    res = iter
    for op, num in record[1]:
        res = op(res, num)
    if mod is not None:
        res %= mod
    if not res % record[2]:
        target = record[3]
    else:
        target = record[4]
    return target, res


def main():
    filepath = "input.txt"
    records_permanent = parse_file(filepath)
    n = len(records_permanent)
    modulus = prod(record[2] for record in records_permanent)
    rounds_range = [20, 10000]

    for idx, rounds in enumerate(rounds_range, start=1):
        records = copy.deepcopy(records_permanent)
        monkey_business = [0] * len(records)
        mod = None
        if idx == 2:
            mod = modulus
            for j in range(n):
                records[j][1][1][1] = 1
        for round in range(rounds):
            for i in range(n):
                iters = records[i][0]
                for iter in iters:
                    target, res = execute(records, i, iter, mod)
                    records[target][0].append(res)
                monkey_business[i] += len(iters)
                records[i][0] = []
        monkey_business.sort(reverse=True)
        print(f"Result for Part {idx}: {monkey_business[0] * monkey_business[1]}")


if __name__ == "__main__":
    main()
