import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    open_set = []
    heapq.heappush(open_set, (0, start))

    g_cost = {start: 0}
    parent = {start: None}

    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            neighbor = (nx, ny)

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_g = g_cost[current] + 1

                if neighbor not in g_cost or new_g < g_cost[neighbor]:
                    g_cost[neighbor] = new_g
                    f = new_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f, neighbor))
                    parent[neighbor] = current

    return None


grid = [
    [0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0],  
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0],  
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],  
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],  
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],  
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]   
]
