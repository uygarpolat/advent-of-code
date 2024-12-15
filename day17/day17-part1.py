import heapq

def shortest_path(grid):
    
    rows = len(grid)
    cols = len(grid[0])
    start_state = ((0,0), (0,0), 0)
    pq = [(0, start_state)]
    visited = {start_state: 0}

    dirs = [(1,0), (0,-1), (-1,0), (0,1)]
    end_loc = (rows-1, cols-1)

    while pq:
        cost, (cur_loc, old_dir, straight_count) = heapq.heappop(pq)

        if cur_loc == end_loc:
            return cost

        if visited[(cur_loc, old_dir, straight_count)] < cost:
            continue

        reverse_dir = None
        if old_dir != (0,0):
            reverse_dir = (-old_dir[0], -old_dir[1])

        for dir in dirs:
            if reverse_dir is not None and dir == reverse_dir:
                continue
            if dir == old_dir and straight_count == 3:
                continue

            new_loc = (cur_loc[0] + dir[0], cur_loc[1] + dir[1])
            if 0 <= new_loc[0] < rows and 0 <= new_loc[1] < cols:
                new_cost = cost + grid[new_loc[0]][new_loc[1]]
                next_straight_count = straight_count + 1 if dir == old_dir else 1
                new_state = (new_loc, dir, next_straight_count)

                if (new_state not in visited) or (visited[new_state] > new_cost):
                    visited[new_state] = new_cost
                    heapq.heappush(pq, (new_cost, new_state))
    return None

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        grid = [list(map(int, line.strip())) for line in file]

    min_cost = shortest_path(grid)

    print("Minimal heat loss:", min_cost)
    
if __name__ == "__main__":
    main()
