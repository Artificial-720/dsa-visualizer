"""
# Tree Data Structure v0.5.0

Binary Trees
Pre-order Traversal
In-order Traversal
Post-order Traversal
Binary search tree
AVL tree <- self balancing tree

PAGE - Tree Traversal
[canvas]
Result label
buttons {Pre-order Traverse, in order, post order}

colors needed:
checking: solid green
checked: faded green
not checked: gray

PAGE - Binary Search Tree
[canvas]
input box
button [search]

colors need:
checking: yellow
found: green

PAGE - AVL Tree
[canvas]
button [insert {}]
"""
import random
import tkinter as tk
from views.base_view import AbstractPage


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class TreeTraversalView(AbstractPage):

    CANVAS_WIDTH = 600
    CANVAS_HEIGHT = 200

    DATA_MIN = 1
    DATA_MAX = 20

    def __init__(self, parent, controller):
        self.root = None

        self.node_width = 20
        self.node_height = 20
        self.offset = 50

        self.setup_test_tree()

        super().__init__(parent, controller)

    def setup_test_tree(self):
        self.root = Node('R')
        nodeA = Node('A')
        nodeB = Node('B')
        nodeC = Node('C')
        nodeD = Node('D')
        nodeE = Node('E')
        nodeF = Node('F')
        nodeG = Node('G')

        self.root.left = nodeA
        self.root.right = nodeB

        nodeA.left = nodeC
        nodeA.right = nodeD

        nodeB.left = nodeE
        nodeB.right = nodeF

        nodeF.left = nodeG

    def tkraise(self):
        """Override tkraise to draw frame when it loads"""
        super().tkraise()
        self.draw()

    def create_info_frame(self):
        """Implement create_info_frame. Creates and configures the information frame."""
        frame = tk.Frame(self, bg=self.COLOR_BG, pady=10, padx=10)
        self.canvas = tk.Canvas(frame, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT, bg="white")
        self.canvas.pack(pady=20)

        # Frame to results label
        result_frame = tk.Frame(frame)
        result_frame.pack()

        # label for output
        self.label = tk.Label(result_frame, text="")
        self.label.pack(pady=10, anchor=tk.W)

        # Frame to hold buttons
        button_frame = tk.Frame(frame)
        button_frame.pack()

        # Buttons
        tk.Button(button_frame, text="Pre-order Traversal", command=self.pre_order_traversal).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="In-order Traversal", command=self.in_order_traversal).grid(row=0, column=1, padx=10)
        tk.Button(button_frame, text="Post-order Traversal", command=self.post_order_traversal).grid(row=0, column=2, padx=10)

        return frame

    def draw(self):
        # Clear canvas
        self.canvas.delete("all")

        total_width = (self.node_count - 1) * self.offset + self.node_width

        start_x = (self.canvas.winfo_width() - total_width) // 2
        x, y = start_x, self.canvas.winfo_height() // 2 - self.node_height / 2

        # Draw each node
        n = self.head
        while n:
            # Draw circle
            self.canvas.create_oval(x, y, x + self.node_width, y + self.node_height, fill="lightblue")
            # Draw text
            self.canvas.create_text(x + self.node_width / 2, y + self.node_height / 2, text=n.data)

            # Draw line to next node
            if n.next:
                next_x = x + self.offset
                # Line from the center-right of the current node to the center-left of the next node
                self.canvas.create_line(x + self.node_width,
                                        y + self.node_height / 2,
                                        next_x,
                                        y + self.node_height / 2, arrow="last")

            x += self.offset
            n = n.next

    def generate_data(self):
        return random.randint(self.DATA_MIN, self.DATA_MAX)

    def pre_order_traversal(self):
        print("pre_order_traversal")

    def in_order_traversal(self):
        print("in_order_traversal")

    def post_order_traversal(self):
        print("post_order_traversal")
