# Breadth First Search (BFS) - uses a QUEUE (First In First Out)
from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}

def bfs(graph, start):
    queue = deque([start])
    visited = [start]                    # a node is marked visited when it enters the queue
    order = []
    print(f"{'Iteration':<11}{'Visited Node':<14}Queue (front -> rear)")
    iteration = 0
    while queue:
        node = queue.popleft()           # remove from the front
        order.append(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)  # add at the rear
        iteration += 1
        print(f"{iteration:<11}{node:<14}{list(queue)}")
    return order

if __name__ == "__main__":
    start = input("Enter start node (default A): ").strip().upper() or "A"
    if start not in graph:
        print("Node not found in the graph.")
    else:
        print()
        order = bfs(graph, start)
        print("\nBFS traversal order:", " -> ".join(order))
