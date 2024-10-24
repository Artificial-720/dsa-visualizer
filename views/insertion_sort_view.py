import time
from views.base_sort_view import BaseSortView


class InsertionSortView(BaseSortView):

    TITLE = "Insertion Sort"
    DESCRIPTION = "Insertion sort has part of the array sort and part unsorted, slowly takes one from the unsorted part and inserts it into the sorted part."

    def sort(self):
        """
        insertion sort with drawing
        """
        # TODO change to a generator, that yeilds the next step
        n = len(self.data)
        completed = [0]

        for i in range(1, n):
            completed.append(i)
            for j in range(i - 1, -1, -1):
                self._draw_bars([j + 1], completed)
                time.sleep(self.speed_var.get() / 1000)
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                else:
                    break

        # Draw bars one last time finished
        self._draw_bars([], completed)
        # change button
        self.button["text"] = "Reset"
        self.button["state"] = "active"
        self.sorted = True
