import collections as C

def main():

    file_path = "input.txt"
    graph = C.defaultdict(set)
    with open(file_path) as file:
        for line in file:
            node, *neighbors = line.replace(':', '').split()
            for neighbor in neighbors:
                graph[node].add(neighbor)
                graph[neighbor].add(node)

    nodes_set = set(graph)

    def count_neighbors_not_in_set(node):
        return len(graph[node] - nodes_set)

    while sum(map(count_neighbors_not_in_set, nodes_set)) != 3:
        node_with_max_neighbors = max(nodes_set, key=count_neighbors_not_in_set)
        nodes_set.remove(node_with_max_neighbors)

    print(len(nodes_set) * len(set(graph) - nodes_set))

if __name__ == "__main__":
    main()