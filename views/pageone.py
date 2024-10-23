import tkinter as tk


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="Page One", font=("Arial", 18))
        label.pack(pady=10)

        # Button to go back to Start Page
        button1 = tk.Button(self, text="Back to Start Page",
                            command=lambda: controller.show_frame('HomePage'))
        button1.pack()

        # Button to go to Page Two
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame('PageTwo'))
        button2.pack()
