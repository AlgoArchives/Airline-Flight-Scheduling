import networkx as nx
import pickle

# Create a directed graph
G = nx.DiGraph()

# Nodes represent airports with certain attributes
G.add_node("Airport_A", location="City_A", runway_capacity=10, operating_hours="08:00-20:00")
G.add_node("Airport_B", location="City_B", runway_capacity=8, operating_hours="07:00-19:00")
G.add_node("Airport_C", location="City_C", runway_capacity=12, operating_hours="06:00-22:00")

# Edges represent flights with certain attributes
G.add_edge("Airport_A", "Airport_B", capacity=100, departure_time="08:30", arrival_time="10:30", duration=2)
G.add_edge("Airport_A", "Airport_C", capacity=150, departure_time="09:00", arrival_time="12:00", duration=3)
G.add_edge("Airport_B", "Airport_C", capacity=200, departure_time="10:00", arrival_time="13:00", duration=3)

# Display airport and flight attributes
print("Initial Airport Attributes:")
for node in G.nodes(data=True):
    print("Airport:", node)

print("\nInitial Flight Attributes:")
for edge in G.edges(data=True):
    print("Flight:", edge)

# Add capacity constraints to airports
G.nodes["Airport_A"]["passenger_capacity"] = 500
G.nodes["Airport_B"]["passenger_capacity"] = 700
G.nodes["Airport_C"]["passenger_capacity"] = 600

# Add maximum number of flights departing from each airport
G.nodes["Airport_A"]["max_departures"] = 5
G.nodes["Airport_B"]["max_departures"] = 4
G.nodes["Airport_C"]["max_departures"] = 6

# Display updated airport attributes
print("\nUpdated Airport Attributes:")
for node in G.nodes(data=True):
    print("Airport:", node)

# Save the graph to a file using pickle
with open("airport_graph.pkl", "wb") as f:
    pickle.dump(G, f)
