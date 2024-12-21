from views.base import BaseArrayView


class BubbleSortView(BaseArrayView):

    TITLE = "Bubble Sort"
    DESCRIPTION = "Bubble sort is a sorting algorithm that works by making the highest value bubble up"

    def algorithm_generator(self):
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
