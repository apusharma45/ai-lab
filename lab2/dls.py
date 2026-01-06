def dls(graph, current, goal, visited, limit, depth):
    visited.append(current)

    if current == goal:
        print("goal found")
        return True

    if depth == limit:
        return False  

    for neighbour in graph[current]:
        if neighbour not in visited:
            if dls(graph, neighbour, goal, visited, limit, depth + 1):
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
dls(graph, 'A', 'G', visited, limit=3, depth=0)
print("Nodes explored:", len(visited))
