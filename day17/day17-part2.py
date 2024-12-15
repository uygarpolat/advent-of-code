import heapq

def shortest_path_ultra(grid):

    rows = len(grid)
    cols = len(grid[0])
    start_state = ((0,0), (0,0), 0)
    pq = [(0, start_state)]
    visited = {start_state: 0}

    dirs = [(1,0), (0,-1), (-1,0), (0,1)]
    end_loc = (rows-1, cols-1)

    while pq:
        cost, (cur_loc, old_dir, straight_count) = heapq.heappop(pq)

        if visited[(cur_loc, old_dir, straight_count)] < cost:
            continue

        if cur_loc == end_loc:
            if old_dir == (0,0) or straight_count >= 4:
                return cost
            else:
                pass

        reverse_dir = (-old_dir[0], -old_dir[1]) if old_dir != (0,0) else None

        for dir in dirs:
            if reverse_dir is not None and dir == reverse_dir:
                continue

            new_loc = (cur_loc[0] + dir[0], cur_loc[1] + dir[1])
            if not (0 <= new_loc[0] < rows and 0 <= new_loc[1] < cols):
                continue

            if old_dir == (0,0):
                next_straight_count = 1
            else:
                if dir == old_dir:
                    if straight_count == 10:
                        continue
                    next_straight_count = straight_count + 1
                else:
                    if straight_count < 4:
                        continue
                    next_straight_count = 1

            new_cost = cost + grid[new_loc[0]][new_loc[1]]
            new_state = (new_loc, dir, next_straight_count)

            if (new_state not in visited) or (visited[new_state] > new_cost):
                visited[new_state] = new_cost
                heapq.heappush(pq, (new_cost, new_state))

    return None

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        grid = [list(map(int, line.strip())) for line in file]

    min_cost = shortest_path_ultra(grid)
    
    print("Minimal heat loss (ultra crucible):", min_cost)

if __name__ == "__main__":
    main()
