import time
import random
import tkinter as tk
from views.base_view import AbstractPage


class BaseSortView(AbstractPage):

    CANVAS_WIDTH = 400
    CANVAS_HEIGHT = 300
    DATA_SIZE = 20

    TITLE = ""
    DESCRIPTION = ""

    def tkraise(self):
        # Override
        super().tkraise()
        # waiting until drawn on the screen before drawing bars
        self._reset_sort()

    def create_info_frame(self):
        # Override
        frame = tk.Frame(self, bg="blue", pady=10, padx=10)
        title = tk.Label(frame, text=self.TITLE, font=("Arial", 18))
        title.pack(pady=10, anchor=tk.W)

        description = tk.Label(frame, text=self.DESCRIPTION)
        description.pack(anchor=tk.W)

        canvas_count_frame = tk.Frame(frame, bg="green")
        canvas_count_frame.pack(anchor=tk.W, expand=True)

        self.canvas = tk.Canvas(canvas_count_frame, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT, borderwidth=1, relief="solid")
        self.canvas.pack(side=tk.LEFT)

        self.count_var = tk.IntVar()
        self.count_var.set(15)
        self.count_scale = tk.Scale(canvas_count_frame, variable=self.count_var, from_=50, to=5, orient=tk.VERTICAL, label="Count: ")
        self.count_scale.pack(side=tk.LEFT, fill=tk.Y, padx=10)
        self.count_scale.bind("<ButtonRelease-1>", lambda e: self._reset_sort())

        controls = tk.Frame(frame, bg="red")
        controls.pack(anchor=tk.W, expand=True)

        self.button = tk.Button(controls, text=self.TITLE, command=self._button_press)
        self.button.pack(side=tk.LEFT)

        self.speed_var = tk.IntVar()
        self.speed_var.set(25)
        self.speed_scale = tk.Scale(controls, variable=self.speed_var, from_=500, to=1, orient=tk.HORIZONTAL, label="Speed:", showvalue=0)
        self.speed_scale.pack(side=tk.LEFT, padx=10)

        return frame

    def _draw_bars(self, checking=[], completed=[]):
        """
        Draws bars on a canvas
        """
        self.canvas.delete("all")
        canvas_height = self.canvas.winfo_height()
        max_value = max(self.data)
        bar_width = self.CANVAS_WIDTH // len(self.data)
        bar_spacing = 2
        for i, value in enumerate(self.data):
            x0 = i * bar_width + bar_spacing
            y0 = canvas_height - (value / max_value) * canvas_height
            x1 = (i + 1) * bar_width
            y1 = canvas_height
            color = "red" if i in checking else "green" if i in completed else "gray"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        self.canvas.update()

    def _button_press(self):
        if self.sorted:
            self._reset_sort()
        else:
            self._start_sort()

    def _start_sort(self):
        self.button["state"] = "disabled"
        # speed = self.speed_scale.get() / 1000
        self.sort()

    def _reset_sort(self):
        self.sorted = False
        self.data = [random.randint(10, 100) for _ in range(self.count_var.get())]
        self.button["text"] = self.TITLE
        self._draw_bars()

    def sort(self):
        raise NotImplementedError
