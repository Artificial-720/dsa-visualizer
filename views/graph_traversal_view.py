import tkinter as tk
from views.base_graph_view import BaseGraphView


class GraphTraversalView(BaseGraphView):

    def __init__(self, parent, controller):
        self.title = "Graph Traversal"
        self.description = "Graph traversal means starting at a vertex and go along edges to visit other vertices."

        self.setup_test_graph()

        super().__init__(parent, controller)

    def setup_test_graph(self):
        self.vertex_data = ['A', 'B', 'C', 'D']

        self.adjacency_matrix = [
            [0, 1, 1, 1],  # Edges for A
            [1, 0, 1, 0],  # Edges for B
            [1, 1, 0, 0],  # Edges for C
            [1, 0, 0, 0]   # Edges for D
        ]

    def create_controls_frame(self, parent):
        controls_frame = tk.Frame()
        # Result label
        # DFS button
        # BFS button
        return controls_frame
