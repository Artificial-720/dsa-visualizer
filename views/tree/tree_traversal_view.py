import tkinter as tk
from views.base import BaseTreeView, Node


class TreeTraversalView(BaseTreeView):

    def __init__(self, parent, controller):
        self.title = "Tree Traversal"
        self.description = "Tree Traversal defines a way to visit each node in a tree. In-order (left, root, right), Pre-order (root, left, right), Post-order (left, right, root)"

        self.root = None

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

    def create_controls_frame(self, parent):
        control_frame = tk.Frame(parent)

        # Frame to results label
        result_frame = tk.Frame(control_frame)
        result_frame.pack()
        # label for output
        tk.Label(result_frame, text="Results: ").pack(side=tk.LEFT)
        self.label = tk.Label(result_frame, text="")
        self.label.pack(pady=10, anchor=tk.W)

        button_frame = tk.Frame(control_frame)
        button_frame.pack()
        # Buttons
        tk.Button(button_frame, text="Pre-order Traversal", command=self.pre_order_traversal_button).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="In-order Traversal", command=self.in_order_traversal_button).grid(row=0, column=1, padx=10)
        tk.Button(button_frame, text="Post-order Traversal", command=self.post_order_traversal_button).grid(row=0, column=2, padx=10)

        return control_frame

    def pre_order_traversal_button(self):
        self.animate(self.pre_order_traversal_generator(self.root))

    def pre_order_traversal_generator(self, node):
        # Result: R,A,C,D,B,E,F,G
        if node is None:
            return

        stack = [node]
        checked = []
        while stack:
            current = stack.pop()
            yield [current], checked
            checked.append(current)
            self.label["text"] += f"{current.data} "

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        yield [], checked

    def in_order_traversal_button(self):
        self.animate(self.in_order_traversal_generator(self.root))

    def in_order_traversal_generator(self, node):
        # Result: C,A,D,R,E,B,G,F
        if node is None:
            return

        stack = []
        current = node
        checked = []
        while stack or current:
            # Go down leftmost branch
            while current:
                if current.left:
                    yield [current], checked
                stack.append(current)
                current = current.left

            current = stack.pop()
            yield [current], checked
            checked.append(current)
            self.label["text"] += f"{current.data} "

            # move to right node
            current = current.right
        yield [], checked

    def post_order_traversal_button(self):
        self.animate(self.post_order_traversal_generator(self.root))

    def post_order_traversal_generator(self, node):
        # Result: C,D,A,E,G,F,B,R
        if node is None:
            return
        current = node
        checked = []
        stack = []
        while current and current not in checked:
            yield [current], checked
            if current.left and current.left not in checked:
                stack.append(current)
                current = current.left
            elif current.right and current.right not in checked:
                stack.append(current)
                current = current.right
            else:
                checked.append(current)
                self.label["text"] += f"{current.data} "
                if stack:
                    temp = stack.pop()
                    if temp == current:
                        temp = stack.pop()
                    current = temp
        yield [], checked
