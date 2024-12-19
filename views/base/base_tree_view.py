import tkinter as tk
from views.base import AbstractPage


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


class BaseTreeView(AbstractPage):

    CANVAS_WIDTH = 400
    CANVAS_HEIGHT = 400

    def __init__(self, parent, controller):
        self.animation_delay = 500
        self.node_diameter = 30
        self.offset_x = 60
        self.offset_y = 60

        self.node_radius = self.node_diameter / 2

        self.color_checked = "SpringGreen"
        self.color_checking = "LimeGreen"
        self.color_neutral = "LightBlue"

        super().__init__(parent, controller)

    def tkraise(self):
        """Override tkraise to draw frame when it loads"""
        super().tkraise()
        self.draw()

    def create_info_frame(self):
        """Implement create_info_frame. Creates and configures the information frame."""
        frame = tk.Frame(self, bg=self.COLOR_BG, pady=10, padx=10)

        tk.Label(frame, text=self.title, font=("Arial", 18)).pack(pady=10, anchor=tk.W)
        tk.Label(frame, text=self.description, wraplength=500, justify="left").pack(anchor=tk.W)

        # Canvas for drawing the frames
        self.canvas = tk.Canvas(frame, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT, borderwidth=1, relief="solid")
        self.canvas.pack(anchor=tk.W)

        self.create_controls_frame(frame).pack(anchor=tk.W)

        return frame

    def create_controls_frame(self, parent):
        raise NotImplementedError

    def animate(self, gen):
        """Animate algorithm by updating the canvas."""
        if hasattr(self, 'label'):
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
            color = self.color_neutral
            if queue_object.node in checking:
                color = self.color_checking
            if queue_object.node in checked:
                color = self.color_checked
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
