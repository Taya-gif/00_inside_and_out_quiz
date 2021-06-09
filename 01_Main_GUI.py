from tkinter import *
from functools import partial   # To prevent unwanted windows

import random

class Start:
    def __init__(self, parent):

        # format variables...
        background_color = "#95DEFE"

        # Start main screen GUI
        self.start_frame = Frame(width=1000, height=1000, bg=background_color,
                                 pady=10)
        self.start_frame.grid()

        # Temperature Conversion heading (row 0)
        self.start_label = Label(self.start_frame, text="Inside and Out Quiz",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.start_label.grid(row=0)

        # history / help frame (row 1)
        self.hist_help_frame = Frame(self.start_frame)
        self.hist_help_frame.grid(row=1, pady=10)

        self.history_button = Button(self.hist_help_frame, text="History", bg="#95B8FE",
                                     font=("Arial", "14"), width=5,
                                     command=self.history)
        self.history_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5, command=self.help)
        self.help_button.grid(row=0, column=1)

    def history(self):
        print("You asked for history")
        get_history = History(self)
        get_history.history_text.configure(text="History text goes here")

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Please enter a number in the box "
                                              "and then push one of the buttons "
                                              " to convert the number to either  "
                                              "degrees C or degrees F.\n\n"
                                              "The Calculation History area shows "
                                              "up to seven past calculations "
                                              "(most recent at the top).  \n\nYou can "
                                              "also export your full calculation "
                                              "history to a text file if desired.")


class History:
    def __init__(self, partner):

        background = "NavajoWhite"

        # disable history button
        partner.history_button.config(state=DISABLED)

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
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


class Help:
    def __init__(self, partner):
        background = "orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="orange", font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Inside and Out")
    something = Start(root)
    root.mainloop()
