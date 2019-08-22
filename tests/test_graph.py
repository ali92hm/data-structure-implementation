import unittest
from src.Graph import Graph

g = Graph(True)
g.add_vertex('A', 'B')
g.add_vertex('A', 'D')
g.add_vertex('A', 'Z')
g.add_vertex('B', 'A')
g.add_vertex('C', 'A')
g.add_vertex('C', 'E')
g.add_vertex('D', 'E')
g.add_vertex('D', 'B')
g.add_vertex('E', 'F')
g.add_vertex('E', 'C')
g.add_vertex('F', 'C')
g.add_vertex('F', 'G')
g.add_vertex('G', 'F')
g.add_vertex('G', 'F')
g.add_vertex('H', 'H')


print(g.shortest_path('A', 'C'))
