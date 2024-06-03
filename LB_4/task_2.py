'''
Для другого завдання ми також реалізуємо обхід у глибину, 
але для графа, заданого матрицею суміжності. Тут граф представлений у вигляді 
двовимірного масиву, де graph[i][j] дорівнює 1, якщо існує ребро між вершиною 
i та вершиною j, і 0, якщо такого ребра немає.
'''

def dfs_adj_matrix(graph, start):
    n = len(graph)
    visited = [False] * n
    stack = [start]
    traversal_order = []

    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            traversal_order.append(vertex)
            stack.extend(i for i in range(n) if graph[vertex][i] == 1 and not visited[i])

    return traversal_order

# Приклад графа заданого матрицею суміжності
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


