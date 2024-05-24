import pandas as pd
from collections import defaultdict, deque

# Load the dataset
df = pd.read_csv('flight-delays/flights.csv')

# Filter relevant columns: 'ORIGIN_AIRPORT', 'DESTINATION_AIRPORT', 'PASSENGERS'
df = df[['ORIGIN_AIRPORT', 'DESTINATION_AIRPORT', 'PASSENGERS']]

# Clean the data (remove rows with missing values and invalid entries)
df.dropna(inplace=True)
df = df[df['PASSENGERS'] > 0]

# Create a graph as an adjacency list
graph = defaultdict(dict)

# Populate the graph with edges and capacities
for _, row in df.iterrows():
    origin = row['ORIGIN_AIRPORT']
    destination = row['DESTINATION_AIRPORT']
    passengers = row['PASSENGERS']
    
    if destination in graph[origin]:
        graph[origin][destination] += passengers
    else:
        graph[origin][destination] = passengers

# Implementing the Edmonds-Karp algorithm
class FlightGraph:
    def __init__(self, graph):
        self.graph = graph
        self.residual_graph = {u: dict(v) for u, v in graph.items()}
        self.V = len(graph)

    def bfs(self, source, sink, parent):
        visited = {u: False for u in self.graph}
        queue = deque([source])
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            
            for v, capacity in self.residual_graph[u].items():
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False
    
    def edmonds_karp(self, source, sink):
        parent = {u: None for u in self.graph}
        max_flow = 0
        
        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink
            
            while s != source:
                path_flow = min(path_flow, self.residual_graph[parent[s]][s])
                s = parent[s]
                
            max_flow += path_flow
            
            v = sink
            while v != source:
                u = parent[v]
                self.residual_graph[u][v] -= path_flow
                self.residual_graph[v][u] += path_flow
                v = parent[v]
                
        return max_flow

# Define the source and sink nodes based on your dataset
# For demonstration, using a small subset of the graph
small_graph = {
    'JFK': {'LAX': 300, 'ORD': 200},
    'LAX': {'ORD': 100, 'DFW': 200},
    'ORD': {'DFW': 150, 'LAX': 50},
    'DFW': {}
}

flight_graph = FlightGraph(small_graph)
source = 'JFK'
sink = 'DFW'

print(f"Maximum number of passengers that can be transported: {flight_graph.edmonds_karp(source, sink)}")

# Display the optimized flow distribution
print("Flow distribution in the residual graph:")
for origin, destinations in flight_graph.residual_graph.items():
    for destination, capacity in destinations.items():
        print(f"{origin} -> {destination}: {capacity} passengers")