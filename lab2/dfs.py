def dfs(graph, current, goal, visited):
    visited.append(current)
    if(current == goal):
        print("goal found")
        return True
    for neighbour in graph[current]:
        if neighbour not in visited:
            if dfs(graph, neighbour, goal, visited):
                return True
    return False


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

visited = []
dfs(graph, current='A', goal='G', visited = visited)
print("steps: ", len(visited))