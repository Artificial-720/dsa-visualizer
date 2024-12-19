import tkinter as tk
from views import HomePage

# Array
from views import (
    BubbleSortView,
    CountingSortView,
    InsertionSortView,
    MergeSortView,
    QuickSortView,
    RadixSortView,
    SelectionSortView,

    LinearSearchView,
    BinarySearchView,


    GraphCycleDetectionDirectedView,
    GraphCycleDetectionUndirectedView,
    GraphMinimumSpanningTreeKruskalView,
    GraphMinimumSpanningTreePrimsView,
    GraphShortestPathBellmanFordView,
    GraphShortestPathDijkstrasView,
    GraphTraversalView,

    AVLTreeView,
    BinarySearchTreeView,
    TreeTraversalView,

    LinkedListView,
    QueueView,
    StackView
)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DSA Visualizer")
        self.geometry("800x950")

        # Main container holding all frames
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Dictionary holding instances of each page
        self.frames = {}

        sorting = [BubbleSortView, CountingSortView, InsertionSortView, MergeSortView, QuickSortView, RadixSortView, SelectionSortView]
        searching = [BinarySearchView, LinearSearchView]
        graph = [GraphCycleDetectionDirectedView, GraphCycleDetectionUndirectedView, GraphMinimumSpanningTreeKruskalView, GraphMinimumSpanningTreePrimsView, GraphShortestPathBellmanFordView, GraphShortestPathDijkstrasView, GraphTraversalView]
        tree = [AVLTreeView, BinarySearchTreeView, TreeTraversalView]
        data_stuct = [LinkedListView, QueueView, StackView]

        pages = sorting + searching + graph + tree + data_stuct
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
