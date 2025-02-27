# ##################################################
# 1) Load workpiece graph and feature graph data from  json file
# ##################################################

# Note: Available files are: workpiece_graph.json, feature_graph.json

import json
from pyvis.network import Network
import networkx as nx
# Function to load the graph
def load_graph(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    G = nx.Graph()

    # Add nodes and edges
    for node_id, attributes in data.get("nodes", []):
        G.add_node(node_id, **attributes)
        for neighbor in attributes["connected_faces"]:
            G.add_edge(node_id, neighbor)

    return G
#Loading the graphs
workpiece_graph = load_graph('workpiece_graph.json')
feature_graph = load_graph('feature_graph.json')

# ##################################################
# 2) Create graphs from loaded data
# ##################################################

# Hint: The library networkx helps you to create a graph. You can use the nx.Graph() class to create a graph.
# Note: Other appraoches are also possible.

# Note: Optional task - Visualize the graph
# Example code:
nt = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
nt.from_nx(workpiece_graph)
nt.from_nx(feature_graph)
nt.show("workpiece_graph.html", notebook=False)
nt.show("feature_graph.html", notebook=False)
