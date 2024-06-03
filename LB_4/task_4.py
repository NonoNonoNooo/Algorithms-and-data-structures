'''
Для четвертого завдання ми також реалізуємо обхід у глибину, 
але для графа, заданого матрицею суміжностей. Тут граф представлений у вигляді 
квадратної матриці, де значення 1 в позиції [i][j] означає наявність ребра між 
вершинами i та j.
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
            for v in range(n):
                if graph[vertex][v] == 1 and not visited[v]:
                    stack.append(v)

    return traversal_order

# Приклад графа заданого матрицею суміжностей
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
