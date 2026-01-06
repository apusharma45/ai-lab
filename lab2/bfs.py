from collections import deque

def bfs(graph, start, goal):
    count = 0
    explored = set()
    frontier = deque([start])
    
    while frontier:
        node = frontier.popleft()
        count+=1
        if(node == goal):
            print("Goal reached!")
            print("Steps", count)
            return
        
        explored.add(node)
        for neighbour in graph[node] :
            if neighbour not in explored and neighbour not in frontier:
                frontier.append(neighbour)
    
    print("Goal not found")
    print("Steps checked:", count)
            

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

bfs(graph, start='A', goal='B')