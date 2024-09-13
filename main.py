import random
from collections import deque


def erdos_renyi_model(n, p):

    G = {i: list() for i in range(n)}

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                G[i].append(j)
                G[j].append(i)
    return G


def bfs_search(a, b, G):
    if a == b:
        return [a]

    queue = deque([a])
    visited = set([a])
    prev = {a: None}

    while queue:
        node = queue.popleft()

        if node == b:
            path = []
            while node:
                path.append(node)
                node = prev[node]
            return path[::-1]

        for neighbor in G[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                prev[neighbor] = node

    return None


size = 10
G = erdos_renyi_model(size, 0.3)

print("Граф")
for _l in G:
    print(G[_l])


print("Вершины")
a = random.randrange(size)
b = random.randrange(size)

print(a, b)

print("Путь")
if a != b:
    path = bfs_search(a, b, G)
    print(path)
