'''
Для шостого завдання реалізуємо обхід у глибину 
для графа, заданого матрицею суміжності. Матриця суміжності представляє 
собою квадратну матрицю, де matrix[i][j] вказує на наявність або відсутність 
ребра між вершинами i і j.
'''

def dfs_adj_matrix(matrix, start):
    n = len(matrix)
    visited = [False] * n
    stack = [start]
    traversal_order = []

    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            traversal_order.append(vertex)
            for i in range(n):
                if matrix[vertex][i] == 1 and not visited[i]:
                    stack.append(i)

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
