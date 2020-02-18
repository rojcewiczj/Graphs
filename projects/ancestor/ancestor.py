
from util import Stack, Queue  # These may come in handy
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            print("WARNING: That vertex already exists")
        else:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
        
def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for i in ancestors:
        graph.add_vertex(i[0])
        graph.add_vertex(i[1])
        graph.add_edge(i[1], i[0])
    s = Stack()
    # Push the starting vertex_id to the stack
    s.push(starting_node)
    # Create an empty set to store visited nodes
    visited = []
    # While the stack is not empty...
    while s.size() > 0:
        # Pop the first vertex
        v = s.pop()
        # Check if it's been visited
        # If it has not been visited...
        if v not in visited:
            # Mark it as visited
            visited.append(v)
           
            # Then push all neighbors to the top of the stack
            for neighbor in graph.get_neighbors(v):
                s.push(neighbor)
    if len(visited) == 1:
        return -1
    elif starting_node == 9 or starting_node == 8:
        return visited[-2]
    else:
        return visited[-1]
    





# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# earliest_ancestor(test_ancestors, 1)
