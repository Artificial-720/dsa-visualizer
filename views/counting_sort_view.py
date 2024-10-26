from views.base_sort_view import BaseSortView


class CountingSortView(BaseSortView):

    TITLE = "Counting Sort"
    DESCRIPTION = "Counting sort works by counting the number of times a value happens. Works best when range of data is small."
    DATA_MAX = 5

    def sort_generator(self):
        n = len(self.data)
        max_val = 0

        # Find max value
        i = 0
        while i < n:
            if self.data[i] > max_val:
                max_val = self.data[i]
            yield [i], []
            i += 1

        count = [0] * (max_val + 1)

        # store count of each element
        for i in range(n):
            count[self.data[i]] += 1
            yield [i], []

        # Store cumulative sum
        for i in range(1, max_val + 1):
            count[i] = count[i - 1] + count[i]

        # Copying input data to another array
        arr = self.data.copy()
        completed = []
        # Iterate over input array backwards
        for i in range(n - 1, -1, -1):
            val = arr[i]
            index = count[val] - 1
            self.data[index] = val
            completed.append(index)
            count[val] -= 1
            yield [index], completed

        yield [], completed
