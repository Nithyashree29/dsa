# # //Edge list - just representing connection
# #   2    0
# # 1   3
# graph = [[0,2], [2,3], [2,1], [1,3]]

# # Adjacent List - index is node , value is nodes neighboures
# graph = [[2], [2,3], [0,1,3], [1,2]]


# # Adjacent matrix
# graph = [
#     [0, 0, 1, 0], #node 0 connected to 2
#     [0, 0, 1, 1], # node 1  connected to 2 and 3
#     [1, 1, 0, 1],
#     [0, 1, 1, 0]
# ]

# graph = {
#    0:  [0, 0, 1, 0], #node 0 connected to 2
#    1:  [0, 0, 1, 1], # node 1  connected to 2 and 3
#    2:  [1, 1, 0, 1],
#    3:  [0, 1, 1, 0]
# }

class Graph:
    def __init__(self):
        self.graph = {}

    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def addedge(self, vertex1, vertex2):
        if vertex1 in self.graph  and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def print_graph(self):
        for vertex in self.graph:
            print(f'{vertex}: {self.graph[vertex]}')

obj1 = Graph()
obj1.addVertex('A')
obj1.addVertex('B')
obj1.addVertex('C')
obj1.addVertex('D')
obj1.addedge('B', 'C')
obj1.addedge('A', 'C')
obj1.addedge('B', 'D')
obj1.addedge('B', 'C')
obj1.print_graph()


