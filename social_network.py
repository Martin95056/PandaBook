from panda import Panda
from collections import deque
import json


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

    def dict_of_friends_of_panda(self, panda):
        dict_friends = []
        for friend in self.friends_of(panda):
            dict_friends.append(friend.panda_to_dict())
        return dict_friends

    def connection_level(self, panda1, panda2):
        return self.bfs_with_level(panda1, panda2)

    def bfs_with_level(self, panda1, panda2):
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

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((level + 1, neighbour))
        return -1

    def are_connected(self, panda1, panda2):
        queue = deque()
        visited = set()

        visited.add(panda1)
        queue.append(panda1)

        while len(queue) != 0:
            node = queue.popleft()

            for neighbour in self.graph[node]:
                if neighbour != panda2:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
                else:
                    return True
        return False

    def how_many_gender_in_network(self, level, panda, gender):
        queue = deque()
        visited = set()

        visited.add(panda)
        queue.append(panda)

        count_male = 0
        count_female = 0

        my_level = 0

        while len(queue) != 0:
            node = queue.popleft()

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                    if neighbour.isMale():
                        count_male += 1
                    if neighbour.isFemale():
                        count_female += 1
            if level == my_level:
                return self.check_gender(gender, count_male, count_female)
            my_level += 1

    def check_gender(self, gender, count_male, count_female):
        if gender == "male":
            return count_male
        if gender == "female":
            return count_female

    def load(self):
        with open('pandabook.json', 'r') as f:
            data = json.load(f)

        return data

    def save(self):
        data = self.load()
        dict_graph = {}
        for panda in self.graph:
            dict_graph[panda.panda_to_dict()] = self.dict_of_friends_of_panda(panda)

        data.update(dict_graph)

        with open('pandabook.json', 'w') as f:
            json.dump(data, f, indent=4, sort_keys=True)
