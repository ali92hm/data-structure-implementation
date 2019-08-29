from collections import deque
from collections import defaultdict

class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self._data = defaultdict(list)

    def add_vertex(self, from_node, to_node):
        self._data[from_node].append(to_node)
        if not self.directed:
            self._data[to_node].append(from_node)

    def can_get_to(self, start, end):
        return self.dfs(start, end)

    def dfs(self, start, end, visited=set()):
        if start == end:
            return True

        visited.add(start)
        path = False
        for neighbor in self._data[start]:
            if neighbor not in visited:
                path = path or self.dfs(neighbor, end, visited)

        return path

    def shortest_path(self, start, end):
        return self.bfs(start, end)

    def bfs(self, start, end):
        queue = deque()
        path = defaultdict(list)
        path[start] = [start]
        queue.append(start)

        while queue:
            current = queue.popleft()
            if current == end:
                return path[end]

            for neighbor in self._data[current]:
                if neighbor not in path:
                    path[neighbor] = list(path[current] + [neighbor])
                    queue.append(neighbor)
        return []
