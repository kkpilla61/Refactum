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
# ##################################################
# 3) Check if the feature graph is a subgraph of the workpiece workpiece and find any other matching subgraphs
# ##################################################

GM = nx.algorithms.isomorphism.GraphMatcher(workpiece_graph, feature_graph, node_match=None, edge_match=None)
is_subgraph = GM.subgraph_is_monomorphic()
# Print result
if is_subgraph:
    print("✅ The feature graph is a subgraph of the workpiece graph.")
else:
    print("❌ The feature graph is NOT a subgraph of the workpiece graph.")
# ##################################################
# 4) Results
# ##################################################

# Print results if matches are found. Return the number of matches and the node ids.

# Find matching nodes (common nodes between both graphs)
matched_nodes = list(set(workpiece_graph.nodes) & set(feature_graph.nodes))

# Find matching edges (common edges between both graphs)
matched_edges = list(set(workpiece_graph.edges) & set(feature_graph.edges))

# Print results
print(f"✅ Number of Matching Nodes: {len(matched_nodes)}")
print(f"🔹 Matching Node IDs: {matched_nodes}")

