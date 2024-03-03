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

class a:

    def __init__(self, screen):
        self.myphone_number = "9568877599"
        self.back_image = PhotoImage(file="back 35.png")
        Button(screen, image=self.back_image, borderwidth=0, bg="#85C1E9", activebackground="#85C1E9").place(x=2, y=2, height=41, width=43)
        Label(screen, text="Pay Money", fg="midnight blue", bg="#85C1E9", font=("Arial", 17, "bold")).place(x=59, y=1, height=43, width=300)

        self.pay_fr = Frame(screen, bg="#5499C7", width=420, height=700)
        self.pay_fr.place(x=0, y=45)

        web_bg = Canvas(self.pay_fr, height=250, width=250, borderwidth=0, bg="#5499C7")
        web_bg.place(x=85, y=20)

        self.cap = cv2.VideoCapture(0)
        self.detector = cv2.QRCodeDetector()
        self.web_cam = Label(web_bg)
        self.web_cam.place(x=0, y=0)

        self.webcam()

        self.payment_amount = IntVar()
        self.payment_amount.set("")

    def webcam(self):
        _, img = self.cap.read()
        data, bbox, _ = self.detector.detectAndDecode(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (250, 250))  # 250, 250
        img2 = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img2)

        self.web_cam.imgtk = imgtk
        self.web_cam.configure(image=imgtk)
        if data:
            try:
                self.taker_phone_no = data

            except:
                messagebox.showinfo("Note", "Number not registered!")

            cursor = mydb.cursor()
            cursor.execute(f"select First_name from user_data where Phone_Number={self.taker_phone_no}")
            first_name = cursor.fetchone()[0]

            cursor.execute(f"select Last_name from user_data where Phone_Number={self.taker_phone_no}")
            last_name = cursor.fetchone()[0]

            name = first_name + " " + last_name
            Label(self.pay_fr, text=name, fg="black", bg="#5499C7", font=("Arial", 16, "bold")).place(x=85, y=275,
                                                                                                      width=250)
            Label(self.pay_fr, text=self.taker_phone_no, fg="black", bg="#5499C7", font=("Arial", 16, "bold")).place(
                x=85,
                y=300,
                width=250)

            amount_fr = Frame(self.pay_fr, bg="royal blue", width=200, height=200)
            amount_fr.place(x=110, y=360)

            Label(amount_fr, text="Amount -:", fg="black", bg="royal blue", font=("Arial", 15, "bold")).place(x=0, y=20,
                                                                                                              width=200)
            Entry(amount_fr, textvariable=self.payment_amount).place(x=30, y=65, height=30, width=140)

            Button(amount_fr, text="Pay", bg="#379683", font=("Arial", 15), command=self.special_pin).place(x=50, y=140,
                                                                                                            width=100)

        else:
            self.web_cam.after(10, self.webcam)

    def special_pin(self):

        try:
            self.pay_amount = self.payment_amount.get()

            self.pin = IntVar()
            self.pin.set("")

            pin_fr = Frame(self.pay_fr, bg = "royal blue", width=200, height=200)
            pin_fr.place(x=110, y=360)

            Label(pin_fr, text="PIN", fg="black", bg="royal blue", font=("Arial", 18, "bold")).place(x=0, y=20, width=200)
            Entry(pin_fr, textvariable=self.pin).place(x=30, y=65, height=30, width=140)

            Button(pin_fr, text="Pay", bg="#379683", font=("Arial", 15), command=self.payed_screen).place(x=50, y=140, width=100)

        except:
            messagebox.showerror("Error", "Enter the proper Ammount!!")

    def payed_screen(self):
        try:
            pin = str(self.pin.get())
            cursor = mydb.cursor()
            cursor.execute(f"select Special_Pin from user_data where Phone_Number = {self.myphone_number}")
            original_pin = cursor.fetchone()[0]

            cursor.execute(f"select Balance from money_data where Phone_Number = {self.taker_phone_no}")
            taker_balance = cursor.fetchone()[0]

            cursor.execute(f"select Balance from money_data where Phone_Number = {self.myphone_number}")
            my_balance = cursor.fetchone()[0]

            payed_fr = Frame(self.pay_fr, bg="#5499C7", width=420, height=400)
            payed_fr.place(x=0, y=330)

            if pin == original_pin:
                if str(self.payment_amount) >= str(my_balance):
                    updated_my_balance = my_balance - self.pay_amount
                    updated_taker_balance = taker_balance + self.pay_amount

                    cursor.execute(
                        f"Update money_data set Balance = {updated_my_balance} where Phone_Number = {self.myphone_number}")
                    cursor.execute(
                        f"Update money_data set Balance = {updated_taker_balance} where Phone_Number = {self.taker_phone_no}")
                    mydb.commit()

                    self.done_image = PhotoImage(file="tick.png")
                    Label(payed_fr, image=self.done_image).place(x=138, y=10)

                    Left_Balance = "Left Balance -: " + str(updated_my_balance)
                    Label(payed_fr, text=Left_Balance, fg="black", bg="#5499C7", font=("Arial", 14, "bold")).place(x=80, y=170, width=260)

                else:
                    messagebox.showwarning("Warning!", "Not enough money")

            else:
                messagebox.showwarning("Error", "Wrong PIN!!!")
        except:
            messagebox.showwarning("Error", "Enter proper PIN!!!")



a(root)
root.mainloop()





def pay_qr_code():


    try:



        while 1:
            pay_amount = int(input("\nEnter the amount you want to pay -: "))



        print("\nLeft balance in your account is", updated_my_balance)

    except TypeError:
        print("\nNo account found")