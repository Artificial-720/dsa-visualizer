import random
import tkinter as tk
from views.base_view import AbstractPage


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListView(AbstractPage):

    CANVAS_WIDTH = 600
    CANVAS_HEIGHT = 200

    DATA_MIN = 1
    DATA_MAX = 20

    def __init__(self, parent, controller):
        self.head = None
        self.node_count = 0

        self.node_width = 20
        self.node_height = 20
        self.offset = 50
        self.max_length = self.CANVAS_WIDTH // self.offset

        self.index = tk.IntVar()
        self.index.set(2)

        super().__init__(parent, controller)

    def tkraise(self):
        """Override tkraise to draw frame when it loads"""
        super().tkraise()
        self.draw()

    def create_info_frame(self):
        """Implement create_info_frame. Creates and configures the information frame."""
        frame = tk.Frame(self, bg=self.COLOR_BG, pady=10, padx=10)
        self.canvas = tk.Canvas(frame, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT, bg="white")
        self.canvas.pack(pady=20)

        # Frame to hold input box and result text
        control_frame = tk.Frame(frame)
        control_frame.pack()

        # label for output
        self.label = tk.Label(control_frame, text="")
        self.label.pack(pady=10, anchor=tk.W)

        # input box for index value
        index_box = tk.Entry(control_frame, textvariable=self.index)
        index_box.pack()

        # Frame to hold buttons
        button_frame = tk.Frame(frame)
        button_frame.pack()

        # Buttons
        tk.Button(button_frame, text="Add Node Head", command=lambda: self.add_node(0)).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Add Node Tail", command=lambda: self.add_node(self.node_count)).grid(row=0, column=1, padx=10)
        tk.Button(button_frame, text="Add Node Index", command=lambda: self.add_node(self.index.get())).grid(row=0, column=2, padx=10)

        tk.Button(button_frame, text="Remove Node Head", command=lambda: self.remove_node(0)).grid(row=1, column=0, padx=10)
        tk.Button(button_frame, text="Remove Node Tail", command=lambda: self.remove_node(self.node_count - 1)).grid(row=1, column=1, padx=10)
        tk.Button(button_frame, text="Remove Node Index", command=lambda: self.remove_node(self.index.get())).grid(row=1, column=2, padx=10)

        # self.delete_button = tk.Button(button_frame, text="Delete Node", command=self.delete_node)
        # self.delete_button.grid(row=0, column=1, padx=10)

        # self.reset_button = tk.Button(button_frame, text="Reset List", command=self.reset_list)
        # self.reset_button.grid(row=0, column=2, padx=10)

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

    def add_node(self, index=None, data=None):
        """Add a new node to the linked list and update the visualization."""
        if self.node_count >= self.max_length:
            self.label["text"] = "List is full"
            return

        i = index if index is not None else self.node_count
        j = 0

        if index < 0 or index > self.node_count:
            self.label["text"] = f"Please enter a number between 0-{self.node_count}"
            return

        new_data = data if data is not None else self.generate_data()
        new_node = Node(new_data)

        if i == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            n = self.head
            for j in range(i - 1):
                if n is not None:
                    n = n.next

            # Insert new node
            new_node.next = n.next
            n.next = new_node

        self.node_count += 1
        self.draw()

    def remove_node(self, index=None):
        """Delete node from linked list and update the visulization."""
        if self.node_count <= 0:
            self.label["text"] = "List is empty"
            return
        if index < 0 or index > self.node_count:
            self.label["text"] = f"Please enter a number between 0-{self.node_count}"
            return
        # If removing the head (index 0)
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for j in range(index - 1):
                current = current.next

            if current.next:
                current.next = current.next.next

        self.node_count -= 1
        self.draw()
