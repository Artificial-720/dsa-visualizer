import tkinter as tk
from views.base import BaseGraphView


class GraphMinimumSpanningTreePrimsView(BaseGraphView):

    # Need more room to show all the nodes with this graph
    CANVAS_WIDTH = 600
    CANVAS_HEIGHT = 600

    def __init__(self, parent, controller):
        self.title = "Prim's Algorithm"
        self.description = "Prim's algorithm finds the minimum spanning tree of a connected undirected graph."

        self.setup_test_graph()

        super().__init__(parent, controller)

        # Need more room to show all the nodes
        self.node_diameter = 25
        self.node_radius = self.node_diameter // 2

    def setup_test_graph(self):
        self.vertex_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.adjacency_matrix = [
            # A  B  C  D  E  F  G  H
            [0, 4, 0, 3, 0, 0, 0, 0],  # A
            [4, 0, 3, 5, 6, 0, 0, 0],  # B
            [0, 3, 0, 0, 4, 0, 0, 2],  # C
            [3, 5, 0, 0, 7, 4, 0, 0],  # D
            [0, 6, 4, 7, 0, 5, 3, 0],  # E
            [0, 0, 0, 4, 5, 0, 7, 0],  # F
            [0, 0, 0, 0, 3, 7, 0, 5],  # G
            [0, 0, 2, 0, 0, 0, 5, 0]   # H
        ]

    def create_controls_frame(self, parent):
        controls_frame = tk.Frame(parent)
        # Frame to results label
        result_frame = tk.Frame(controls_frame)
        result_frame.pack()
        # label for output
        self.label = tk.Label(result_frame, text="")
        self.label.pack(pady=10, anchor=tk.W)

        # Buttons
        button_frame = tk.Frame(controls_frame)
        button_frame.pack()
        self.button = tk.Button(button_frame, text="Run Prim's", command=self.prim_button)
        self.button.grid(row=0, column=0, padx=10)
        return controls_frame

    def prim_button(self):
        self.animate(self.prim_generator())

    def prim_generator(self):
        n = len(self.vertex_data)
        in_min_tree = [False] * n
        parents = [-1] * n
        values = [float('inf')] * n
        values[0] = 0

        completed = []
        highlight = []

        for _ in range(n):
            # Find vertex with lowest value
            u = None
            min = float('inf')
            for v in range(n):
                if not in_min_tree[v] and values[v] < min:
                    min = values[v]
                    u = v

            if u is None:
                # no more vertices to include
                break

            in_min_tree[u] = True
            completed.append(u)

            if parents[u] != -1:
                # has parent add to tree
                highlight.append((parents[u], u))

            yield [], completed, highlight

            for v in range(n):
                if 0 < self.adjacency_matrix[u][v] < values[v] and not in_min_tree[v]:
                    values[v] = self.adjacency_matrix[u][v]
                    parents[v] = u
                    yield [u, v], completed, highlight

        self.label["text"] += "Done"

        yield [], completed, highlight
