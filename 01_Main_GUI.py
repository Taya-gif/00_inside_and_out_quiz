from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Start:
    def __init__(self, parent):

        # format variables...
        background_color = "lightcoral"

        # Start main screen GUI
        self.start_frame = Frame(width=1000, height=1000, bg=background_color,
                                 pady=10)
        self.start_frame.grid()

        # Temperature Conversion heading (row 0)
        self.start_label = Label(self.start_frame, text="Temperature Start",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.start_label.grid(row=0)

        # history button (row 1)
        self.his_button = Button(self.start_frame, text="History", bg="Salmon",
                                 font=("Arial", "14"),
                                 padx=10, pady=10, command=self.history)
        self.his_button.grid(row=1)

    def history(self):
        print("You asked for history")
        get_history = History(self)
        get_history.history_text.configure(text="History text goes here")

class History:
    def __init__(self, partner):

        background = "NavajoWhite"

        # disable history button
        partner.his_button.config(state=DISABLED)

        # set up history box
        self.history_box = Toplevel()

        # If uses closes the window - re open the history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # History GUI frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        # set up History heading(row 0)
        self.history_heading = Label(self.history_frame, text="History / Instructions",
                                  font=("arial", "10", "bold"), bg=background)
        self.history_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame, text="History text goes here...",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.history_text.grid(column=0, row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.history_frame, text="Dismiss",
                                  width=10, bg="BurlyWood", font="arial 10 bold",
                                  command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_history(self, partner):
        partner.his_button.config(state=NORMAL)
        self.history_box.destroy()



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Inside and Out")
    something = Start(root)
    root.mainloop()
