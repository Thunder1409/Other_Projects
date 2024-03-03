import re
import tkinter
from tkinter import *
from tkinter import messagebox
import qrcode, inflect, cv2, os
from mysql.connector import connect

mydb = connect(user='root', password='Khushan', host='localhost', auth_plugin='mysql_native_password',
               database="paytm_data")
cursor = mydb.cursor()


def sign_up_button():
    first_name = set_first_name.get()
    if (not (first_name and first_name.strip())):
        Label(sing_up, text="*First Name -: ", fg="red", bg="#379683", font=("Arial", 11)).place(x=10, y=20)
    else:
        Label(sing_up, text="*First Name -: ", fg="snow", bg="#379683", font=("Arial", 11)).place(x=10, y=20)
        fn = True

    last_name = set_last_name.get()
    if (not (last_name and last_name.strip())):
        Label(sing_up, text="*Last Name -: ", fg="red", bg="#379683", font=("Arial", 11)).place(x=160, y=20)
    else:
        Label(sing_up, text="*Last Name -: ", fg="snow", bg="#379683", font=("Arial", 11)).place(x=160, y=20)
        ln = True

    try:
        phone_number = str(set_phone_number.get())
        try:
            cursor.execute(f"select Phone_Number from user_data where Phone_Number={phone_number}")
            original_phone_number = cursor.fetchone()[0]
            if original_phone_number == phone_number:
                messagebox.showerror("Error", "Number already exist")
            else:
                pass
        except:
            Label(sing_up, text="*Phone Number -: ", fg="snow", bg="#379683", font=("Arial", 11)).place(x=10, y=80)
            if len(phone_number) != 10:
                Label(sing_up, text="Enter 10 digit number", bg="#379683", fg="red").place(x=10, y=130)
            else:
                Label(sing_up, text="                                        ", bg="#379683", fg="snow").place(x=10,
                                                                                                               y=130)
                pn = True
    except:
        Label(sing_up, text="*Phone Number -: ", fg="red", bg="#379683", font=("Arial", 11)).place(x=10, y=80)

    email_id = set_email_id.get()
    if (not (email_id and email_id.strip())):
        Label(sing_up, text="*Email id -: ", fg="red", bg="#379683", font=("Arial", 11)).place(x=10, y=160)
    elif '@' not in email_id:
        Label(sing_up, text="Enter proper ID", bg="#379683", fg="red").place(x=10, y=212)
    elif ' ' in email_id:
        Label(sing_up, text="Enter proper ID", bg="#379683", fg="red").place(x=10, y=212)
    else:
        Label(sing_up, text="*Email id -: ", fg="snow", bg="#379683", font=("Arial", 11)).place(x=10, y=160)
        Label(sing_up, text="                                               ", bg="#379683", fg="snow").place(x=10,
                                                                                                              y=212)
        ei = True

    address = set_address.get()
    if (not (address and address.strip())):
        Label(sing_up, text="*Address -: ", fg="red", bg="#379683", font=("Arial", 11)).place(x=10, y=240)
    else:
        Label(sing_up, text="*Address -: ", fg="snow", bg="#379683", font=("Arial", 11)).place(x=10, y=240)
        a = True

    password = set_password.get()
    if (not (password and password.strip())):
        Label(sing_up, text="*Password -: ", fg="red", bg="#379683", font=("Arial", 11)).place(x=10, y=300)
    else:
        Label(sing_up, text="*Password -: ", fg="snow", bg="#379683", font=("Arial", 11)).place(x=10, y=300)
        p1 = True

    k = re.search('[A-Z]', password)
    if (k is None):
        Label(sing_up, text="Use capital letters", bg="#379683", fg="red").place(x=10, y=351)
    else:
        Label(sing_up, text="Use capital letters", bg="#379683", fg="snow").place(x=10, y=351)
        p2 = True

    k = re.search('[a-z]', password)
    if (k is None):
        Label(sing_up, text="Use small letters", bg="#379683", fg="red").place(x=10, y=381)
    else:
        Label(sing_up, text="Use small letters", bg="#379683", fg="snow").place(x=10, y=381)
        p3 = True

    k = re.search('[0-9]', password)
    if (k is None):
        Label(sing_up, text="Use numbers", bg="#379683", fg="red").place(x=10, y=366)
    else:
        Label(sing_up, text="Use numbers", bg="#379683", fg="snow").place(x=10, y=366)
        p4 = True

    if len(password) >= 10 and len(password) <= 20:
        Label(sing_up, text=" [10-20 digits] -: ", fg="snow", bg="#379683", font=("Arial", 11)).place(x=85, y=300)
        Label(sing_up, text="*Password -: ", fg="snow", bg="#379683", font=("Arial", 11)).place(x=10, y=300)
        p5 = True
    else:
        Label(sing_up, text=" [10-20 digits] -: ", fg="red", bg="#379683", font=("Arial", 11)).place(x=85, y=300)

    re_password = set_re_password.get()
    if (not (re_password and re_password.strip())):
        Label(sing_up, text="*Re Enter Password -: ", fg="red", bg="#379683", font=("Arial", 11)).place(x=10, y=405)
    elif re_password != password:
        Label(sing_up, text="not same", bg="#379683", fg="red").place(x=10, y=456)
        Label(sing_up, text="*Re Enter Password -: ", fg="snow", bg="#379683", font=("Arial", 11)).place(x=10, y=405)
    else:
        Label(sing_up, text="                   ", bg="#379683", fg="snow").place(x=10, y=456)
        Label(sing_up, text="*Re Enter Password -: ", fg="snow", bg="#379683", font=("Arial", 11)).place(x=10, y=405)
        rep = True

    try:
        adhar_number = str(set_adhar_number.get())
        Label(sing_up, text="*Adharar No. -:", fg="snow", bg="#379683", font=("Arial", 11)).place(x=160, y=80)
        if len(adhar_number) != 12:
            Label(sing_up, text="Enter 12 digits number", bg="#379683", fg="red").place(x=160, y=130)
        else:
            Label(sing_up, text="                                      ", bg="#379683", fg="snow").place(x=160, y=130,
                                                                                                         width=400)
            an = True
    except:
        Label(sing_up, text="*Adharar No. -:", fg="red", bg="#379683", font=("Arial", 11)).place(x=160, y=80)

    try:
        pin = str(set_pin.get())
        Label(sing_up, text="*Special pin -: ", fg="snow", bg="#379683", font=("Arial", 11)).place(x=10, y=475)
        if len(pin) != 4:
            Label(sing_up, text="Enter 4 digits only number", bg="#379683", fg="red").place(x=115, y=500)
        else:
            Label(sing_up, text=" ", bg="#379683", fg="snow").place(x=115, y=500, width=400)
            p = True
    except:
        Label(sing_up, text="*Special pin -: ", fg="red", bg="#379683", font=("Arial", 11)).place(x=10, y=475)

    try:
        if fn and ln and pn and an and p and ei and a and p1 and p2 and p3 and p4 and p5 and rep == True:
            insert_command = "INSERT INTO user_data(First_name, Last_name, Phone_Number, Mail_id, Adhar_card_number, Address, Set_Password, Special_Pin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            insert_values = (first_name, last_name, phone_number, email_id, adhar_number, address, password, pin)
            cursor.execute(insert_command, insert_values)
            mydb.commit()
            messagebox.showinfo("Done", "Account is created")
        else:
            pass
    except:
        pass


