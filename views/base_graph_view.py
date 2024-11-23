import random
import math
import tkinter as tk
from views.base_view import AbstractPage


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Point(self.x / scalar, self.y / scalar)

    def magnitude(self):
        """Returns the magnitude of the vector."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        """Returns a normalized vector (unit vector)."""
        mag = self.magnitude()
        if mag == 0:  # prevent ZeroDivisionError
            return Point(1, 1)
        return self / mag

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)


class BaseGraphView(AbstractPage):

    CANVAS_WIDTH = 400
    CANVAS_HEIGHT = 400

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.node_diameter = 50
        self.node_radius = self.node_diameter // 2

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

    def normalize(self, vec):
        length = math.sqrt(vec.x**2 + vec.y**2)
        if length == 0:
            return Point(1, 1)
        return Point((vec.x / length), (vec.y / length))

    def draw(self, checking=[], checked=[]):
        self.vertex_data = ['A', 'B', 'C', 'D']

        self.adjacency_matrix = [
            [0, 1, 1, 1],  # Edges for A
            [1, 0, 1, 0],  # Edges for B
            [1, 1, 0, 0],  # Edges for C
            [1, 0, 0, 0]   # Edges for D
        ]

        # Clear canvas
        self.canvas.delete("all")

        # Graph is empty
        if not self.adjacency_matrix or not self.vertex_data:
            return

        start_x = self.canvas.winfo_width() // 2
        start_y = self.canvas.winfo_height() // 2

        x, y = start_x, start_y
        color = "green"

        # Calculate node locations
        n = len(self.vertex_data)
        self.force = 10
        self.min_distance = 100
        locations = [Point(start_x, start_y) for _ in range(n)]

        max_interations = 50

        for _ in range(max_interations):
            print("Physics step")
            changed = False
            for i in range(n):
                for j in range(n):
                    p1 = locations[i]
                    if i == j:  # Skip self
                        continue
                    p2 = locations[j]
                    dis = p1.distance(p2)
                    print(f"Distance between {p1} and {p2} is {dis}")
                    if dis < self.min_distance:
                        if dis == 0:
                            direction_vector = Point(random.randint(0, 10), random.randint(0, 10))
                        else:
                            direction_vector = p1 - p2
                        direction_vector_norm = direction_vector.normalize()
                        print(f"direction vec {direction_vector}")
                        new_p1 = p1 + (direction_vector_norm * self.force)
                        locations[i] = new_p1
                        changed = True
                        print(f"Moved {i} from {p1} to {new_p1}")
            if not changed:
                break  # stop interations if positions have stabalized

        # Draw nodes
        for i in range(n):
            p = locations[i]
            # Draw circle
            self.canvas.create_oval(p.x, p.y, p.x + self.node_diameter, p.y + self.node_diameter, fill=color)
            # Draw text
            self.canvas.create_text(p.x + self.node_radius, p.y + self.node_radius, text=self.vertex_data[i])

        # Draw edges
        for i in range(n):
            for j in range(n):
                if self.adjacency_matrix[i][j] == 1:
                    print(f"Draw connection from {self.vertex_data[i]} to {self.vertex_data[j]}")
                    p1 = locations[i]
                    p2 = locations[j]
                    print(p1)
                    # Move to center of node
                    p1_center = Point(p1.x + self.node_radius, p1.y + self.node_radius)
                    p2_center = Point(p2.x + self.node_radius, p2.y + self.node_radius)
                    # convert points into a direction vector
                    d_v = p1_center - p2_center
                    d_v = d_v.normalize()
                    # Find edge
                    p1_edge = p1_center + (d_v * -self.node_radius)  # Negative cause want to flip direction
                    p2_edge = p2_center + (d_v * self.node_radius)
                    self.canvas.create_line(p1_edge.x, p1_edge.y, p2_edge.x, p2_edge.y, fill="black")
