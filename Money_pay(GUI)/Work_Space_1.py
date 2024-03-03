'''

import re
import tkinter
import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
import qrcode, inflect, cv2, os
from PIL import Image, ImageTk
from mysql.connector import connect

mydb = connect(user='root', password='Khushan', host='localhost', auth_plugin='mysql_native_password',
               database="paytm_data")


root = Tk()
root.geometry("420x700+250+50")
root.minsize(width=420, height=700)
root.maxsize(width=420, height=700)
root.configure(bg="#85C1E9")

back_image = PhotoImage(file="back 35.png")
Button(root, image=back_image, borderwidth=0, bg="#85C1E9", activebackground="#85C1E9").place(x=2, y=2, height=41,
                                                                                              width=43)
Label(text="Pay Money", fg="midnight blue", bg="#85C1E9", font=("Arial", 17, "bold")).place(x=59, y=1, height=43,
                                                                                            width=300)

pay_fr = Frame(root, bg="#5499C7", width=420, height=700)
pay_fr.place(x=0, y=45)

web_bg = Canvas(pay_fr, height=250, width=250, borderwidth=0, bg="#5499C7")
web_bg.place(x=85, y=20)

payment_amount = IntVar()
payment_amount.set("")

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
web_cam = Label(web_bg)
web_cam.place(x=0, y=0)


    def pin(self):
        try:
            pay_amount = self.payment_amount.get()
            cursor.execute(f"select Balance from money_data where Phone_Number = {taker_phone_no}")
            pin_fr = Frame(self.pay_fr, bg="#5499C7", width=420, height=400)
            pin_fr.place(x=0, y=330)

            self.pin_inp = IntVar()
            self.pin_inp.set("")

            Label(self.pay_fr, text="Amount -:", fg="black", bg="#5499C7", font=("Arial", 12)).place(x=138, y=340)
            Entry(self.pay_fr, textvariable=self.pin_inp).place(x=138, y=362, height=30, width=150)

            Button(self.pay_fr, text="Pay", bg="#379683", font=("Arial", 15)).place(x=160, y=430, width=100)

        except:
            messagebox.showerror("Error", "Enter the proper Ammount!!")

def webcam():
    _, img = cap.read()
    data, bbox, _ = detector.detectAndDecode(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (250, 250))  # 250, 250
    img2 = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=img2)

    web_cam.imgtk = imgtk
    web_cam.configure(image=imgtk)
    if data:
        try:

            cursor = mydb.cursor()
            taker_phone_no = data
            cursor.execute(f"select First_name from user_data where Phone_Number={taker_phone_no}")
            first_name = cursor.fetchone()[0]

            cursor.execute(f"select Last_name from user_data where Phone_Number={taker_phone_no}")
            last_name = cursor.fetchone()[0]

            name = first_name + " " + last_name
            Label(pay_fr, text=name, fg="black", bg="#5499C7", font=("Arial", 16, "bold")).place(x=85, y=270,
                                                                                                 width=250)
            Label(pay_fr, text=taker_phone_no, fg="black", bg="#5499C7", font=("Arial", 16, "bold")).place(x=85,
                                                                                                           y=300,
                                                                                                           width=250)

            Label(pay_fr, text="Amount -:", fg="black", bg="#5499C7", font=("Arial", 12)).place(x=138, y=340)
            Entry(pay_fr, textvariable=payment_amount).place(x=138, y=362, height=30, width=150)

            Button(pay_fr, text="Pay", bg="#379683", font=("Arial", 15), command=special_pin).place(x=160,
                                                                                                         y=430,
                                                                                                         width=100)

        except:
            messagebox.showinfo("Note", "Number not registered!")

    else:
        web_cam.after(10, webcam)


    def payed_screen(self):
        try:
            pin = self.pin.get()
            cursor = mydb.cursor()
            cursor.execute(f"select Special_Pin from money_data where Phone_Number = {self.myphone_number}")
            payed_fr = Frame(self.pay_fr, bg="#5499C7", width=420, height=400)
            payed_fr.place(x=0, y=330)


        except:
            print("Enter the pin")


webcam()

root.mainloop()





def pay_qr_code():

    cursor.execute(f"select Balance from money_data where Phone_Number = {taker_phone_no}")
    try:
        taker_balance = cursor.fetchone()[0]
        cursor.execute(f"select Balance from money_data where Phone_Number = {my_phone_number}")
        my_balance = cursor.fetchone()[0]
        print("\nYour Balance ", my_balance)
        while 1:
            pay_amount = int(input("\nEnter the amount you want to pay -: "))
            if pay_amount > my_balance:
                print("Not enough money")

            else:
                break

        updated_my_balance, updated_taker_balance = my_balance - pay_amount, taker_balance + pay_amount
        print(updated_taker_balance, updated_my_balance)
        cursor.execute(f"Update money_data set Balance = {updated_my_balance} where Phone_Number = {my_phone_number}")
        cursor.execute(f"Update money_data set Balance = {updated_taker_balance} where Phone_Number = {taker_phone_no}")
        mydb.commit()
        print("\nLeft balance in your account is", updated_my_balance)

    except TypeError:
        print("\nNo account found")

'''