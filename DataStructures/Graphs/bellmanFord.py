

class Graph:

    def __init__(self, vertices):
        self.V = vertices # Total number of vertices in the graph
        self.graph = [] # Array of edges


    def add_edge(self, s, d, w):
        self.graph.append([s,d,w])

    def print_solution(self,distances):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i,distances[i]))

    def bellman_ford(self, src):

        # set all distances to infinity and previous vertex to NULL
        distances = [float("inf")]*self.V
        #mark the source vertex distance as 0
        distances[src] = 0

        # loop through from start to finish and add the distances. Replace the distance between two nodes from the graph arrays
        for _ in range(self.V - 1):
            for s,d,w in self.graph:
                if distances[s] != float("inf") and distances[d] > distances[s] + w:
                    distances[d] = distances[s] + w

        # check for negative loop
        for s,d,w in self.graph:
            if distances[s] != float("inf") and distances[d] > distances[s] + w:
                print("Graph contains negative weight cycle between vertices {0} and {1}".format(s,d))
                return

        self.print_solution(distances)


g = Graph(5)
# g.add_edge(0, 1, 5)
# g.add_edge(0, 2, 4)
# g.add_edge(1, 3, 3)
# g.add_edge(2, 1, 6)
# g.add_edge(3, 2, 2)

g.add_edge(0,1,4)
g.add_edge(0,2,2)
g.add_edge(1,2,-3)
g.add_edge(2,1,1)
g.add_edge(1,3,2)
g.add_edge(1,4,3)
g.add_edge(2,3,4)
g.add_edge(2,4,5)
g.add_edge(4,3,-5)


g.bellman_ford(0)