from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
import os
from worng import *

# Designing window for registration


def register():
    global F_ont
    global display2
    F_ont = Font(family='Times New Roman', size=17,
                 weight='bold', slant='italic', underline=1)
    display2 = Toplevel(display)
    display2.title("Registatration")
    display2.config(bg='white')
    display2.geometry("500x500")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(display2, text="Please enter details below").pack()
    Label(display2, text="").pack()
    username_lable = Label(display2, text="Username ", font=F_ont)
    username_lable.pack()
    username_entry = Entry(display2, textvariable=username,
                           width=15, bd=5, font=("Helvetica", 18), justify='left')
    username_entry.pack()
    password_lable = Label(display2, text="Password ")
    password_lable.pack()
    password_entry = Entry(display2, textvariable=password, show='*',
                           width=15, bd=5, font=("Helvetica", 18), justify='left')
    password_entry.pack()
    Label(display2, text="").pack()
    Button(display2, text="Register", width=10,
           height=1, bg="blue", command=register_user).pack()


# Implementing event on register button


def register_user():

    username_info = username.get()
    password_info = password.get()

    with open('userfile.txt', 'w') as f:
        f.write(username_info+'\n')
        f.write(password_info)

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(display2, text="Registration Success",
          fg="green", font=("calibri", 11)).pack()

# Implementing event on login button


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    try:

        with open('userfile.txt', 'r') as f:
            ss = f.read().splitlines()
            if username1 in ss:
                if password1 == ss[1]:
                    login_sucess()
                else:
                    password_not_recognised()
            else:
                user_not_found()
    except :
        print('Type something')

# Designing popup for login success


def login_sucess():
    Calculator()

# Designing popup for login invalid password


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(display)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK",
           command=delete_password_not_recognised).pack()

# Designing popup for user not found


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(display)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK",
           command=delete_user_not_found_screen).pack()

# Deleting popups


# def delete_login_success():
#     login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global display
    global username_verify
    global password_verify
    display = Tk()
    display.geometry("400x900")
    display.title("Account Login")
    t_img = PhotoImage(file='L.png')
    # t_img = t_img.zoom()
    t_img = t_img.subsample(6)

    Label(display, image=t_img).pack()

    Label(text="Select Your Choice", width="300",
          height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Label(display, text="Please enter details below to login").pack()
    Label(display, text="").pack()

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(display, text="Username * ").pack()
    username_login_entry = Entry(display, textvariable=username_verify)
    username_login_entry.pack()
    Label(display, text="").pack()
    Label(display, text="Password * ").pack()
    password_login_entry = Entry(
        display, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(display, text="").pack()
    Button(display, text="Login", width=10,
           height=1, command=login_verify).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    display.mainloop()


main_account_screen()
