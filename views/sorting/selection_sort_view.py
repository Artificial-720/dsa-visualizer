from views.base import BaseArrayView


class SelectionSortView(BaseArrayView):

    TITLE = "Selection Sort"
    DESCRIPTION = "Selection sort is a sorting algorithm that works by finding the smallest value and placing that value at the start of the array"

    def algorithm_generator(self):
        completed = []
        n = len(self.data)

        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                yield [j, min_index], completed
                if self.data[j] < self.data[min_index]:
                    min_index = j
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]
            completed.append(i)

        completed.append(n - 1)
        yield [], completed
