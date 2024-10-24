import time
from views.base_sort_view import BaseSortView


class BubbleSortView(BaseSortView):

    TITLE = "Bubble Sort"
    DESCRIPTION = "Bubble sort is a sorting algorithm that works by making the highest value bubble up"

    def sort(self):
        """
        bubble sort with drawing
        """
        # TODO change to a generator, that yeilds the next step
        n = len(self.data)
        completed = []
        for i in range(n - 1):
            for j in range(n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                self._draw_bars([j, j + 1], completed)
                time.sleep(self.speed_var.get() / 1000)
            completed.append(n - i - 1)
        completed.append(0)
        # Draw bars one last time finished
        self._draw_bars([], completed)
        # change button
        self.button["text"] = "Reset"
        self.button["state"] = "active"
        self.sorted = True
