import time
from views.base_sort_view import BaseSortView


class BubbleSortView(BaseSortView):

    TITLE = "Bubble Sort"
    DESCRIPTION = "Bubble sort is a sorting algorithm that works by making the highest value bubble up"

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

    def sort(self):
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
                time.sleep(self.speed_var.get() / 1000)
        # Draw bars one last time finished
        self._draw_bars(highlight_index=0)
        # change button
        self.button["text"] = "Reset"
        self.button["state"] = "active"
        self.sorted = True
