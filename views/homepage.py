import tkinter as tk


def create_list_frame(container, controller):
    # Scroll bar
    # https://www.geeksforgeeks.org/scrollable-frames-in-tkinter/
    frame = tk.Frame(container, bg="blue")

    for b in ["title1", "title2", "title3"]:
        tk.Button(frame, text=b,
                  command=lambda: controller.show_frame('SelectionSortView'))

    for widget in frame.winfo_children():
        widget.pack(anchor="w", padx=5, pady=5)

    return frame


def create_selection_frame(container, controller):
    frame = tk.Frame(container, bg="grey")
    # Title
    label = tk.Label(frame, text="Hello world!", justify=tk.LEFT, font=("Arial", 16, "bold"))
    label.pack(side=tk.TOP, fill=tk.X, pady=5)

    # List
    list_frame = create_list_frame(frame, controller)
    list_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    return frame


def create_button_frame(container, controller):
    frame = tk.Frame(container, bg="grey", padx=10, pady=10)

    def a():
        frame2 = tk.Frame(container, bg="green", padx=10, pady=10)
        button2 = tk.Button(frame2, text="Next")
        button2.pack(side=tk.RIGHT, anchor="s")
        frame2.tkraise()
        print("HI")

    # button = tk.Button(frame, text="Next", command=a)
    # button.pack(side=tk.RIGHT, anchor="s")
    button = tk.Button(frame, text="Go to Bubble Sort",
                       command=lambda: controller.show_frame('BubbleSortView'))
    button.pack(side=tk.RIGHT, anchor="s")
    return frame


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        """
        label = tk.Label(self, text="Start Page", font=("Arial", 18))
        label.pack(pady=10)

        # Button to go to Page One
        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()
        """
        selection_frame = create_selection_frame(self, controller)
        selection_frame["borderwidth"] = 5
        selection_frame["relief"] = "sunken"
        selection_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        button_frame = create_button_frame(self, controller)
        button_frame["borderwidth"] = 5
        button_frame["relief"] = "sunken"
        button_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
