import tkinter as tk
from views.base_array_view import BaseArrayView


class BinarySearchView(BaseArrayView):

    TITLE = "Binary Search"
    DESCRIPTION = "Binary search works by checking the value at the center. if value is lower it next checks the center of the lower half and so on until value is found."

    DATA_MAX = 20

    def algorithm_generator(self):
        found = False
        search = self.search.get()
        left = 0
        right = len(self.data) - 1

        while left <= right:
            mid = (left + right) // 2

            # check middle value
            yield [mid], []
            if self.data[mid] == search:
                found = True
                self.label.config(text=f"Found at index {mid}")
                yield [], [mid]
                break

            # Update pointer
            if self.data[mid] < search:
                left = mid + 1
            else:
                right = mid - 1

        if not found:
            self.label.config(text="Not found")
            yield [], []

    def _generate_data(self):
        # Binary search needs data to be sorted
        return sorted(super()._generate_data())

    def create_controls_frame(self, container):
        control_frame = super().create_controls_frame(container)

        # label for output
        self.label = tk.Label(control_frame, text="")
        self.label.pack(pady=10, anchor=tk.W)

        # input box for search value
        self.search = tk.IntVar()
        self.search.set(4)
        search_box = tk.Entry(control_frame, textvariable=self.search)
        search_box.pack()
