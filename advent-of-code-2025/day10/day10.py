from collections import deque
import numpy as np
from scipy.optimize import linprog


def bits_from_indices(indices):
    mask = 0
    for idx in indices:
        mask |= 1 << idx
    return mask


def parse_file(filepath) -> list[tuple[int, list[int], list[int]]]:

    manual = []
    with open(filepath, "r") as f:
        for line in f:

            onetwo, three = line.strip("\n[}").split("{")
            one, two = onetwo.split("]")

            target_mask = bits_from_indices(
                idx for idx, char in enumerate(one) if char == "#"
            )

            buttons_raw = two.strip().replace("(", "").replace(")", "").split()

            joltage = tuple(map(int, three.split(",")))

            button_masks = [
                bits_from_indices(map(int, t.split(","))) for t in buttons_raw
            ]

            buttons = [tuple(map(int, t.split(","))) for t in buttons_raw]

            manual.append((target_mask, [button_masks, buttons], joltage))
    return manual


def min_presses_part1(target, buttons):

    q = deque([(0, 0)])
    visited = {0}

    while q:
        state, steps = q.popleft()
        for button in buttons:
            nxt = state ^ button
            if nxt == target:
                return steps + 1
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, steps + 1))


def min_presses_part2(jolts, button_indices) -> int:
    width = len(jolts)
    cols = []
    for idxs in button_indices:
        col = np.zeros(width, dtype=float)
        for idx in idxs:
            if 0 <= idx < width:
                col[idx] += 1.0
        cols.append(col)

    A_eq = np.column_stack(cols)
    b_eq = np.array(jolts, dtype=float)
    c = np.ones(A_eq.shape[1], dtype=float)
    integrality = np.ones_like(c)

    res = linprog(
        c,
        A_eq=A_eq,
        b_eq=b_eq,
        integrality=integrality,
    )

    return int(round(res.fun))


def main() -> None:
    filepath = "input.txt"
    manual = parse_file(filepath)

    result1 = 0
    result2 = 0
    for target, (button_masks, button_tuples), jolts in manual:
        result1 += min_presses_part1(target, button_masks)
        result2 += min_presses_part2(jolts, button_tuples)

    print(f"Solution for Part 1: {result1}")
    print(f"Solution for Part 2: {result2}")


if __name__ == "__main__":
    main()
