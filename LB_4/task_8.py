def dfs_adj_matrix(graph, start):
    visited = set()
    stack = [start]
    traversal_order = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal_order.append(vertex)
            for neighbor in range(len(graph[vertex]) - 1, -1, -1):
                if graph[vertex][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)

    return traversal_order

# Приклад матриці суміжності графа
adj_matrix = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0]
]

# Початкова вершина для обходу
start_vertex = 0

# Виклик функції для обходу графа у глибину
result = dfs_adj_matrix(adj_matrix, start_vertex)
print("DFS traversal for adjacency matrix graph:", result)
