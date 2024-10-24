import tkinter as tk
from views.homepage import HomePage
from views.pageone import PageOne
from views.pagetwo import PageTwo
from views.bubblesort import BubbleSortView
from views.selectionsort import SelectionSortView


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
        for F in (HomePage, PageOne, PageTwo, BubbleSortView, SelectionSortView):
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
