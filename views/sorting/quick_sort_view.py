from views.base import BaseArrayView


class QuickSortView(BaseArrayView):

    TITLE = "Quick Sort"
    DESCRIPTION = "Quick sort chooses a pivot point and moves elements that are lower to the left and elements that are higher to the right."

    def algorithm_generator(self):
        self.completed = []
        yield from self._quick_sort()
        yield [], self.completed

    def _quick_sort(self, low=0, high=None):
        if high is None:
            high = len(self.data) - 1

        if low < high:
            pivot = yield from self._partition(low, high)
            yield from self._quick_sort(low, pivot - 1)
            yield from self._quick_sort(pivot + 1, high)
        elif low == high:
            # array of length 1 so sorted
            self.completed.append(low)

    def _partition(self, low, high):
        pivot_val = self.data[high]
        i = low - 1

        for j in range(low, high):
            yield [high, j], self.completed
            if self.data[j] <= pivot_val:
                i += 1
                # swap cause less then pivot
                # yield [i, j], self.completed
                self.data[i], self.data[j] = self.data[j], self.data[i]

        # i + 1 is now in correct spot
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        self.completed.append(i + 1)
        yield [i + 1, high], self.completed
        return i + 1
