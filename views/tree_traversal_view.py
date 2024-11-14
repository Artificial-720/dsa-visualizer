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
import tkinter as tk
from views.base_view import AbstractPage


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class QueueObject():
    """ Object used for holding data in queue during draw loop """

    def __init__(self, node, x, y, offset_x):
        self.node = node
        self.x = x
        self.y = y
        self.offset_x = offset_x


class TreeTraversalView(AbstractPage):

    CANVAS_WIDTH = 400
    CANVAS_HEIGHT = 400

    def __init__(self, parent, controller):
        self.root = None

        self.animation_delay = 500
        self.node_diameter = 30
        self.offset_x = 60
        self.offset_y = 60

        self.node_radius = self.node_diameter / 2
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
        tk.Label(result_frame, text="Results: ").pack(side=tk.LEFT)
        self.label = tk.Label(result_frame, text="")
        self.label.pack(pady=10, anchor=tk.W)

        # Frame to hold buttons
        button_frame = tk.Frame(frame)
        button_frame.pack()

        # Buttons
        tk.Button(button_frame, text="Pre-order Traversal", command=self.pre_order_traversal_button).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="In-order Traversal", command=self.in_order_traversal_button).grid(row=0, column=1, padx=10)
        tk.Button(button_frame, text="Post-order Traversal", command=self.post_order_traversal_button).grid(row=0, column=2, padx=10)

        return frame

    def draw(self, checking=[], checked=[]):
        # Clear canvas
        self.canvas.delete("all")

        # Tree is empty
        if not self.root:
            return

        start_x = (self.canvas.winfo_width() // 2) - self.node_radius
        x, y = start_x, 10

        q = []
        q.append(QueueObject(self.root, x, y, self.offset_x))
        while len(q) > 0:
            queue_object = q.pop(0)
            x, y = queue_object.x, queue_object.y
            """
            checking: solid green
            checked: faded green
            not checked: gray
            """
            color = "LightBlue"
            if queue_object.node in checking:
                color = "LimeGreen"
            if queue_object.node in checked:
                color = "SpringGreen"
            # Draw circle
            self.canvas.create_oval(x, y, x + self.node_diameter, y + self.node_diameter, fill=color)
            # Draw text
            self.canvas.create_text(x + self.node_radius, y + self.node_radius, text=queue_object.node.data)

            y += self.offset_y

            def calc_edge(point, multiple=1):
                return (point + self.node_radius) + self.node_radius * 0.707106781 * multiple
            # Draw left node
            if queue_object.node.left:
                left_object = QueueObject(queue_object.node.left, x - queue_object.offset_x, y, queue_object.offset_x // 2)
                q.append(left_object)
                # Draw line
                self.canvas.create_line(calc_edge(queue_object.x, -1),
                                        calc_edge(queue_object.y),
                                        calc_edge(left_object.x),
                                        calc_edge(left_object.y, -1),
                                        arrow="last")
            # Draw right node
            if queue_object.node.right:
                right_object = QueueObject(queue_object.node.right, x + queue_object.offset_x, y, queue_object.offset_x // 2)
                q.append(right_object)
                # Draw line
                self.canvas.create_line(calc_edge(queue_object.x),
                                        calc_edge(queue_object.y),
                                        calc_edge(right_object.x, -1),
                                        calc_edge(right_object.y, -1),
                                        arrow="last")

    def animate(self, gen):
        """Animate algorithm by updating the canvas."""
        self.label["text"] = ""

        def step():
            try:
                checking, checked = next(gen)
                self.draw(checking, checked)
                self.after(self.animation_delay, step)
            except StopIteration:
                self.animation_finished = True

        # Inital start of animation
        step()

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
