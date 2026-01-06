from collections import deque

def bidirectional_bfs(graph, start, goal):
    if start == goal:
        print("Goal found immediately")
        return

    front_start = deque([start])
    front_goal = deque([goal])

    visited_start = {start}
    visited_goal = {goal}

    steps = 0

    while front_start and front_goal:
        steps += 1

        # Expand from start side
        for _ in range(len(front_start)):
            node = front_start.popleft()
            for neighbour in graph[node]:
                if neighbour in visited_goal:
                    print("Goal found!")
                    print("Steps explored:", steps)
                    return
                if neighbour not in visited_start:
                    visited_start.add(neighbour)
                    front_start.append(neighbour)

        # Expand from goal side
        for _ in range(len(front_goal)):
            node = front_goal.popleft()
            for neighbour in graph[node]:
                if neighbour in visited_start:
                    print("Goal found!")
                    print("Steps explored:", steps)
                    return
                if neighbour not in visited_goal:
                    visited_goal.add(neighbour)
                    front_goal.append(neighbour)

    print("Goal not found")

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'G'],
    'E': ['C', 'G'],
    'G': ['D', 'E']
}
bidirectional_bfs(graph, 'A', 'G')
