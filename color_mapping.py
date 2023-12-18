import networkx as nx
import matplotlib.pyplot as plt

# Given graph representing regions and their neighbors
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

# Dictionary to store colors for each region
colors = {}

# List of available colors
available_colors = ['red', 'green', 'blue']

# Create a graph
G = nx.Graph(graph)

# Function to check if it's valid to color a region with a specific color
def is_valid_color(region, color):
    for neighbor in graph[region]:
        if colors.get(neighbor) == color:
            return False  # Invalid color if any neighbor has the same color
    return True

# Simple method to color regions recursively
def color_regions(region):
    for color in available_colors:
        if is_valid_color(region, color):
            colors[region] = color
            # Recursively color the next region
            next_region = next((r for r in graph if r not in colors), None)
            if next_region:
                color_regions(next_region)
            else:
                break  # Stop if all regions are colored

# Start coloring from any region
start_region = next(iter(graph))
color_regions(start_region)

# Draw the graph with colors
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_size=8, font_color='black',
        node_size=700, node_color=[colors.get(node, 'white') for node in G.nodes()],
        edge_color='black', linewidths=0.5, arrowsize=10)

# Display the graph
plt.show()
