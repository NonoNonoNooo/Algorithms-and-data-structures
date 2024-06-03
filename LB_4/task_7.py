'''
Для сьомого завдання реалізуємо обхід у глибину для графа, 
заданого списком суміжних вершин.
'''

def dfs_adj_list(graph, start):
    visited = set()
    stack = [start]
    traversal_order = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal_order.append(vertex)
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal_order

# Приклад списку суміжних вершин графа
adj_list = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

# Початкова вершина для обходу
start_vertex = 0

# Виклик функції для обходу графа у глибину
result = dfs_adj_list(adj_list, start_vertex)
print("DFS traversal for adjacency list graph:", result)
