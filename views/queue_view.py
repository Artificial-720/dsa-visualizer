import random
import tkinter as tk
from views.base_view import AbstractPage


class QueueView(AbstractPage):

    CANVAS_WIDTH = 400
    CANVAS_HEIGHT = 300
    CANVAS_COLOR_CHECKING = "yellow"
    CANVAS_COLOR_NEUTRAL = "lightblue"

    DATA_MAX = 20
    DATA_MIN = 1

    TITLE = "Queue"
    DESCRIPTION = "Queues organize elements in FIFO First In First Out."

    def __init__(self, parent, controller):
        self.right_x = self.CANVAS_WIDTH - 10
        self.box_height = 100
        self.box_width = 25
        self.y = self.CANVAS_HEIGHT // 2

        self.result_text = tk.StringVar()
        self.queue = [1, 2, 3]
        self.padding = 10  # Bucket padding
        self.queue_max = ((self.CANVAS_WIDTH - (self.padding * 2)) // self.box_width) - 1

        super().__init__(parent, controller)

    def tkraise(self):
        """Override tkraise to draw frame when it loads"""
        super().tkraise()
        self._draw()

    def create_info_frame(self):
        """Implement create_info_frame. Creates and configures the information frame."""
        frame = tk.Frame(self, bg=self.COLOR_BG, pady=10, padx=10)

        tk.Label(frame, text=self.TITLE, font=("Arial", 18)).pack(pady=10, anchor=tk.W)
        tk.Label(frame, text=self.DESCRIPTION, wraplength=500, justify="left").pack(anchor=tk.W)

        # Canvas for drawing the frames
        self.canvas = tk.Canvas(frame, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT, borderwidth=1, relief="solid")
        self.canvas.pack(side=tk.TOP, anchor=tk.W)

        # Result text
        result_frame = tk.Frame(frame, pady=10)
        result_frame.pack(side=tk.TOP, anchor=tk.W)
        tk.Label(result_frame, text="Result: ").pack(side=tk.LEFT)
        tk.Label(result_frame, textvariable=self.result_text).pack(side=tk.LEFT)

        # Button group
        self.create_controls_frame(frame)

        return frame

    def create_controls_frame(self, container):
        """Create control frame with buttons to push, pop, peek, is_empty, and size."""
        controls = tk.Frame(container, bg=self.COLOR_BG)
        controls.pack(anchor=tk.W, expand=True)

        tk.Button(controls, text="enqueue", command=self._enqueue).pack(padx=10, side=tk.LEFT)
        tk.Button(controls, text="dequeue", command=self._dequeue).pack(padx=10, side=tk.LEFT)
        tk.Button(controls, text="peek", command=self._peek).pack(padx=10, side=tk.LEFT)
        tk.Button(controls, text="is_empty", command=self._is_empty).pack(padx=10, side=tk.LEFT)
        tk.Button(controls, text="size", command=self._size).pack(padx=10, side=tk.LEFT)

    def _draw_bucket(self):
        # Draw three lines to represent a "bucket" around the queue
        top_y = self.y - self.padding
        bottom_y = self.y + self.box_width + self.padding
        left_x = self.padding
        right_x = self.right_x

        # Draw bucket lines
        self.canvas.create_line(left_x, top_y, left_x, bottom_y, width=3)      # Left side
        self.canvas.create_line(right_x, top_y, right_x, bottom_y, width=3)    # Right side
        self.canvas.create_line(left_x, bottom_y, right_x, bottom_y, width=3)  # Bottom side

    def _draw(self, highlight=None):
        """Redraw the canvas using data from self.queue"""
        # Clear canvas
        self.canvas.delete("all")

        # Draw "bucket" just to help visualize
        self._draw_bucket()

        # Draw each item in the queue
        for i, item in enumerate(self.queue):
            x0 = self.padding * 2 + (i + 1) * self.box_width
            y0 = self.y - self.padding * 2 - self.box_height // 2
            x1 = x0 - self.box_width
            y1 = y0 + self.box_height

            color = self.CANVAS_COLOR_NEUTRAL
            if i == highlight:
                color = self.CANVAS_COLOR_CHECKING
                # refresh later without color
                self.after(200, self._draw)

            # Draw rectangle and text for each item
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")
            self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(item), font=("Arial", 14))

        self.canvas.update()

    # Queue

    def _enqueue(self):
        if len(self.queue) >= self.queue_max:
            self.result_text.set("Queue is full")
        else:
            elm = random.randint(self.DATA_MIN, self.DATA_MAX)
            self.queue.append(elm)
            self.result_text.set("")
            self._draw(len(self.queue) - 1)

    def _dequeue(self):
        if len(self.queue) == 0:
            self.result_text.set("Queue is empty")
        else:
            elm = self.queue.pop(0)
            self.result_text.set(str(elm))
            self._draw()

    def _peek(self):
        if len(self.queue) == 0:
            self.result_text.set("Queue is empty")
        else:
            elm = self.queue[0]
            self.result_text.set(str(elm))
            self._draw(0)

    def _is_empty(self):
        elm = len(self.queue) == 0
        self.result_text.set(str(elm))

    def _size(self):
        self.result_text.set(str(len(self.queue)))
