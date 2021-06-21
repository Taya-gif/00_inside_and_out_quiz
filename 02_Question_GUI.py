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
        self.quiz_label = Label(self.start_frame, text="Inside and Out Quiz",
                                 font=("Arial", "16", "bold"),
                                 bg=background_color,
                                 padx=10, pady=10)
        self.quiz_label.grid(row=0)

        # Quiz breif (row 1)
        self.quiz_brief = Label(self.start_frame, text="Press the start button to begin the quiz :)",
                                 font=("Arial", "14"), bg=background_color)
        self.quiz_brief.grid(row=1)

        # quiz buttons (row 2)
        self.quiz_button = Button(self.start_frame, text="start",
                                  font=("Arial", "16", "bold"),
                                  bg="#B0FCB7", width="10", command=self.quiz)
        self.quiz_button.grid(row=2)

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

    def quiz(self):
        print("Pick A, B or C to answer the question")
        get_quiz = Quiz(self)
        get_quiz.quiz_text.configure(text="Pick A, B or C to answer the question")


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


class Quiz:
    def __init__(self, partner):

        background = "#D0CEFC"

        # disable quiz button
        partner.quiz_button.config(state=DISABLED)

        # set up quiz box
        self.quiz_box = Toplevel()

        # If uses closes the window - re open the quiz button
        self.quiz_box.protocol('WM_DELETE_WINDOW', partial(self.close_quiz, partner))

        # Quiz GUI frame
        self.quiz_frame = Frame(self.quiz_box, width=300, bg=background)
        self.quiz_frame.grid()

        # set up quiz heading(row 0)
        self.quiz_heading = Label(self.quiz_frame, text="Inside and Out Quiz",
                                  font=("arial", "13", "bold"), bg=background)
        self.quiz_heading.grid(row=0, pady=15, padx=15)

        # quiz text (label, row 1)
        self.quiz_text = Label(self.quiz_frame, text="", font="Arial 10 bold",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.quiz_text.grid(column=0, row=1)

        # question label (row 2)
        self.question_text = Label(self.quiz_frame, text="What's not a function of the skeletal system? \n"
                                                         "A, protection  B, support  C, digestion",
                                   width=40, bg=background, wrap=250)
        self.question_text.grid(row=2)

        # Quiz Question Frame (row 3)
        self.question_frame = Frame(self.quiz_frame, bg=background)
        self.question_frame.grid(row=3, pady=10)

        self.a_button = Button(self.question_frame, text="A", width="10",
                               bg="#BABCE2", font="arial 10 bold")
        self.a_button.grid(row=3, column=0)

        self.b_button = Button(self.question_frame, text="B", width="10",
                               bg="#BABCE2", font="arial 10 bold")
        self.b_button.grid(row=3, column=1)

        self.c_button = Button(self.question_frame, text="C", width="10",
                               bg="#BABCE2", font="arial 10 bold")
        self.c_button.grid(row=3, column=3)

        # Quiz feedback(row 4)
        self.quiz_feedback = Label(self.quiz_frame, text="Feedback", font=("arial", "13", "bold"),
                                   width="40", wrap=250, bg=background)
        self.quiz_feedback.grid(row=4, column=0)

        # Dismiss/next button Frame(row 5)
        self.dis_next_frame = Frame(self.quiz_frame, bg=background)
        self.dis_next_frame.grid(row=5)

        self.dismiss_btn = Button(self.dis_next_frame, text="Dismiss",
                                  width=10, bg="#95B8FE", font="arial 10 bold",
                                  command=partial(self.close_quiz, partner))
        self.dismiss_btn.grid(row=5, pady=10, column=0)

        self.next_btn = Button(self.dis_next_frame, text="Next", width=10, bg="#95B8FE",
                               font="arial 10 bold")
        self.next_btn.grid(row=5, column=1)

    def close_quiz(self, partner):
        partner.quiz_button.config(state=NORMAL)
        self.quiz_box.destroy()



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Inside and Out")
    something = Start(root)
    root.mainloop()
