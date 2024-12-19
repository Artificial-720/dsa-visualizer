import tkinter as tk
from views.base import BaseGraphView


class GraphMinimumSpanningTreeKruskalView(BaseGraphView):

    # Need more room to show all the nodes with this graph
    CANVAS_WIDTH = 600
    CANVAS_HEIGHT = 600

    def __init__(self, parent, controller):
        self.title = "Kruskal's Algorithm"
        self.description = "Kruskal's algorithm finds the minimum spanning tree of a undirected graph."

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
        tk.Button(button_frame, text="Run Kruskal's", command=self.kruskal_button).grid(row=0, column=0, padx=10)
        return controls_frame

    def kruskal_button(self):
        self.animate(self.kruskal_generator())

    def kruskal_generator(self):
        n = len(self.vertex_data)
        result = []
        i = 0

        edges = []
        # convert adjacency matrix to edge list
        for u in range(n):
            for v in range(u + 1, n):
                if self.adjacency_matrix[u][v] != 0:
                    edges.append((u, v, self.adjacency_matrix[u][v]))

        # sort by weight
        edges = sorted(edges, key=lambda i: i[2])

        parent = []
        rank = []

        for node in range(n):
            parent.append(node)
            rank.append(0)

        while i < len(edges):
            u, v, weight = edges[i]
            i += 1
            yield [], [], result

            # roots of u and v
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                result.append((u, v))
                self.union(parent, rank, x, y)

        self.label["text"] += "Done"

        yield [], [], result

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1
