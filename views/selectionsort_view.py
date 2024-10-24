import time
from views.base_sort_view import BaseSortView


class SelectionSortView(BaseSortView):

    TITLE = "Selection Sort"
    DESCRIPTION = "Selection sort is a sorting algorithm that works by finding the smallest value and placing that value at the start of the array"

    def sort(self):
        """
        selection sort with drawing
        """
        # TODO change to a generator, that yeilds the next step
        completed = []
        n = len(self.data)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if self.data[j] < self.data[min_index]:
                    min_index = j
                self._draw_bars([j, min_index], completed)
                time.sleep(self.speed_var.get() / 1000)
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]
            completed.append(i)

        # Draw bars one last time finished
        self._draw_bars(completed=[i for i in range(n)])
        # change button
        self.button["text"] = "Reset"
        self.button["state"] = "active"
        self.sorted = True
