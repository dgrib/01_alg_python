"""
2. Доработать алгоритм Дейкстры (рассматривался на уроке),
чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
"""
g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dejkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    parent[start] = start
    # будет использоваться при поиске пути в parent
    start_save = start
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:

                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')

        for i in range(length):

            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    # начало 2 задания
    # список путей от start до каждой вершины
    path_list = [[] for _ in range(length)]

    # разматываем путь в parent для каждой вершины
    for i, item in enumerate(parent):

        if item == -1:
            path_list[i].append('нет пути')
            continue
        # нашли сам узел от которого считаем
        elif item == i:
            path_list[i].append(item)
        else:
            j = item
            while j != start_save:
                path_list[i].insert(0, j)
                j = parent[j]
            # добавляем сам узел в конец
            path_list[i].append(i)
            # добавляем start узел в начало
            path_list[i].insert(0, start_save)

    return cost, path_list


s = int(input('От какой вершины идти: '))
cost_list, path_list = dejkstra(g, s)
print(cost_list)
for i, path in enumerate(path_list):
    print(f'Путь от {s} до {i} стоит {cost_list[i]:3} уе: {path}')

