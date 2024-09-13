import random
from collections import deque

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        self.previous = None

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
    predecessors = {a: None}

    while queue:
        node = queue.popleft()
        
        
        if node == b:
            path = []
            while node is not None:
                path.append(node)
                node = predecessors[node]
            return path[::-1]

        for neighbor in G[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                predecessors[neighbor] = node

    
    return None


size = 10
G = erdos_renyi_model(size, .3)

print("Граф")
for _l in G:
    print(G[_l])


print("Вершины")
a = random.randrange(size)
b = random.randrange(size)

print(a, b)

print("Путь")
if a != b:
    print("Вершины допустимы")
    path = bfs_search(a, b, G)
    print(path)
   
