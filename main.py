import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes (airports)
G.add_node("Airport_A")
G.add_node("Airport_B")
G.add_node("Airport_C")

# Add edges (flights) with capacities
G.add_edge("Airport_A", "Airport_B", capacity=100)
G.add_edge("Airport_A", "Airport_C", capacity=150)
G.add_edge("Airport_B", "Airport_C", capacity=200)

# Find the maximum flow
max_flow_value = nx.maximum_flow_value(G, "Airport_A", "Airport_C", capacity='capacity')
print("Maximum Flow Value:", max_flow_value)