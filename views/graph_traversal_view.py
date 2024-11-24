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
        controls_frame = tk.Frame(parent)
        # Frame to results label
        result_frame = tk.Frame(controls_frame)
        result_frame.pack()
        # label for output
        tk.Label(result_frame, text="Results: ").pack(side=tk.LEFT)
        self.label = tk.Label(result_frame, text="")

        # Buttons
        button_frame = tk.Frame(controls_frame)
        button_frame.pack()
        tk.Button(button_frame, text="DFS Traversal", command=self.dfs_traversal_button).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="BFS Traversal", command=self.bfs_traversal_button).grid(row=0, column=1, padx=10)
        return controls_frame

    def dfs_traversal_button(self):
        pass

    def bfs_traversal_button(self):
        pass
