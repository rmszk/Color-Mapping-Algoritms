import networkx as nx
import matplotlib.pyplot as plt


'''	
# Given graph with original node labels
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

# Colors
colors = {'Vr': None, 'Ct': None, 'Bw': None, 'Gq': None, 'Bloem': None, 'Mas': None, 'Dur': None, 'Pre': None}
domain = {'red', 'green', 'blue'}

# Create a graph
G = nx.Graph(graph)

# Function to check if neighboring nodes have different colors
def valid_coloring(node, color):
    for neighbor in G.neighbors(node):
        if colors[neighbor] == color:
            return False
    return True

# Backtracking graph coloring algorithm
def color_graph(node):
    if all(colors[node] is not None for node in G.nodes()):
        return True

    for color in domain:
        if valid_coloring(node, color):
            colors[node] = color
            next_node = next((n for n in G.nodes() if colors[n] is None), None)
            if next_node is not None:
                if color_graph(next_node):
                    return True
            else:
                return True
            colors[node] = None
    return False

# Start coloring from any node
start_node = next(iter(graph.keys()))
color_graph(start_node)

# Draw the graph with alphabet labels and colors
alphabet_labels = {node: chr(ord('A') + i) for i, node in enumerate(G.nodes())}
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, labels=alphabet_labels, font_size=8, font_color='black', node_size=700, node_color=[colors[node] for node in G.nodes()], edge_color='gray', linewidths=0.5, arrowsize=10)

# Display the graph
plt.show()
'''
import networkx as nx
import matplotlib.pyplot as plt

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

# Function to check if neighboring nodes have different colors
def valid_coloring(node, color, graph, colors):
    for neighbor in graph.neighbors(node):
        if colors[neighbor] == color:
            return False
    return True

# Backtracking graph coloring algorithm with user-defined coloring function
def color_graph(node, graph, colors, domain, coloring_func):
    if all(colors[node] is not None for node in graph.nodes()):
        return True

    for color in domain:
        if coloring_func(node, color, graph, colors):
            colors[node] = color
            next_node = next((n for n in graph.nodes() if colors[n] is None), None)
            if next_node is not None:
                if color_graph(next_node, graph, colors, domain, coloring_func):
                    return True
            else:
                return True
            colors[node] = None
    return False

# User-defined coloring function
def user_coloring_function(node, color, graph, colors):
    # Example: Allow coloring only if the color is not 'red'
    return color != 'red'

# Get user-defined input
user_domain = input("Enter the set of colors (comma-separated): ").split(',')
user_colors = {node: None for node in graph}
user_start_node = input("Enter the starting node: ")

# Start coloring from the user-defined node using the user-defined coloring function
color_graph(user_start_node, nx.Graph(graph), user_colors, user_domain, user_coloring_function)

# Draw the graph with colors
pos = nx.spring_layout(nx.Graph(graph))
nx.draw(nx.Graph(graph), pos, with_labels=True, font_size=8, font_color='black', node_size=700, node_color=[user_colors[node] for node in graph], edge_color='gray', linewidths=0.5, arrowsize=10)

# Display the graph
plt.show()