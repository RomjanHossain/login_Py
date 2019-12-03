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
        lb = Label(display,text='Sign In',font=("Helvetica", 18),underline=0)
        lb.grid(column=2,row=1)
        username = Label(display,text='Username')
        username.grid(column=1,row=2)
        entry = Entry(display,font=("Helvetica", 8))
        entry.grid(column=1,row=3)


        password = Label(display,text='password')
        password.grid(column=1,row=4)
        entry1 = Entry(display,font=("Helvetica", 8))
        entry1.grid(column=1,row=5)

        snbtn = Button(display,text='Sign In')
        snbtn.grid(column=3,row=8)
        fpass = Button(display,text='Forget Password')
        fpass.grid(column=3,row=9)

        display.mainloop()


if __name__ == '__main__':
    Log_in()
