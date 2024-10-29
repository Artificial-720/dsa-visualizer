import tkinter as tk


class AbstractPage(tk.Frame):

    COLOR_BG = "grey85"

    def __init__(self, parent, controller):
        super().__init__(parent)
        nav_frame = self.create_nav_frame(controller)
        nav_frame.pack(side=tk.BOTTOM, fill=tk.X)

        info_frame = self.create_info_frame()
        info_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def create_nav_frame(self, controller):
        frame = tk.Frame(self, bg=self.COLOR_BG)
        # Button to go back to Start Page
        button1 = tk.Button(frame, text="Back to Start Page",
                            command=lambda: controller.show_frame('HomePage'))
        button1.pack()

        # Button to go to Page Two
        # button2 = tk.Button(frame, text="Go to Page Two",
                            # command=lambda: controller.show_frame('PageTwo'))
        # button2.pack()
        return frame

    def create_info_frame(self):
        frame = tk.Frame(self, bg="red")
        return frame
