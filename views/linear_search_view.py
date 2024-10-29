import tkinter as tk
from views.base_sort_view import BaseSortView


class LinearSearchView(BaseSortView):

    TITLE = "Linear Search"
    DESCRIPTION = "Linear search works by check each index for the value from left to right until it finds the value."

    DATA_MAX = 10

    def sort_generator(self):
        n = len(self.data)
        found = False
        self.label["text"] = ""
        search = self.search.get()
        for i in range(n):
            yield [i], []
            if self.data[i] == search:
                found = True
                self.label["text"] = f"Found at index {i}"
                yield [], [i]
                break
        if not found:
            self.label["text"] = "Not found"

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
