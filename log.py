from tkinter import *


class Log_in:
    def __init__(self):
        display = Tk()

        #img = PhotoImage('800x800')
        display.geometry('800x500')
        display.config(bg='black')
        display.title('Log-in')
        #display.resizable(width=False, height=False)
        self.string = StringVar()
        # entry = Entry(display, font=("Helvetica", 18), textvariable=self.string, width=30, bd=30, insertwidth=4,
        #               justify='right')
        # entry.grid(row=0, column=0, columnspan=6)
        # entry.configure(background="white")
        # entry.focus()

        btn = Label(display,bg='black',font=("Helvetica", 10),width=30)
        btn.grid(column=0, row=0)
        lb = Label(display,text='Sign Up',font=("Helvetica", 18),underline=0)
        lb.grid(column=2,row=1)


        display.mainloop()


if __name__ == '__main__':
    Log_in()
