import tkinter as tk
from views.base import BaseGraphView


class GraphTraversalView(BaseGraphView):

    def __init__(self, parent, controller):
        self.title = "Graph Traversal"
        self.description = "Graph traversal means starting at a vertex and go along edges to visit other vertices."

        self.setup_test_graph()

        super().__init__(parent, controller)

    def setup_test_graph(self):
        # self.vertex_data = ['A', 'B', 'C', 'D']

        # self.adjacency_matrix = [
        #     [0, 1, 1, 1],  # Edges for A
        #     [1, 0, 1, 0],  # Edges for B
        #     [1, 1, 0, 0],  # Edges for C
        #     [1, 0, 0, 0]   # Edges for D
        # ]

        self.vertex_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.adjacency_matrix = [
            [0, 0, 1, 1, 1, 0, 0],  # A (vertex 0)
            [0, 0, 1, 0, 0, 1, 0],  # B (vertex 1)
            [1, 1, 0, 0, 1, 1, 1],  # C (vertex 2)
            [1, 0, 0, 0, 0, 0, 0],  # D (vertex 3)
            [1, 0, 1, 0, 0, 0, 0],  # E (vertex 4)
            [0, 1, 1, 0, 0, 0, 0],  # F (vertex 5)
            [0, 0, 1, 0, 0, 0, 0],  # G (vertex 6)
        ]

    def create_controls_frame(self, parent):
        controls_frame = tk.Frame(parent)
        # Frame to results label
        result_frame = tk.Frame(controls_frame)
        result_frame.pack()
        # label for output
        tk.Label(result_frame, text="Results: ").pack(side=tk.LEFT)
        self.label = tk.Label(result_frame, text="")
        self.label.pack(pady=10, anchor=tk.W)

        # Buttons
        button_frame = tk.Frame(controls_frame)
        button_frame.pack()
        self.btn1 = tk.Button(button_frame, text="DFS Traversal from D", command=self.dfs_traversal_button)
        self.btn1.grid(row=0, column=0, padx=10)
        self.btn2 = tk.Button(button_frame, text="BFS Traversal from D", command=self.bfs_traversal_button)
        self.btn2.grid(row=0, column=1, padx=10)
        return controls_frame

    def set_button_state(self, state):
        self.btn1.config(state=state)
        self.btn2.config(state=state)

    def dfs_traversal_button(self):
        self.animate(self.dfs_traversal_generator('D'))

    def dfs_traversal_generator(self, start_value):
        # Result: D,A,C,B,F,E,G
        index = self.vertex_data.index(start_value)
        n = len(self.vertex_data)
        visited = [False] * n

        stack = [index]
        checked = []
        while stack:
            current = stack.pop()
            if not visited[current]:
                visited[current] = True
                yield [current], checked
                checked.append(current)
                self.label["text"] += f"{self.vertex_data[current]} "

                for i in range(n - 1, -1, -1):
                    if self.adjacency_matrix[current][i] == 1 and not visited[i]:
                        stack.append(i)
        yield [], checked

    def bfs_traversal_button(self):
        self.animate(self.bfs_traversal_generator('D'))

    def bfs_traversal_generator(self, start_value):
        # Result: D,A,C,E,B,F,G
        start_index = self.vertex_data.index(start_value)
        n = len(self.vertex_data)
        visited = [False] * n

        queue = [start_index]
        checked = []
        while queue:
            current = queue.pop(0)
            if not visited[current]:
                visited[current] = True
                yield [current], checked
                checked.append(current)
                self.label["text"] += f"{self.vertex_data[current]} "

                for i in range(n):
                    if self.adjacency_matrix[current][i] == 1 and not visited[i]:
                        queue.append(i)
        yield [], checked
