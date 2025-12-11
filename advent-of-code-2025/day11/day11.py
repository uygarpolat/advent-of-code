def main():
    filepath = "input.txt"
    book = {}
    dp1 = {}
    dp2 = {}

    with open(filepath, "r") as f:
        for line in f:
            key, val = line.strip().split(":")
            book[key] = val.strip().split()

    def dfs1(curr):
        if curr == "out":
            return 1

        if curr in dp1:
            return dp1[curr]

        local_result = 0
        for nxt in book[curr]:
            dp1[nxt] = dfs1(nxt)
            local_result += dp1[nxt]
        return local_result

    def dfs2(curr, fft, dac):
        if curr == "out":
            if not dac or not fft:
                return 0
            return 1

        if (curr, fft, dac) in dp2:
            return dp2[(curr, fft, dac)]

        if curr == "dac":
            dac = True
        if curr == "fft":
            fft = True

        local_result = 0
        for nxt in book[curr]:
            dp2[(nxt, fft, dac)] = dfs2(nxt, fft, dac)
            local_result += dp2[(nxt, fft, dac)]
        return local_result

    print(f"Solution for Part 1: {dfs1('you')}")
    print(f"Solution for Part 2: {dfs2('svr', False, False)}")


if __name__ == "__main__":
    main()
