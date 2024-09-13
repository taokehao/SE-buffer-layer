import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Number of nodes
num_nodes = 25
half_neighbors = 6  # Number of neighbors to connect on each side from the opposite side

# Create an empty graph
G = nx.Graph()

# Add nodes
for i in range(num_nodes):
    G.add_node(i)

# Add edges to connect each node to its neighbors on the opposite side
for i in range(num_nodes):
    for j in range(1, half_neighbors + 1):
        G.add_edge(i, (i + num_nodes // 2 + j) % num_nodes)
        G.add_edge(i, (i + num_nodes // 2 - j) % num_nodes)

# Create a circular layout
pos = nx.circular_layout(G)

# Scale positions to avoid overlap
scale = 2.0  # Increase this value to increase the distance between nodes
for key in pos:
    pos[key] *= scale

# Define node colors
node_colors = ['#CC5B45'] * 15 + ['#57AF37'] + ['#F5A216'] * 2 + ['#6A8EC9'] * 6

# Add an extra color to match the number of nodes
node_colors += ['#D9A421']

# Draw the graph
plt.figure(figsize=(12, 12), dpi=500)
nx.draw_networkx_nodes(G, pos, node_size=4000, node_color=node_colors, edgecolors='black')  # Increased node size
nx.draw_networkx_edges(G, pos, width=0.5, alpha=0.5)

# Set the font to Arial
plt.rcParams['font.family'] = 'Arial'

# Draw labels
labels = {i: f'{i+1:02d}' for i in range(num_nodes)}
nx.draw_networkx_labels(G, pos, labels, font_size=25)

# Customize the plot
plt.axis('off')

# Save the figure as a transparent PNG
file_path = 'circular_graph_colored.png'
plt.savefig(file_path, transparent=True, bbox_inches='tight', pad_inches=0)
plt.close()

print(f"The graph has been saved as {file_path}")
