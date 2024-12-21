import tkinter as tk
from views.base import BaseGraphView


class GraphCycleDetectionUndirectedView(BaseGraphView):

    def __init__(self, parent, controller):
        self.title = "Graph Cycle Detection using DFS on undirected graph"
        self.description = "A cycle in a Graph is a path that starts and ends at the same vertex"

        self.setup_test_graph()

        super().__init__(parent, controller)

    def setup_test_graph(self):
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
        tk.Label(result_frame, text="Is cyclic: ").pack(side=tk.LEFT)
        self.label = tk.Label(result_frame, text="")
        self.label.pack(pady=10, anchor=tk.W)

        # Buttons
        button_frame = tk.Frame(controls_frame)
        button_frame.pack()
        self.button = tk.Button(button_frame, text="DFS Cycle Detection", command=self.dfs_cycle_button)
        self.button.grid(row=0, column=0, padx=10)
        return controls_frame

    def dfs_cycle_button(self):
        self.animate(self.dfs_cycle_generator())

    def dfs_cycle_generator(self):
        n = len(self.vertex_data)
        visited = [False] * n
        path = [False] * n
        checked = []

        def dfs(node_index):
            stack = [(node_index, -1)]
            while stack:
                current, parent = stack.pop()
                if path[current]:
                    # Cycle Found
                    yield [current], checked
                    return True

                if not visited[current]:
                    visited[current] = True
                    path[current] = True
                    yield [current], checked
                    checked.append(current)

                    for i in range(n - 1, -1, -1):
                        if self.adjacency_matrix[current][i] == 1 and i != parent:
                            stack.append((i, current))
            path[current] = False
            return False

        result = False
        for i in range(n):
            if not visited[i]:
                result = yield from dfs(i)
                if result:
                    break
        self.label["text"] += str(result)

        yield [], checked
