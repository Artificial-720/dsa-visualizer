import string
import random
import tkinter as tk
from views.base import BaseTreeView, Node


class AVLTreeNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.height = 1


class AVLTreeView(BaseTreeView):

    def __init__(self, parent, controller):
        self.title = "AVL Tree"
        self.description = "A Adelson-Velsky and Evgenii Landis (AVL) are a type of binary tree that are self-balancing."

        self.root = None
        self.letters = list(string.ascii_uppercase)

        super().__init__(parent, controller)

    def create_controls_frame(self, container):
        control_frame = tk.Frame(container, bg="green")

        # Button to start binary search
        self.button = tk.Button(control_frame, text="Insert", command=self.button_event)
        self.button.pack()

        return control_frame

    def button_event(self):
        if not self.letters:
            self.root = None
            self.letters = list(string.ascii_uppercase)
            self.button["text"] = "Insert"
        letter = self.letters.pop(random.randrange(len(self.letters)))
        self.animate(self.insert(letter))
        if not self.letters:
            self.button["text"] = "Reset"

    def insert(self, data):
        # Tree is empty
        if not self.root:
            self.root = AVLTreeNode(data)
            yield [self.root], []
            return

        path_stack = []
        current = self.root
        checked = []

        while True:
            yield [current], checked
            checked.append(current)
            path_stack.append(current)

            if data < current.data:
                if current.left is None:
                    current.left = AVLTreeNode(data)
                    yield [current.left], checked
                    break
                else:
                    current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = AVLTreeNode(data)
                    yield [current.right], checked
                    break
                else:
                    current = current.right
            else:
                # Duplicate value
                yield [], checked
                return

        # Balance the tree
        yield from self.balance_tree(data, path_stack)

    def get_height(self, node):
        return node.height if node else 0

    def update_height(self, node):
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)

        return y

    def balance_tree(self, data, path_stack=[]):
        checked = []
        while path_stack:
            node = path_stack.pop()
            self.update_height(node)
            balance = self.get_balance(node)

            # Left Left Case
            if balance > 1 and data < node.left.data:
                if path_stack:
                    parent = path_stack[-1]
                    if parent.left == node:
                        parent.left = self.rotate_right(node)
                    else:
                        parent.right = self.rotate_right(node)
                else:
                    self.root = self.rotate_right(node)

            # Right Right Case
            elif balance < -1 and data > node.right.data:
                if path_stack:
                    parent = path_stack[-1]
                    if parent.left == node:
                        parent.left = self.rotate_left(node)
                    else:
                        parent.right = self.rotate_left(node)
                else:
                    self.root = self.rotate_left(node)

            # Left Right Case
            elif balance > 1 and data > node.left.data:
                node.left = self.rotate_left(node.left)
                if path_stack:
                    parent = path_stack[-1]
                    if parent.left == node:
                        parent.left = self.rotate_right(node)
                    else:
                        parent.right = self.rotate_right(node)
                else:
                    self.root = self.rotate_right(node)

            # Right Left Case
            elif balance < -1 and data < node.right.data:
                node.right = self.rotate_right(node.right)
                if path_stack:
                    parent = path_stack[-1]
                    if parent.left == node:
                        parent.left = self.rotate_left(node)
                    else:
                        parent.right = self.rotate_left(node)
                else:
                    self.root = self.rotate_left(node)

            # Yield each step for visualization after balancing adjustments
            yield [node], checked

        yield [], checked
