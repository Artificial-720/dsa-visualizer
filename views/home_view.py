import tkinter as tk
import re


class HomePage(tk.Frame):

    COLOR_BG = "grey85"
    COLOR_SUB_FRAME = "darkgray"

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
        frame = tk.Frame(self, bg=self.COLOR_BG, padx=10, pady=10, borderwidth=5, relief="sunken")

        button = tk.Button(frame, text="Go to Bubble Sort",
                           command=lambda: self.controller.show_frame('BubbleSortView'))
        button.pack(side=tk.RIGHT, anchor="s")

        return frame

    def _create_selection_frame(self):
        frame = tk.Frame(self, bg=self.COLOR_BG, borderwidth=5, relief="sunken")

        # Title
        label = tk.Label(frame, text="Data Structures and Algorithms!", justify=tk.LEFT, font=("Arial", 16, "bold"))
        label.pack(side=tk.TOP, fill=tk.X, pady=5)

        # List frame with buttons to each algorithm
        list_frame = self._create_list_frame(frame)
        list_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        return frame

    def _create_list_frame(self, container):
        frame = tk.Frame(container, bg=self.COLOR_BG)

        sub_sections = self.controller.get_subsections()
        row, col = 0, 0
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        for group_title in sub_sections.keys():
            sub_frame = tk.Frame(frame, bg=self.COLOR_SUB_FRAME, bd=5, relief="ridge")
            sub_frame.grid(row=row, column=col, sticky="new", padx=10, pady=10)
            col += 1
            if col > 1:
                col = 0
                row += 1

            label = tk.Label(sub_frame, text=group_title, justify=tk.LEFT, font=("Arial", 14, "bold"))
            label.pack(side=tk.TOP, fill=tk.X)

            for frame_name in sub_sections[group_title]:
                title = frame_name
                # Remove view
                if title.endswith("View"):
                    title = title[:-4]
                # Add space between words
                title = re.sub(r"([a-z])([A-Z])", r"\1 \2", title)

                btn = tk.Button(sub_frame, text=title,
                                command=lambda frame_name=frame_name: self.controller.show_frame(frame_name))
                btn.pack(anchor="w", padx=5, pady=5)

        return frame
