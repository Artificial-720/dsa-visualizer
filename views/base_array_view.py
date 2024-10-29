import time
import random
import tkinter as tk
from views.base_view import AbstractPage


class BaseArrayView(AbstractPage):

    CANVAS_WIDTH = 400
    CANVAS_HEIGHT = 300
    CANVAS_COLOR_CHECKING = "red"
    CANVAS_COLOR_COMPLETED = "green"
    CANVAS_COLOR_NEUTRAL = "gray"

    DATA_SIZE = 20
    DATA_MAX = 100
    DATA_MIN = 1

    BAR_SPACING = 2
    SPEED_MAX = 1
    SPEED_MIN = 500
    SPEED_DEFAULT = 25
    COUNT_MAX = 5
    COUNT_MIN = 50
    COUNT_DEFAULT = 15

    TITLE = ""
    DESCRIPTION = ""

    def tkraise(self):
        """Override tkraise to reset animation when loading frame"""
        super().tkraise()
        self._reset()

    def create_info_frame(self):
        """Implement create_info_frame. Creates and configures the information frame."""
        frame = tk.Frame(self, bg=self.COLOR_BG, pady=10, padx=10)

        tk.Label(frame, text=self.TITLE, font=("Arial", 18)).pack(pady=10, anchor=tk.W)
        tk.Label(frame, text=self.DESCRIPTION, wraplength=500, justify="left").pack(anchor=tk.W)

        # Canvas and count scale frame
        canvas_count_frame = tk.Frame(frame, bg=self.COLOR_BG)
        canvas_count_frame.pack(anchor=tk.W, expand=True)

        # Canvas for drawing the frames
        self.canvas = tk.Canvas(canvas_count_frame, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT, borderwidth=1, relief="solid")
        self.canvas.pack(side=tk.LEFT)

        # Count scale
        self.count_var = tk.IntVar(value=self.COUNT_DEFAULT)
        self.count_scale = tk.Scale(canvas_count_frame, variable=self.count_var, from_=self.COUNT_MIN, to=self.COUNT_MAX, orient=tk.VERTICAL, label="Count: ")
        self.count_scale.pack(side=tk.LEFT, fill=tk.Y, padx=10)
        self.count_scale.bind("<ButtonRelease-1>", self._on_count_scale_change)

        self.create_controls_frame(frame)

        return frame

    def create_controls_frame(self, container):
        """Create control frame with button to start and speed scale."""
        controls = tk.Frame(container, bg=self.COLOR_BG)
        controls.pack(anchor=tk.W, expand=True)

        self.button = tk.Button(controls, text=self.TITLE, command=self._button_press)
        self.button.pack(side=tk.LEFT)

        self.speed_var = tk.IntVar(value=self.SPEED_DEFAULT)
        self.speed_scale = tk.Scale(controls, variable=self.speed_var, from_=self.SPEED_MIN, to=self.SPEED_MAX, orient=tk.HORIZONTAL, label="Speed:", showvalue=0)
        self.speed_scale.pack(side=tk.LEFT, padx=10)

        return controls

    def _on_count_scale_change(self, event):
        """Handle click on scale for count"""
        self._reset()

    def _draw_bars(self, checking=[], completed=[]):
        """
        Draws bars on a canvas
        changing colors for checking and completed indices
        """
        # Clear
        self.canvas.delete("all")

        canvas_height = self.canvas.winfo_height()
        max_value = max(self.data)
        bar_width = self.CANVAS_WIDTH // len(self.data)

        for i, value in enumerate(self.data):
            x0 = i * bar_width + self.BAR_SPACING
            y0 = canvas_height - (value / max_value) * canvas_height
            x1 = (i + 1) * bar_width
            y1 = canvas_height

            color = self.CANVAS_COLOR_NEUTRAL
            if i in checking:
                color = self.CANVAS_COLOR_CHECKING
            elif i in completed:
                color = self.CANVAS_COLOR_COMPLETED
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        self.canvas.update()

    def _button_press(self):
        """Handle button press for starting or resetting animation."""
        if self.animation_finished:
            self._reset()
        else:
            self._start()

    def _start(self):
        """Start algorithm animation and disable button."""
        self.button.config(state="disabled")
        self._animate()

    def _reset(self):
        """Reset data, animation state, and button text, then draw initial data."""
        self.animation_finished = False
        self.data = self._generate_data()
        self.button.config(text=self.TITLE)
        self._draw_bars()

    def _generate_data(self):
        """Generate random data into self.data"""
        return [random.randint(self.DATA_MIN, self.DATA_MAX) for _ in range(self.count_var.get())]

    def _animate(self):
        """Animate algorithm by updating the canvas."""
        for checking, completed in self.algorithm_generator():
            self._draw_bars(checking, completed)
            time.sleep(self.speed_var.get() / 1000)

        self.button.config(text="Reset", state="active")
        self.animation_finished = True

    def algorithm_generator(self):
        """Yield steps for the algorithm. This method should be implemented by subclasses."""
        raise NotImplementedError
