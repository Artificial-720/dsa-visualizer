import tkinter as tk
from views.base import BaseGraphView


class GraphShortestPathDijkstrasView(BaseGraphView):

    # Need more room to show all the nodes with this graph
    CANVAS_WIDTH = 600
    CANVAS_HEIGHT = 600

    def __init__(self, parent, controller):
        self.title = "Dijkstra's Algorithm"
        self.description = "Dijkstra's algorithm finds the shortest path from one node to all other nodes."

        self.setup_test_graph()

        super().__init__(parent, controller)

        # Need more room to show all the nodes
        self.node_diameter = 25
        self.node_radius = self.node_diameter // 2

    def setup_test_graph(self):
        self.vertex_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
        self.adjacency_matrix = [
            # A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R
            [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # A (vertex 0)
            [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # B (vertex 1)
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # C (vertex 2)
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # D (vertex 3)
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # E (vertex 4)
            [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # F (vertex 5)
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # G (vertex 6)
            [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # H (vertex 7)
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # I (vertex 8)
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # J (vertex 9)
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # K (vertex 10)
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # L (vertex 11)
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # M (vertex 12)
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],  # N (vertex 13)
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],  # O (vertex 14)
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],  # P (vertex 15)
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],  # Q (vertex 16)
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # R (vertex 17)
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
        tk.Button(button_frame, text="Run Dijkstra's", command=self.dijkstra_button).grid(row=0, column=0, padx=10)
        return controls_frame

    def dijkstra_button(self):
        self.animate(self.dijkstra_generator())

    def dijkstra_generator(self):
        n = len(self.vertex_data)
        start_vertex = 3
        distances = [float('inf')] * n
        distances[start_vertex] = 0
        visited = [False] * n

        checked = []

        for _ in range(n):
            min = float('inf')
            current = None
            for i in range(n):
                if not visited[i] and distances[i] < min:
                    min = distances[i]
                    current = i
            if current is None:
                # No next vertex alg is done
                break

            visited[current] = True
            checked.append(current)

            # Update distances for not visted vertex
            for v in range(n):
                if self.adjacency_matrix[current][v] != 0 and not visited[v]:
                    yield [v], checked
                    alt = distances[current] + self.adjacency_matrix[current][v]
                    if alt < distances[v]:
                        distances[v] = alt
                        self.vertex_data[v] = alt

            yield [], checked

        # return distances

        self.label["text"] += "Done"

        yield [], checked
