import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add airports with attributes
G.add_node("Airport_A", location="City_A", runway_capacity=10, operating_hours="08:00-20:00")
G.add_node("Airport_B", location="City_B", runway_capacity=8, operating_hours="07:00-19:00")
G.add_node("Airport_C", location="City_C", runway_capacity=12, operating_hours="06:00-22:00")

# Add flights with attributes
G.add_edge("Airport_A", "Airport_B", capacity=100, departure_time="08:30", arrival_time="10:30", duration=2)
G.add_edge("Airport_A", "Airport_C", capacity=150, departure_time="09:00", arrival_time="12:00", duration=3)
G.add_edge("Airport_B", "Airport_C", capacity=200, departure_time="10:00", arrival_time="13:00", duration=3)

# Display airport and flight attributes
for node in G.nodes(data=True):
    print("Airport:", node)

for edge in G.edges(data=True):
    print("Flight:", edge)