import tkinter as tk
from views.home_view import HomePage

# Array
from views.bubble_sort_view import BubbleSortView
from views.selection_sort_view import SelectionSortView
from views.insertion_sort_view import InsertionSortView
from views.merge_sort_view import MergeSortView
from views.counting_sort_view import CountingSortView
from views.radix_sort_view import RadixSortView
from views.quick_sort_view import QuickSortView
from views.linear_search_view import LinearSearchView
from views.binary_search_view import BinarySearchView

from views.stack_view import StackView


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DSA Visualizer")
        self.geometry("800x600")

        # Main container holding all frames
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Dictionary holding instances of each page
        self.frames = {}

        # Initialize each view saving in dictionary
        for F in (HomePage, BubbleSortView, SelectionSortView, InsertionSortView, MergeSortView, CountingSortView, RadixSortView, QuickSortView, LinearSearchView, BinarySearchView, StackView):
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        # Show home page
        self.show_frame('HomePage')

    def show_frame(self, page_name):
        """
        Raise frame to top making it visible
        """
        print(f"Switching view to {page_name}")
        frame = self.frames[page_name]
        frame.tkraise()
