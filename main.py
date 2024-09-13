import random


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        self.previous = None
        self.cost = float("inf")

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.get_next_node():
                current = current.get_next_node()
            current.set_next_node(new_node)

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.get_value())
            current = current.get_next_node()
        return elements


def erdos_renyi_model(n, p):

    G = {i: LinkedList() for i in range(n)}

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                G[i].append(j)
                G[j].append(i)
    return G


def choose_node(reachable, goal_node):
    min_cost = float("inf")
    best_node = None

    for node in reachable:
        cost_start_to_node = node.cost
        cost_node_to_goal = estimate_distance(node, goal_node)
        total_cost = cost_start_to_node + cost_node_to_goal

        if min_cost > total_cost:
            min_cost = total_cost
            best_node = node

    return best_node


def estimate_distance(node, goal_node):
    # Эвристика. Граф неориентирован и невзвешенный. Минимальное расстояние 1.
    return 1


def get_adjacent_nodes(node_value, G):
    return G[node_value].print_list()


def build_path(node):
    path = []
    while node:
        path.append(node.get_value())
        node = node.previous
    return path[::-1]


def find_path_Astar(a, b, G):
    start_node = Node(a)
    start_node.cost = 0
    goal_node = Node(b)

    reachable = [start_node]
    explored = set()

    while reachable:
        node = choose_node(reachable, goal_node)
        if node.get_value() == b:
            return build_path(node)

        reachable.remove(node)
        explored.add(node.get_value())

        new_reachable = set(get_adjacent_nodes(node.get_value(), G)) - explored

        for adj in new_reachable:
            adj_node = Node(adj)

            if adj_node.get_value() not in [n.get_value() for n in reachable]:
                reachable.append(adj_node)

            if node.cost + 1 < adj_node.cost:
                adj_node.previous = node
                adj_node.cost = node.cost + 1

    return None


size = 10
G = erdos_renyi_model(size, 0.3)

for _l in G:
    print(G[_l].print_list())

print()

a = random.randrange(size)
b = random.randrange(size)

print(find_path_Astar(a, b, G))
