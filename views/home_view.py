import tkinter as tk


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Left frame
        selection_frame = self._create_selection_frame()
        selection_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Right frame
        button_frame = self._create_button_frame()
        button_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def _create_button_frame(self):
        frame = tk.Frame(self, bg="grey", padx=10, pady=10, borderwidth=5, relief="sunken")

        button = tk.Button(frame, text="Go to Bubble Sort",
                           command=lambda: self.controller.show_frame('BubbleSortView'))
        button.pack(side=tk.RIGHT, anchor="s")

        return frame

    def _create_selection_frame(self):
        frame = tk.Frame(self, bg="grey", borderwidth=5, relief="sunken")

        # Title
        label = tk.Label(frame, text="Data Structures and Algorithms!", justify=tk.LEFT, font=("Arial", 16, "bold"))
        label.pack(side=tk.TOP, fill=tk.X, pady=5)

        # List frame with buttons to each algorithm
        list_frame = self._create_list_frame(frame)
        list_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        return frame

    def _create_list_frame(self, container):
        frame = tk.Frame(container, bg="blue")

        tk.Button(frame, text="Bubble Sort",
                  command=lambda: self.controller.show_frame('BubbleSortView'))
        tk.Button(frame, text="Selection Sort",
                  command=lambda: self.controller.show_frame('SelectionSortView'))
        tk.Button(frame, text="Insertion Sort",
                  command=lambda: self.controller.show_frame('InsertionSortView'))
        tk.Button(frame, text="Merge Sort",
                  command=lambda: self.controller.show_frame('MergeSortView'))
        tk.Button(frame, text="Counting Sort",
                  command=lambda: self.controller.show_frame('CountingSortView'))
        tk.Button(frame, text="Radix Sort",
                  command=lambda: self.controller.show_frame('RadixSortView'))
        tk.Button(frame, text="Quick Sort",
                  command=lambda: self.controller.show_frame('QuickSortView'))
        tk.Button(frame, text="Linear Search",
                  command=lambda: self.controller.show_frame('LinearSearchView'))
        tk.Button(frame, text="Binary Search",
                  command=lambda: self.controller.show_frame('BinarySearchView'))

        # Stack
        tk.Button(frame, text="Stack",
                  command=lambda: self.controller.show_frame('StackView'))
        # Queue
        tk.Button(frame, text="Queue",
                  command=lambda: self.controller.show_frame('QueueView'))

        for widget in frame.winfo_children():
            widget.pack(anchor="w", padx=5, pady=5)

        return frame
