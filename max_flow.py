import networkx as nx
import pickle

# Load the graph from the file using pickle
with open("airport_graph.pkl", "rb") as f:
    G = pickle.load(f)

# Define the source and sink airports for the maximum flow calculation
source = "Airport_A"
sink = "Airport_C"

# Compute the maximum flow
flow_value, flow_dict = nx.maximum_flow(G, source, sink, capacity='capacity')

# Display the results
print("Maximum Flow Value from", source, "to", sink, ":", flow_value)
print("Flow Dictionary:")
for u, v_flow in flow_dict.items():
    for v, flow in v_flow.items():
        print(f"{u} -> {v}: {flow}")
