import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Given graph
graph = {
    'Vr': {'Ct', 'Bw'},
    'Ct': {'Vr', 'Bw'},
    'Bw': {'Vr', 'Ct', 'Gq', 'Bloem'},
    'Gq': {'Bw', 'Mas'},
    'Bloem': {'Bw', 'Mas', 'Pre'},
    'Mas': {'Gq', 'Bloem', 'Dur', 'Pre'},
    'Dur': {'Mas', 'Pre'},
    'Pre': {'Dur', 'Mas', 'Bloem'}
}

# Create a directed graph
G = nx.Graph(graph)

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_size=8, font_color='black', node_size=700, node_color='skyblue', edge_color='gray', linewidths=0.5, arrowsize=10)

# Display the graph
plt.show()
