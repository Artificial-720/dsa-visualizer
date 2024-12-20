import tkinter as tk
from views.base import BaseGraphView


class GraphShortestPathBellmanFordView(BaseGraphView):

    # Need more room to show all the nodes with this graph
    CANVAS_WIDTH = 600
    CANVAS_HEIGHT = 600

    def __init__(self, parent, controller):
        self.title = "Bellman Ford Algorithm"
        self.description = "Bellman Ford algorithm finds the shortest path from one node to all other nodes. With one or more negative edge weights."

        self.setup_test_graph()

        super().__init__(parent, controller)

        # Need more room to show all the nodes
        self.node_diameter = 25
        self.node_radius = self.node_diameter // 2

    def setup_test_graph(self):
        self.vertex_data = ['A', 'B', 'C', 'D', 'E']
        self.adjacency_matrix = [
            # A  B  C  D  E
            [0, 0, 4, 0, 5],  # A (vertex 0)
            [0, 0, -4, 0, 0],  # B (vertex 1)
            [-3, 0, 0, 0, 0],  # C (vertex 2)
            [4, 0, 7, 0, 3],  # D (vertex 3)
            [0, 2, 3, 0, 0],  # E (vertex 4)
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
        self.button = tk.Button(button_frame, text="Run Bellman's", command=self.bellman_button)
        self.button.grid(row=0, column=0, padx=10)
        return controls_frame

    def bellman_button(self):
        self.animate(self.bellman_generator())

    def bellman_generator(self):
        n = len(self.vertex_data)
        start_vertex = 3
        distances = [float('inf')] * n
        distances[start_vertex] = 0

        for i in range(n - 1):
            for current in range(n):
                for v in range(n):
                    if self.adjacency_matrix[current][v] != 0:
                        if distances[current] + self.adjacency_matrix[current][v] < distances[v]:
                            # Distance is less this path
                            distances[v] = distances[current] + self.adjacency_matrix[current][v]
                            # Setting distance to data so that its drawn
                            self.vertex_data[v] = distances[v]
                            yield [current, v], []

        # return distances

        self.label["text"] += "Done"

        yield [], [i for i in range(n)]
