import re
import tkinter
from tkinter import *
from tkinter import messagebox
import qrcode, inflect, cv2, os
from mysql.connector import connect

mydb = connect(user='root', password='Khushan', host='localhost', auth_plugin='mysql_native_password', database="paytm_data")
cursor = mydb.cursor()

User_win = Tk()

User_win.geometry("420x700+50+50")
User_win.minsize(width=420, height=700)
User_win.maxsize(width=420, height=700)
User_win.title("Pay Money")

User_win.configure(bg="#85C1E9")  # LightCyan4

back_image = PhotoImage(file="back 35.png")
Button(User_win, image=back_image, borderwidth=0, bg="#85C1E9", activebackground="#85C1E9").place(x=2, y=2, height=41, width=43)
Label(text="Khushan", fg="midnight blue", bg="#85C1E9", font=("Arial", 17, "bold")).place(x=59, y=1, height=43, width=300)


user_fr = Frame(User_win, bg="#5499C7", width=420, height=700)
user_fr.place(x=0, y=45)

user_cn = Canvas(user_fr, bg="#5499C7", width=100, height=100, highlightthickness=0)
user_cn.place(x=159, y=20)
user_cn.create_oval(2, 2, 99, 99, fill="red", outline="black", width=1)


qr_img = PhotoImage(file="test.png")
Label(user_fr, image = qr_img).place(x=110, y=140, width=200, height=200)


present_money = 1000
money = "Your Balance -: " + u"\u20B9" + str(present_money)
Label(user_fr, text=money, bg="#5499C7", font=("Arial", 15, "bold")).place(x=1, y=370, width=420)
Label(user_fr, text="Your phone number", bg="#5499C7", font=("Arial", 15, "bold")).place(x=1, y=340, width=420)

name = "Name -: " + "first name" + " last name"
Label(user_fr, text=name, bg="#5499C7", font=("Arial", 12, "bold")).place(x=30, y=440)

address = "Address -: " + "Address"
Label(user_fr, text=address, bg="#5499C7", font=("Arial", 12, "bold")).place(x=30, y=480)


User_win.mainloop()

