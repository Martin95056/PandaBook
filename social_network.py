from panda import Panda
from collections import deque


class SocialNetwork:

    def __init__(self):
        self.graph = {}

    def _get_graph(self):
        return self.graph

    def add_panda(self, panda):
        self.graph[panda] = set()

    def has_panda(self, panda):
        if panda in self.graph.keys():
            return True
        return False

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)

        if not self.has_panda(panda2):
            self.add_panda(panda2)

        self.graph[panda1].add(panda2)
        self.graph[panda2].add(panda1)

    def are_friends(self, panda1, panda2):
        if panda2 in self.graph[panda1] and panda1 in self.graph[panda2]:
            return True
        return False

    def friends_of(self, panda):
        if not self.has_panda(panda):
            return False
        return self.graph[panda]

    def connected_level(self, panda1, panda2):
        return self.BFS_algo(panda1, panda2)

    def BFS_algo(self, panda1, panda2):
        queue = deque()
        visited = set()

        visited.add(panda1)
        queue.append((0, panda1))

        while len(queue) != 0:
            node_with_level = queue.popleft()
            node = node_with_level[1]
            level = node_with_level[0]

            if node == panda2:
                return level

            for neighbour in self.graph[panda1]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((level + 1, neighbour))
        return -1


network = SocialNetwork()
ivo = Panda("Ivo", "ivo@pandamail.com", "male")
rado = Panda("Rado", "rado@pandamail.com", "male")
tony = Panda("Tony", "tony@pandamail.com", "female")

for panda in [ivo, rado, tony]:
    network.add_panda(panda)

network.make_friends(ivo, rado)
network.make_friends(rado, tony)

network.connected_level(ivo, rado) == 1  # True
network.connected_level(ivo, tony) == 2  # True

# network.how_many_gender_in_network(1, rado, "female") == 1 # True
