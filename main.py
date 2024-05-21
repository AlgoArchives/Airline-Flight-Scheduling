import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Edges along with their capacities (maximum passengers)
G.add_edge('A', 'B', capacity=30)
G.add_edge('A', 'C', capacity=20)
G.add_edge('B', 'C', capacity=10)
G.add_edge('B', 'D', capacity=20)
G.add_edge('C', 'D', capacity=20)

# Define the source and sink nodes
source = 'A'
sink = 'D'

# Calculate the maximum flow
flow_value, flow_dict = nx.maximum_flow(G, source, sink)

print(f"Maximum number of passengers that can be transported: {flow_value}")
print("Flow distribution:")
for origin, flows in flow_dict.items():
    for destination, flow in flows.items():
        if flow > 0:
            print(f"{origin} -> {destination}: {flow} passengers")