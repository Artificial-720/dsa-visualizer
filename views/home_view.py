import tkinter as tk
import re


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

        for frame_name in self.controller.get_frames():
            title = frame_name
            # Remove view
            if title.endswith("View"):
                title = title[:-4]
            # Add space between words
            title = re.sub(r"([a-z])([A-Z])", r"\1 \2", title)

            btn = tk.Button(frame, text=title,
                            command=lambda frame_name=frame_name: self.controller.show_frame(frame_name))
            btn.pack(anchor="w", padx=5, pady=5)

        return frame