def sign_up_gui():
    Label(sing_up, text="*First Name -: ", fg="snow", bg="#379683", font=("Arial", 11)).place(x=10, y=20)
    Entry(sing_up, textvariable=set_first_name).place(x=12, y=45, height=25, width=115)

    Label(sing_up, text="*Last Name -: ", fg="snow", bg="#379683", font=("Arial", 11)).place(x=160, y=20)
    Entry(sing_up, textvariable=set_last_name).place(x=162, y=45, height=25, width=115)

    Label(sing_up, text="*Phone Number -: ", fg="snow", bg="#379683", font=("Arial", 11)).place(x=10, y=80)
    Entry(sing_up, textvariable=set_phone_number).place(x=12, y=105, height=25, width=115)

    Label(sing_up, text="*Adharar No. -:", fg="snow", bg="#379683", font=("Arial", 11)).place(x=160, y=80)
    Entry(sing_up, textvariable=set_adhar_number).place(x=162, y=105, height=25, width=115)

    Label(sing_up, text="*Email id -: ", fg="snow", bg="#379683", font=("Arial", 11)).place(x=10, y=160)
    Entry(sing_up, textvariable=set_email_id).place(x=12, y=185, height=26, width=250)

    Label(sing_up, text="*Address -: ", fg="snow", bg="#379683", font=("Arial", 11)).place(x=10, y=240)
    Entry(sing_up, textvariable=set_address).place(x=12, y=265, height=26, width=250)

    Label(sing_up, text="*Password  [10-20 digits] -: ", fg="snow", bg="#379683", font=("Arial", 11)).place(x=10, y=300)
    Entry(sing_up, textvariable=set_password, show="*").place(x=12, y=325, height=26, width=250)
    Label(sing_up, text="Use capital letters", bg="#379683", fg="snow").place(x=10, y=351)
    Label(sing_up, text="Use numbers", bg="#379683", fg="snow").place(x=10, y=366)
    Label(sing_up, text="Use small letters", bg="#379683", fg="snow").place(x=10, y=381)

    Label(sing_up, text="*Re Enter Password -: ", fg="snow", bg="#379683", font=("Arial", 11)).place(x=10, y=405)
    Entry(sing_up, textvariable=set_re_password, show="*").place(x=12, y=430, height=26, width=250)

    Label(sing_up, text="*Special pin -: ", fg="snow", bg="#379683", font=("Arial", 11)).place(x=10, y=475)
    Entry(sing_up, textvariable=set_pin).place(x=12, y=500, height=25, width=100)

    Button(sing_up, text="Sumbit", fg="snow", bg="#379683", font=("Arial", 15), command=sign_up_button).place(x=89,
                                                                                                              y=535,
                                                                                                              width=120)


root = Tk()
root.geometry("420x700")
root.configure(bg="#659DBD")  # LightCyan4

Label(text="Pay Money", fg="midnight blue", bg="#659DBD", font=("Arial", 25, "bold")).place(x=115, y=1, height=43)
Label(text="Create Account", bg="#659DBD", font=("Arial", 15, "bold")).place(x=130, y=60, width=148)

set_first_name, set_last_name, set_password, set_re_password, set_email_id, set_address = Variable(), Variable(), Variable(), Variable(), Variable(), Variable()
set_phone_number, set_adhar_number, set_pin = IntVar(), IntVar(), IntVar()
set_pin.set("")
set_phone_number.set("")
set_adhar_number.set("")

sing_up = Frame(root, bg="#379683", width=300, height=585)
sing_up.place(x=60, y=85)

sign_up_gui()

root.mainloop()
