import re
import tkinter
from tkinter import *
from tkinter import messagebox
import qrcode, inflect, cv2, os
from mysql.connector import connect

mydb = connect(user='root', password='Khushan', host='localhost', auth_plugin='mysql_native_password',
               database="paytm_data")


class App:

    def __init__(self, root):
        self.phone_number = IntVar()
        self.phone_number.set("")
        self.password = StringVar()



        Login_frame = Frame(root, bg="#379683", width=252, height=400)
        Login_frame.place(x=84, y=150)

        Label(text="Pay Money", fg="midnight blue", bg="#659DBD", font=("Arial", 25, "bold")).place(x=115, y=1, width=190, height=43)
        Label(text="My Login", bg="#659DBD", font=("Arial", 15, "underline", "bold")).place(x=165, y=119, width=90)

        Label(Login_frame, text="Phone Number -:", fg="snow", bg="#379683", font=("Arial", 11)).place(x=10, y=58, height=30)
        Entry(Login_frame, textvariable=self.phone_number).place(x=13, y=80, height=30, width=190)

        Label(Login_frame, text="Password -:", fg="snow", bg="#379683", font=("Arial", 11)).place(x=10, y=168, height=30)
        Entry(Login_frame, textvariable=self.password, show="*").place(x=13, y=190, height=30, width=190)

        Button(Login_frame, text="Sumbit", fg="snow", bg="#379683", font=("Arial", 15), command=self.login_button).place(x=60, y=310, width=120)

    def login_button(self):
        cursor = mydb.cursor()
        set_password = str(self.password.get())

        try:
            set_phone_number = str(self.phone_number.get())
            try:
                cursor.execute(f"select Phone_Number from user_data where Phone_Number={set_phone_number}")
                original_phone_number = cursor.fetchone()[0]

                cursor.execute(f"select Set_Password from user_data where Phone_Number={set_phone_number}")
                original_password = cursor.fetchone()[0]

                if original_phone_number == set_phone_number and original_password == set_password:
                    print("Ph login")
                    self.home_screen(root)

                else:
                    messagebox.showerror("ERROR", "Invalid Phone Number or password!")

            except UnboundLocalError and TypeError:
                messagebox.showerror("ERROR", "Invalid Phone Number or password!")

        except :
            pass





scr = Tk()
scr.geometry("420x700")
scr.configure(bg="#659DBD")  # LightCyan4

App(scr)
scr.mainloop()