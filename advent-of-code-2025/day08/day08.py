def main():
    filepath = "input.txt"
    limit = 1000 if filepath == "input.txt" else 10

    boxes = []
    with open(filepath, "r") as f:
        for line in f:
            boxes.append(tuple(int(l) for l in line.strip().split(",")))

    edges = []
    num_points = len(boxes)

    for i in range(num_points):
        for j in range(i + 1, num_points):
            p1 = boxes[i]
            p2 = boxes[j]
            dist_sq = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2
            edges.append((dist_sq, i, j))

    edges.sort()

    parent = list(range(num_points))
    size = [1] * num_points
    num_components = num_points

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)

        if root_i != root_j:
            size[root_i] += size[root_j]
            size[root_j] = 0
            parent[root_j] = root_i
            return True
        return False

    count = 0
    for _, u, v in edges:
        if count == limit:
            sorted_sizes = sorted(size, reverse=True)
            result1 = sorted_sizes[0] * sorted_sizes[1] * sorted_sizes[2]
            print(f"Solution for Part 1: {result1}")

        count += 1

        if union(u, v):
            num_components -= 1
            if num_components == 1:
                result2 = boxes[u][0] * boxes[v][0]
                print(f"Solution for Part 2: {result2}")
                break


if __name__ == "__main__":
    main()
