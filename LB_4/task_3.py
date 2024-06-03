'''
Для третього завдання ми також реалізуємо обхід у глибину, 
але для графа, заданого списком суміжних вершин. Тут граф представлений у вигляді 
словника, де ключі - вершини, а значення - списки суміжних вершин.
'''

def dfs_adj_list(graph, start):
    visited = {}
    stack = [start]
    traversal_order = []

    for vertex in graph.keys():
        visited[vertex] = False

    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            traversal_order.append(vertex)
            stack.extend(v for v in graph[vertex] if not visited[v])

    return traversal_order

# Приклад графа заданого списком суміжних вершин
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
