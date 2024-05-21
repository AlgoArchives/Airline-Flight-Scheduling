from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]
    
    def add_edge(self, u, v, w):
        self.graph[u][v] = w

    def bfs(self, source, sink, parent):
        visited = [False] * self.V
        queue = deque([source])
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            
            for v, capacity in enumerate(self.graph[u]):
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False
    
    def edmonds_karp(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0
        
        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink
            
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
                
            max_flow += path_flow
            
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
                
        return max_flow

# Example usage:
vertices = 4
graph = Graph(vertices)

# Edges along with capacities (maximum passengers)
graph.add_edge(0, 1, 30)  # A -> B
graph.add_edge(0, 2, 20)  # A -> C
graph.add_edge(1, 2, 10)  # B -> C
graph.add_edge(1, 3, 20)  # B -> D
graph.add_edge(2, 3, 20)  # C -> D

source = 0  # Source node (A)
sink = 3    # Sink node (D)

print(f"Maximum number of passengers that can be transported: {graph.edmonds_karp(source, sink)}")