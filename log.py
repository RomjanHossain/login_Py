from tkinter import *
from tkinter.font import Font
from turtle import *


class Log_in:
    def __init__(self):

        display = Tk()
        # canvas = Canvas(display, width=500, height=500)
        # canvas.grid(column=4, row=11)
        F_ont = Font(family='Times New Roman', size=17,
                     weight='bold', slant='italic', underline=1, overstrike=1)

        #img = PhotoImage('800x800')
        display.geometry('700x500')
        display.config(bg='black')
        display.title('Log-in')
        #display.resizable(width=False, height=False)
        self.string = StringVar()
        # entry = Entry(display, font=("Helvetica", 18), textvariable=self.string, width=30, bd=30, insertwidth=4,
        #               justify='right')
        # entry.grid(row=0, column=0, columnspan=6)
        # entry.configure(background="white")
        # entry.focus()

        btn = Label(display, bg='black', font=F_ont, width=14)
        btn.grid(column=0, row=0)
        lb = Label(display, text='Log to Your Account', font=F_ont)
        lb.grid(column=1, row=1)
        username = Label(display, text='Username',font=F_ont)
        username.grid(column=0, row=2)
        entry = Entry(display, font=("Helvetica", 18), textvariable=self.string, width=30, bd=8, insertwidth=4,
                      justify='left')
        entry.grid(column=0, row=3)

        password = Label(display, text='password',font=F_ont)
        password.grid(column=0, row=4)
        entry1 = Entry(display, font=("Helvetica", 18),show='*', width=30, bd=8, insertwidth=4,
                      justify='left')
        entry1.grid(column=0, row=5)

        snbtn = Button(display, text='Sign In',width=30)
        snbtn.grid(column=1, row=8)
        fpass = Button(display, text='Forget Password')
        fpass.grid(column=1, row=9)

        display.mainloop()

    # def make_a_circle(self):
    #     king = Turtle()
    #     for i in range(3):
    #         king.forward(200)
    #         king.left(90)


if __name__ == '__main__':
    Log_in()
