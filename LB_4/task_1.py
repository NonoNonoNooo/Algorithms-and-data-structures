'''
Для першого завдання ми реалізуємо обхід у глибину для графа, заданого
списком суміжних вершин. Тут граф представлений у вигляді словника, де ключі - це вершини, 
а значення - це список суміжних вершин.
'''

def dfs(graph, start):
    visited = set()
    stack = [start]
    traversal_order = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal_order.append(vertex)
            stack.extend(graph[vertex] - visited)

    return traversal_order

# Приклад графа заданого списком суміжних вершин
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

# Початкова вершина для обходу
start_vertex = 'A'

# Виклик функції для обходу графа у глибину
result = dfs(graph, start_vertex)
print("DFS traversal:", result)
