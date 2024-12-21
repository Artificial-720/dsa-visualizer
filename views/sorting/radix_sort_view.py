from views.base import BaseArrayView


class RadixSortView(BaseArrayView):

    TITLE = "Radix Sort"
    DESCRIPTION = "Radix sort is a sorting algorithm that sorts by digit starting at the least moving to the greatest. This algorithm is a non comparative algorithm."
    DATA_MAX = 999

    def algorithm_generator(self):
        n = len(self.data)
        max_val = 0
        exp = 1

        # Find max value
        for i in range(n):
            if self.data[i] > max_val:
                max_val = self.data[i]
            yield [i], []

        # Run sort on each digit
        while max_val / exp >= 1:
            last_pass = not (max_val / (exp * 10) >= 1)

            count = [0] * 10

            # store count of each element
            for i in range(n):
                index = self.data[i] // exp
                count[index % 10] += 1
                yield [i], []

            # Store cumulative sum
            for i in range(1, 10):
                count[i] = count[i - 1] + count[i]

            # Copying input data to another array
            arr = self.data.copy()
            completed = []
            # Iterate over input array backwards
            for i in range(n - 1, -1, -1):
                index = arr[i] // exp
                data_index = count[index % 10] - 1
                self.data[data_index] = arr[i]
                # only append if on last pass
                if last_pass:
                    completed.append(data_index)
                count[index % 10] -= 1
                yield [data_index], completed

            exp *= 10

        yield [], completed
