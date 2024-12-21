from views.base import BaseArrayView


class MergeSortView(BaseArrayView):

    TITLE = "Merge Sort"
    DESCRIPTION = "Merge sort is a sorting algorithm that sorts by divide-and-conquer breaking the array into smaller arrays"

    def algorithm_generator(self):
        yield from self._merge_sort(0, len(self.data) - 1)
        yield [], [i for i in range(len(self.data))]

    def _merge_sort(self, l_index, r_index):
        if l_index < r_index:
            mid = l_index + (r_index - l_index) // 2
            yield from self._merge_sort(l_index, mid)
            yield from self._merge_sort(mid + 1, r_index)
            yield from self._merge(l_index, mid, r_index)

    def _merge(self, start, mid, end):
        completed = []
        right_index = mid + 1

        while (start <= mid and right_index <= end):
            yield [start, right_index], completed

            completed.append(start)
            if (self.data[start] <= self.data[right_index]):
                start += 1
            else:
                value = self.data[right_index]
                index = right_index

                # shift all the items
                while (index != start):
                    self.data[index] = self.data[index - 1]
                    index -= 1

                self.data[start] = value

                start += 1
                mid += 1
                right_index += 1
