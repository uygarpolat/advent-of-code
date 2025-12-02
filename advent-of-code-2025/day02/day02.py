def generateTwiceRepeat(num: int) -> int:
    return num * (10 ** len(str(num))) + num


def generateNthRepeat(
    num: int,
    start: int,
    end: int,
    seen: set,
) -> int:
    local_res = 0
    multiplier = 10 ** len(str(num))
    local_num = num * multiplier + num

    while local_num <= end:
        if start <= local_num and local_num not in seen:
            local_res += local_num
            seen.add(local_num)
        local_num = local_num * multiplier + num

    return local_res


def main() -> tuple[int, int]:
    result1 = 0
    result2 = 0

    with open("input.txt", "r") as file:
        for rng in file.read().split(","):
            start_str, end_str = rng.split("-")
            start_num = int(start_str)
            end_num = int(end_str)

            first = start_num // (10 ** ((len(start_str) + 1) // 2))

            while (local_res := generateTwiceRepeat(first)) <= end_num:
                if local_res >= start_num:
                    result1 += local_res
                first += 1

            seen = set()
            for i in range(1, first):
                result2 += generateNthRepeat(
                    i,
                    start_num,
                    end_num,
                    seen,
                )

    print(f"Solution for Part 1: {result1}")
    print(f"Solution for Part 2: {result2}")


if __name__ == "__main__":
    main()
