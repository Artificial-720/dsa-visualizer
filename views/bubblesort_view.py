from views.base_sort_view import BaseSortView


class BubbleSortView(BaseSortView):

    TITLE = "Bubble Sort"
    DESCRIPTION = "Bubble sort is a sorting algorithm that works by making the highest value bubble up"

    def sort_generator(self):
        n = len(self.data)
        completed = []
        for i in range(n - 1):
            for j in range(n - i - 1):
                yield [j, j + 1], completed
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
            completed.append(n - i - 1)
        completed.append(0)
        yield [], completed
