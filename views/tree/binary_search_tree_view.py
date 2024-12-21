import tkinter as tk
from views.base import BaseTreeView, Node


class BinarySearchTreeView(BaseTreeView):

    def __init__(self, parent, controller):
        self.title = "Binary Search Tree"
        self.description = "A Binary Search Tree (BST) is a tree which each node has a value greater then all values in left sub tree and less than all the values in the right sub tree."

        self.root = None

        self.setup_test_tree()

        super().__init__(parent, controller)

        self.color_checking = "Yellow"

    def setup_test_tree(self):
        self.root = Node(13)
        nodeA = Node(7)
        nodeB = Node(15)
        nodeC = Node(3)
        nodeD = Node(8)
        nodeE = Node(14)
        nodeF = Node(19)
        nodeG = Node(18)

        self.root.left = nodeA
        self.root.right = nodeB

        nodeA.left = nodeC
        nodeA.right = nodeD

        nodeB.left = nodeE
        nodeB.right = nodeF

        nodeF.left = nodeG

    def create_controls_frame(self, container):
        control_frame = tk.Frame(container)

        # label for output
        self.label = tk.Label(control_frame, text="")
        self.label.pack(pady=10, anchor=tk.W)

        # input box for search value
        self.search = tk.IntVar()
        self.search.set(4)
        search_box = tk.Entry(control_frame, textvariable=self.search)
        search_box.pack()

        # Button to start binary search
        self.button = tk.Button(control_frame, text="Binary Search", command=self.binary_search_button)
        self.button.pack()

        return control_frame

    def binary_search_button(self):
        self.animate(self.binary_search_generator(self.root, self.search.get()))

    def binary_search_generator(self, node, data):
        if node is None:
            return
        self.label["text"] = ""

        current = node
        found = []
        while current:
            yield [current], []
            if data == current.data:
                found.append(current)
                break
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        if found:
            self.label["text"] = "Found"
        else:
            self.label["text"] = "Not Found"
        yield [], found
