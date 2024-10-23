import time
import random
import tkinter as tk
from views.abstractpage import AbstractPage


class BubbleSortView(AbstractPage):

    CANVAS_WIDTH = 400
    CANVAS_HEIGHT = 300
    DATA_SIZE = 20

    def tkraise(self):
        # Override
        super().tkraise()
        # waiting until drawn on the screen before drawing bars
        self._reset_sort()

    def create_info_frame(self):
        # Override
        frame = tk.Frame(self, bg="blue")
        title = tk.Label(frame, text="Bubble Sort", font=("Arial", 18))
        title.pack(pady=10)

        description = tk.Label(frame, text="some stuff")
        description.pack()

        self.canvas = tk.Canvas(frame, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT)
        self.canvas.pack()

        self.button = tk.Button(frame, text="Bubble Sort", command=self._button_press)
        self.button.pack()

        self.speed_scale = tk.Scale(frame, from_=1, to=100, orient=tk.HORIZONTAL, label="Speed:")
        self.speed_scale.pack()
        self.speed_scale.set(50)

        return frame

    def _draw_bars(self, checking=[], highlight_index=-1):
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
            color = "red" if i in checking else "green" if i >= highlight_index and highlight_index != -1 else "gray"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        self.canvas.update()

    def _bubble_sort(self, speed):
        """
        bubble sort with drawing
        """
        # TODO change to a generator, that yeilds the next step
        n = len(self.data)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                self._draw_bars([j, j + 1], n - i)
                time.sleep(speed)
        # Draw bars one last time finished
        self._draw_bars(highlight_index=0)
        # change button
        self.button["text"] = "Reset"
        self.button["state"] = "active"
        self.sorted = True

    def _button_press(self):
        if self.sorted:
            self._reset_sort()
        else:
            self._start_sort()

    def _start_sort(self):
        self.button["state"] = "disabled"
        speed = self.speed_scale.get() / 1000
        self._bubble_sort(speed)

    def _reset_sort(self):
        self.sorted = False
        self.data = [random.randint(10, 100) for _ in range(self.DATA_SIZE)]
        self.button["text"] = "Bubble Sort"
        self._draw_bars()
