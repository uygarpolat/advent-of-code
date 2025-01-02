from collections import defaultdict, deque
from functools import lru_cache

def is_in_grid(grid, loc):
    rows = len(grid)
    cols = len(grid[0])
    row = loc[0]
    col = loc[1]
    return 0 <= row < rows and 0 <= col < cols

def find_intersections(grid):
    rows, cols = len(grid), len(grid[0])
    intersections = {(0, 1), (rows-1, cols-2)}
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '#':
                neighbors = 0
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    if is_in_grid(grid, (nr, nc)) and grid[nr][nc] != '#':
                        neighbors += 1
                if neighbors > 2:
                    intersections.add((r, c))
    return intersections

def find_distances(grid, start, intersections):
    distances = {}
    queue = deque([(start, 0, {start})])
    
    while queue:
        pos, dist, visited = queue.popleft()
        
        if pos in intersections and pos != start:
            distances[pos] = dist
            continue
            
        r, c = pos
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            new_pos = (nr, nc)
            
            if (is_in_grid(grid, new_pos) and 
                grid[nr][nc] != '#' and 
                new_pos not in visited):
                queue.append((new_pos, dist + 1, visited | {new_pos}))
                
    return distances

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file]
    
    intersections = find_intersections(grid)
    
    graph = {}
    for inter in intersections:
        graph[inter] = find_distances(grid, inter, intersections)
    
    start = (0, 1)
    end = (len(grid)-1, len(grid[0])-2)
    
    @lru_cache(maxsize=None)
    def dfs(pos, visited):
        if pos == end:
            return 0
            
        max_dist = float('-inf')
        visited = set(visited)
        
        for next_pos, dist in graph[pos].items():
            if next_pos not in visited:
                result = dfs(next_pos, frozenset(visited | {next_pos}))
                if result != float('-inf'):
                    max_dist = max(max_dist, dist + result)
                    
        return max_dist
    
    longest_path = dfs(start, frozenset({start}))
    print(f"Solution for Part 2: {longest_path}")

if __name__ == "__main__":
    main()