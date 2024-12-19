import tkinter as tk
from views.base import BaseGraphView


class GraphCycleDetectionDirectedView(BaseGraphView):

    def __init__(self, parent, controller):
        self.title = "Graph Cycle Detection using DFS on directed graph"
        self.description = "A cycle in a Graph is a path that starts and ends at the same vertex"

        self.setup_test_graph()

        super().__init__(parent, controller)

    def setup_test_graph(self):
        self.vertex_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.adjacency_matrix = [
            [0, 0, 1, 0, 0, 0, 0],  # A (vertex 0)
            [0, 0, 0, 0, 0, 1, 0],  # B (vertex 1)
            [0, 1, 0, 0, 1, 0, 1],  # C (vertex 2)
            [1, 0, 0, 0, 0, 0, 0],  # D (vertex 3)
            [1, 0, 0, 0, 0, 0, 0],  # E (vertex 4)
            [0, 0, 0, 0, 0, 0, 0],  # F (vertex 5)
            [0, 0, 0, 0, 0, 0, 0],  # G (vertex 6)
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
        tk.Button(button_frame, text="DFS Cycle Detection", command=self.dfs_cycle_button).grid(row=0, column=0, padx=10)
        return controls_frame

    def dfs_cycle_button(self):
        self.animate(self.dfs_cycle_generator())

    def dfs_cycle_generator(self):
        n = len(self.vertex_data)
        visited = [False] * n
        path = [False] * n
        checked = []

        def dfs(node_index):
            stack = [(node_index, iter(range(n)))]
            path[node_index] = True

            while stack:
                current, neighbors = stack[-1]
                if not visited[current]:
                    visited[current] = True
                    yield [current], checked
                    checked.append(current)

                for neighbor in neighbors:
                    if self.adjacency_matrix[current][neighbor] == 1:
                        if path[neighbor]:
                            # Cycle Found
                            yield [neighbor], checked
                            return True
                        if not visited[neighbor]:
                            stack.append((neighbor, iter(range(n))))
                            path[neighbor] = True
                            break
                else:
                    # Done exploring neighbors of `current` remove from path/stack
                    path[current] = False
                    stack.pop()

            # No Cycle found
            return False

        result = False
        for i in range(n):
            if not visited[i]:
                result = yield from dfs(i)
                if result:
                    break
        self.label["text"] += str(result)

        yield [], checked
