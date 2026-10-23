# Depth First Search (DFS) - uses a STACK (Last In First Out)
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}

def dfs_iterative(graph, start):
    stack = [start]
    visited = []
    print(f"{'Iteration':<11}{'Visited Node':<14}Stack (top = right end)")
    iteration = 0
    while stack:
        node = stack.pop()               # remove from the top
        if node in visited:
            continue
        visited.append(node)
        # push children in reverse so that the left-most child is visited first
        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)
        iteration += 1
        print(f"{iteration:<11}{node:<14}{stack}")
    return visited

def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = []
    visited.append(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs_recursive(graph, neighbour, visited)
    return visited

if __name__ == "__main__":
    start = input("Enter start node (default A): ").strip().upper() or "A"
    if start not in graph:
        print("Node not found in the graph.")
    else:
        print()
        order = dfs_iterative(graph, start)
        print("\nDFS traversal order (using stack)    :", " -> ".join(order))
        print("DFS traversal order (using recursion):", " -> ".join(dfs_recursive(graph, start)))
