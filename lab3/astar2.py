import heapq

def h(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    pq = []
    heapq.heappush(pq, (0, start))

    g_cost = {start: 0}
    parent = {start: None}

    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    while pq:
        _, current = heapq.heappop(pq)
        if current == goal:
            path = []
            while current:
                path.push(current)
                current = parent[current]
            return path[::-1]
        


                
