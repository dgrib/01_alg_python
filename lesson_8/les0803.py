"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""
from random import randint


def get_graph(num):
    """
    Генерирует ориентированный связанный граф в виде списка смежности.
    :param num: количество вершин графа
    :return граф в виде списка смежности
    """
    graph = [[] for _ in range(num)]

    for i in range(len(graph)):
        possibles = list(range(len(graph)))
        possibles.remove(i)
        edges = []

        vertex_num = randint(1, len(possibles))
        for j in range(vertex_num):
            rand_idx = randint(0, len(possibles) - 1)
            edges.append(possibles.pop(rand_idx))

        graph[i].extend(sorted(edges))

    return graph


def bfs(graph, start):
    """
    Обходит граф по алгоритму поиска в глубину (Depth-First Search)
    :param graph:
    :param start:
    :return: список посещенных вершин.
    """
    is_visited = [False for _ in range(len(graph))]

    def recourse_func(graph, start, is_visited):
        is_visited[start] = True

        for vertex in graph[start]:

            if not is_visited[vertex]:
                recourse_func(graph, vertex, is_visited)

        return is_visited

    recourse_func(graph, start, is_visited)

    return is_visited


num = int(input('Введите количество вершин графа: '))
random_graph = get_graph(num)
for i, vertex in enumerate(random_graph):
    print(f'Вершина {i}: {vertex}')

s = int(input('С какой вершины начать обход графа?: '))
check_list = bfs(random_graph, s)

if all(check_list):
    print(f'Все вершины пройдены из {s}.')
else:
    for i, item in enumerate(check_list):
        if not item:
            print(f'Вершина {i} не может быть достигнута из {s}.')

# Пример, который выдает программа, когда вершина не может быть достигнута
# Введите количество вершин графа: 5
# Вершина 0: [1, 3]
# Вершина 1: [0]
# Вершина 2: [3]
# Вершина 3: [0, 1, 2]
# Вершина 4: [0, 1, 3]
# С какой вершины начать обход графа?: 0
# Вершина 4 не может быть достигнута из 0.

# Пример, когда алгоритм проходит все вершины
# Введите количество вершин графа: 5
# Вершина 0: [2, 3]
# Вершина 1: [0, 2, 3]
# Вершина 2: [0, 1, 3, 4]
# Вершина 3: [0, 1]
# Вершина 4: [1, 2, 3]
# С какой вершины начать обход графа?: 0
# Все вершины пройдены из 0.
