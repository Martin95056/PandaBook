from panda import Panda


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
        return list(self.graph[panda])

    def connected_level(seld, panda1, panda2):
        pass
