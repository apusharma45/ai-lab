def dls(graph, current, goal, visited, limit, depth):
    visited.append(current)

    if current == goal:
        return True

    if depth == limit:
        return False  

    for neighbour in graph[current]:
        if neighbour not in visited:
            if dls(graph, neighbour, goal, visited, limit, depth + 1):
                return True

    return False

def iddfs(graph, start, goal, max_depth):
    for limit in range(max_depth+1):
        visited = []
        if dls(graph, start, goal, visited, limit, 0):
            print("goal found")
            print("steps:", len(visited))
            return
    print("goal not found")


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
iddfs(graph, 'A', 'G', max_depth=5)

