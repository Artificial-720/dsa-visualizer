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
from views.queue_view import QueueView

from views.linked_list_view import LinkedListView

from views.tree_traversal_view import TreeTraversalView
from views.binary_search_tree_view import BinarySearchTreeView
from views.avl_tree_view import AVLTreeView


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DSA Visualizer")
        self.geometry("800x800")

        # Main container holding all frames
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Dictionary holding instances of each page
        self.frames = {}

        pages = [BubbleSortView, SelectionSortView, InsertionSortView, MergeSortView, CountingSortView, RadixSortView, QuickSortView, LinearSearchView, BinarySearchView, StackView, QueueView, LinkedListView, TreeTraversalView, BinarySearchTreeView, AVLTreeView]
        # Initialize home page last, to include all other pages
        pages.append(HomePage)

        # Initialize each view saving in dictionary
        for F in pages:
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

    def get_frames(self):
        """Returns frame names"""
        return self.frames.keys()
