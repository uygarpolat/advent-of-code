def main():
    filepath = "input.txt"
    tiles = []
    with open(filepath, "r") as f:
        for line in f:
            x, y = line.strip().split(",")
            tiles.append((int(x), int(y)))

    n = len(tiles)

    poly_edges = []
    for k in range(n):
        poly_edges.append((tiles[k], tiles[(k + 1) % n]))

    def validate_rectangle(x1, y1, x2, y2):
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        for (px1, py1), (px2, py2) in poly_edges:
            if px1 == px2:
                if min_x < px1 < max_x:
                    edge_y_min, edge_y_max = min(py1, py2), max(py1, py2)
                    overlap_start = max(edge_y_min, min_y)
                    overlap_end = min(edge_y_max, max_y)
                    if overlap_start < overlap_end:
                        return False
            else:
                if min_y < py1 < max_y:
                    edge_x_min, edge_x_max = min(px1, px2), max(px1, px2)
                    overlap_start = max(edge_x_min, min_x)
                    overlap_end = min(edge_x_max, max_x)
                    if overlap_start < overlap_end:
                        return False

        return True

    result1 = 0
    result2 = 0

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]

            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            result1 = max(result1, area)

            if area > result2 and validate_rectangle(x1, y1, x2, y2):
                result2 = area

    print(f"Solution for Part 1: {result1}")
    print(f"Solution for Part 2: {result2}")


if __name__ == "__main__":
    main()
