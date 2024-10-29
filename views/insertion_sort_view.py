from views.base_array_view import BaseArrayView


class InsertionSortView(BaseArrayView):

    TITLE = "Insertion Sort"
    DESCRIPTION = "Insertion sort has part of the array sort and part unsorted, slowly takes one from the unsorted part and inserts it into the sorted part."

    def algorithm_generator(self):
        n = len(self.data)
        completed = [0]

        for i in range(1, n):
            completed.append(i)
            for j in range(i - 1, -1, -1):
                yield [j + 1], completed
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                else:
                    break
        yield [], completed
