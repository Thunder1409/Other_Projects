import re
import tkinter
from tkinter import *
from tkinter import messagebox
import qrcode, inflect, cv2, os
from mysql.connector import connect


mian_screen = Tk()
mian_screen.geometry("420x700")
mian_screen.configure(bg="#85C1E9")  # LightCyan4

main_frame = Frame(mian_screen, bg="#5499C7", width=420, height=700)
main_frame.place(x=0, y=45)

user_image = PhotoImage(file="user.png")
Button(mian_screen, image=user_image, borderwidth=0, bg="#85C1E9", activebackground="#85C1E9").place(x=2, y=2, height=41, width=43)
Label(text="Hello Khushan", fg="midnight blue", bg="#85C1E9", font=("Arial", 15, "bold")).place(x=43, y=2, height=43)

pay_frame = Frame(main_frame, bg="#6832a8", width=380, height=90)
pay_frame.place(x=20, y=20)

scan_image = PhotoImage(file="money transfer 35.png")
Button(pay_frame, image=scan_image).place(x=15, y=15, height=40, width=68)
Label(pay_frame, text="Scan and Pay", bg="#6832a8", fg="snow").place(x=12, y=60)

pay_image = PhotoImage(file="cash 35.png")
Button(pay_frame, image=pay_image).place(x=110, y=15, height=40, width=68)
Label(pay_frame, text="Pay", bg="#6832a8", fg="snow").place(x=110, y=60, width=68)

mian_screen.mainloop()

