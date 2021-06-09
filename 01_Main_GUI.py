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

        # Quiz Name heading (row 0)
        self.start_label = Label(self.start_frame, text="Inside and Out Quiz",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.start_label.grid(row=0)

        # Quiz breif (row 1)
        self.start_brief = Label(self.start_frame, text="Press the start button to begin the quiz :)",
                                 font=("Arial", "14"), bg=background_color)
        self.start_brief.grid(row=1)

        # start buttons (row 2)
        self.start_button = Button(self.start_frame, text="start",
                                   font=("Arial", "16", "bold"),
                                   bg="#B0FCB7", width="10")
        self.start_button.grid(row=2)

        # history / help frame (row 3)
        self.hist_help_frame = Frame(self.start_frame)
        self.hist_help_frame.grid(row=3, pady=10)

        self.history_button = Button(self.hist_help_frame, text="History", bg="#95B8FE",
                                     font=("Arial", "14"), width=8,
                                     command=self.history)
        self.history_button.grid(row=3, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 14", bg="#95B8FE",
                                  text="Help", width=8, command=self.help)
        self.help_button.grid(row=3, column=1)

    def history(self):
        print("You asked for history")
        get_history = History(self)
        get_history.history_text.configure(text="History text goes here")

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Press Start whenever you are ready, \n"
                                          "You will then be asked questions and \n"
                                          "you have three options \n"
                                          "after you have answered press the next \n"
                                          "question button \n"
                                          "The program will then give you feedback \n"
                                          "and send you onto the next question \n")


class History:
    def __init__(self, partner):

        background = "#D0CEFC"

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
                                  width=10, bg="#95B8FE", font="arial 10 bold",
                                  command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_history(self, partner):
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


class Help:
    def __init__(self, partner):
        background = "#D0CEFC"

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
                                  width=10, bg="#95B8FE", font="arial 10 bold",
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
