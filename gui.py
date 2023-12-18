import tkinter as tk

class GraphGUI:
    def __init__(self, master, graph):
        self.master = master
        self.master.title("Graph GUI")

        self.graph = graph

        # Canvas for drawing the graph
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="white")
        self.canvas.pack()

        self.draw_graph()

    def draw_graph(self):
        node_positions = self.calculate_node_positions()

        for node, neighbors in self.graph.items():
            x, y = node_positions[node]
            self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="blue", outline="black")
            self.canvas.create_text(x, y - 15, text=node, fill="black")

            for neighbor in neighbors:
                x1, y1 = node_positions[node]
                x2, y2 = node_positions[neighbor]
                self.canvas.create_line(x1, y1, x2, y2, fill="black")

    def calculate_node_positions(self):
        # Hardcoded node positions for simplicity
        return {
            'a': (50, 50),
            'b': (200, 50),
            'c': (350, 50),
            'd': (50, 200),
            'e': (200, 200),
            'f': (350, 200),
            'g': (50, 350),
            'h': (200, 350)
        }

if __name__ == "__main__":
    graph = {
        'a': ['c', 'b'],
        'b': ['c', 'a'],
        'c': ['a', 'c','d', 'e'],
        'd': ['c', 'f'],
        'e': ['c', 'f', 'h'],
        'f': ['d', 'e', 'g', 'h'],
        'g': ['f', 'h'],
        'h': ['e', 'f', 'g']
    }

    root = tk.Tk()
    app = GraphGUI(root, graph)
    root.mainloop()
