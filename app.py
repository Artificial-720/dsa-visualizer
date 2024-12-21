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

        # Dictionary holding page groupings
        self.subsections = {}

        # Dictionary holding instances of each page
        self.frames = {}

        sorting = [BubbleSortView, CountingSortView, InsertionSortView, MergeSortView, QuickSortView, RadixSortView, SelectionSortView]
        self.init_view("Sorting", sorting, container)
        searching = [BinarySearchView, LinearSearchView]
        self.init_view("Searching", searching, container)
        graph = [GraphCycleDetectionDirectedView, GraphCycleDetectionUndirectedView, GraphMinimumSpanningTreeKruskalView, GraphMinimumSpanningTreePrimsView, GraphShortestPathBellmanFordView, GraphShortestPathDijkstrasView, GraphTraversalView]
        self.init_view("Graphs", graph, container)
        tree = [AVLTreeView, BinarySearchTreeView, TreeTraversalView]
        self.init_view("Tree", tree, container)
        data_stuct = [LinkedListView, QueueView, StackView]
        self.init_view("Data Structures", data_stuct, container)

        # Initialize home page last, to include all other pages
        self.init_view(None, [HomePage], container)

        # Show home page
        self.show_frame('HomePage')

    def init_view(self, grouping, pages, container):
        # Initialize each view saving in dictionary
        for F in pages:
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)
            if grouping is not None:
                self.subsections.setdefault(grouping, []).append(F.__name__)

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

    def get_subsections(self):
        """Returns dictionary with sections"""
        return self.subsections
