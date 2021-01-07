"""
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было? Примечание. Решите задачу при помощи построения графа.
"""
from collections import deque


def get_graph(friends_num):
    """Формирует граф в виде матрицы смежности. На вход получает количество узлов графа."""
    graph = [[] for _ in range(friends_num)]

    for friend in range(len(graph)):
        for handshake in range(len(graph)):
            if friend == handshake:
                graph[friend].append(0)
            else:
                graph[friend].append(1)

    return graph


def get_handshakes(graph):
    """Считает количество рукопожатий. На вход получает граф в виде матрицы смежности."""
    is_visited = [False for _ in range(len(graph))]
    deq = deque([0])
    result = 0

    while len(deq) > 0:

        current = deq.pop()

        for i, hand_shake in enumerate(graph[current]):
            if hand_shake == 1 and not is_visited[i]:
                result += 1
                deq.appendleft(i)

            is_visited[current] = True

    return result


num = int(input('Введите количество друзей: '))
friends_graph = get_graph(num)
print(f'Если из {num} друзей, каждый пожмет руку друг другу, то будет {get_handshakes(friends_graph)} рукопожатий')




