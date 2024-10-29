import random
import tkinter as tk
from views.base_view import AbstractPage


class StackView(AbstractPage):

    CANVAS_WIDTH = 400
    CANVAS_HEIGHT = 300
    CANVAS_COLOR_CHECKING = "yellow"
    CANVAS_COLOR_NEUTRAL = "lightblue"

    DATA_MAX = 20
    DATA_MIN = 1

    TITLE = "Stack"
    DESCRIPTION = "Stacks organize elements in LIFO Last In First Out."

    def __init__(self, parent, controller):
        self.stack_bottom_y = self.CANVAS_HEIGHT - 10  # Y position of the bottom of stack
        self.box_height = 25    # Height of each stack item box
        self.x = 50
        self.box_width = 100

        self.result_text = tk.StringVar()
        self.stack = [1, 2, 3]
        self.padding = 10  # Bucket padding
        self.stack_max = (self.CANVAS_HEIGHT // self.box_height) - 1

        super().__init__(parent, controller)

    def tkraise(self):
        """Override tkraise to draw frame when it loads"""
        super().tkraise()
        self._draw_stack()

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

        tk.Button(controls, text="push", command=self._push).pack(padx=10, side=tk.LEFT)
        tk.Button(controls, text="pop", command=self._pop).pack(padx=10, side=tk.LEFT)
        tk.Button(controls, text="peek", command=self._peek).pack(padx=10, side=tk.LEFT)
        tk.Button(controls, text="is_empty", command=self._is_empty).pack(padx=10, side=tk.LEFT)
        tk.Button(controls, text="size", command=self._size).pack(padx=10, side=tk.LEFT)

    def _draw_bucket(self):
        # Draw three lines to represent a "bucket" around the stack
        left_x = self.x - self.padding
        right_x = self.x + self.box_width + self.padding
        top_y = self.padding
        bottom_y = self.stack_bottom_y + self.padding

        # Draw bucket lines
        self.canvas.create_line(left_x, top_y, left_x, bottom_y, width=3)      # Left side
        self.canvas.create_line(right_x, top_y, right_x, bottom_y, width=3)    # Right side
        self.canvas.create_line(left_x, bottom_y, right_x, bottom_y, width=3)  # Bottom side

    def _draw_stack(self, highlight=None):
        """Redraw the canvas using data from self.stack"""
        # Clear canvas
        self.canvas.delete("all")

        # Draw stack "bucket" just to help visualize
        self._draw_bucket()

        # Draw each item in the stack
        for i, item in enumerate(self.stack):
            x0, y0 = self.x, self.stack_bottom_y - (i * self.box_height)
            x1, y1 = self.x + self.box_width, y0 - self.box_height

            color = self.CANVAS_COLOR_NEUTRAL
            if i == highlight:
                color = self.CANVAS_COLOR_CHECKING
                # refresh later without color
                self.after(200, self._draw_stack)

            # Draw rectangle and text for each item
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")
            self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(item), font=("Arial", 14))

        self.canvas.update()

    # Stack

    def _push(self):
        if len(self.stack) >= self.stack_max:
            self.result_text.set("Stack is full")
        else:
            elm = random.randint(self.DATA_MIN, self.DATA_MAX)
            self.stack.append(elm)
            self.result_text.set("")
            self._draw_stack(len(self.stack) - 1)

    def _pop(self):
        if len(self.stack) == 0:
            self.result_text.set("Stack is empty")
        else:
            elm = self.stack.pop()
            self.result_text.set(str(elm))
            self._draw_stack()

    def _peek(self):
        if len(self.stack) == 0:
            self.result_text.set("Stack is empty")
        else:
            elm = self.stack[-1]
            self.result_text.set(str(elm))
            self._draw_stack(len(self.stack) - 1)

    def _is_empty(self):
        res = len(self.stack) == 0
        self.result_text.set(str(res))

    def _size(self):
        res = len(self.stack)
        self.result_text.set(str(res))
