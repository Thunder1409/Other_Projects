import qrcode, inflect, cv2, os
from mysql.connector import connect


my_phone_number = 1234
mydb = connect(user='root', password='Khushan', host='localhost', auth_plugin='mysql_native_password', database="paytm_data")
cursor = mydb.cursor()
p = inflect.engine()


def login():
    number = {"1234567890"}
    caps = {"QWERTYUIOPLKJHGFDSAZXCVBNM"}
    small = {"qwertyuioplkjhgfdsazxcvbnm"}

    while 1:
        try:
            phone_number = int(input("Enter your phone number -: "))
            if len(str(phone_number)) != 10:
                print("Enter the proper number\n")
            else:
                break
        except ValueError:
            print("Its mandatory to fill\n")

    while 1:
        set_password = input("Enter your password -: ")
        if (not (set_password and set_password.strip())):
            print("Its mandatory to fill\n")
        elif set_password in number:
            print("Use NUMBER in the password\n")
        elif set_password in caps:
            print("Use CAPITAL ALPHABET in the password\n")
        elif set_password in small:
            print("Use SMALL ALPHABET in the password\n")
        elif len(set_password) >= 10 and len(set_password) <= 20:
            break
        else:
            print("Not proper still. Try again \n")

def signin():
    print("\nNote -: ")
    print("All the fields are mandatory to fill.\n")
    number = {'1234567890'}
    caps = {'QWERTYUIOPLKJHGFDSAZXCVBNM'}
    small = {'qwertyuioplkjhgfdsazxcvbnm'}

    while 1:
        first_name = input("Enter your first name -: ")
        if (not (first_name and first_name.strip())):
            print("Its mandatory to fill\n")
        else:
            break

    while 1:
        last_name = input("Enter your last name -: ")
        if (not (last_name and last_name.strip())):
            print("Its mandatory to fill\n")
        else:
            break

    while 1:
        try:
            phone_number = int(input("Enter your phone number -: "))
            if len(str(phone_number)) != 10:
                print("Enter the proper number\n")
            else:
                break
        except ValueError:
            print("Its mandatory to fill\n")

    while 1:
        mail_id = input("Enter your mail id -: ")
        if (not (mail_id and mail_id.strip())):
            print("Its mandatory to fill\n")
        elif '@' not in mail_id:
            print("Enter proper mail id\n")
        else:
            break

    while 1:
        try:
            adhar_card_number = int(input("Enter your Adhar card number -: "))
            if len(str(adhar_card_number)) != 12:
                print("Enter the proper number\n")
            else:
                break
        except ValueError:
            print("Its mandatory to fill\n")

    while 1:
        address = input("Enter your address -: ")
        if (not (address and address.strip())):
            print("Its mandatory to fill\n")
        else:
            break

    print("\nNote -: \nLength of password must be between 10 to 20 \n")
    while 1:
        set_password = input("Enter your password -: ")
        if (not (set_password and set_password.strip())):
            print("Its mandatory to fill\n")
        elif set_password in number:
            print("Use NUMBER in the password\n")
        elif set_password in caps:
            print("Use CAPITAL ALPHABET in the password\n")
        elif set_password in small:
            print("Use SMALL ALPHABET in the password\n")
        elif len(set_password) >= 10 and len(set_password) <= 20:
            break
        else:
            print("Not proper still. Try again \n")

    while 1:
        try:
            special_pin = int(input("Enter your special four digit pin -: "))
            if len(str(special_pin)) != 4:
                print("Enter the proper PIN\n")
            else:
                break
        except ValueError:
            print("Its mandatory to fill\n")

def check_balance():
    phone_number = int(input("Enter your phone number"))
    cursor.execute(f"select Balance from money_data where Phone_Number = {phone_number}")
    try:
        Balance = cursor.fetchone()[0]
        print("\nYour left balance is -:", Balance)
        Balance_word = p.number_to_words(Balance)
        print(Balance_word, "only")

    except TypeError:
        print("\nNo account found")
        print("Please create your account")

def pay_qr_code():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    while True:
        _, img = cap.read()
        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            taker_phone_no = data
            break
        cv2.imshow("QRCODEscanner", img)
        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

    cursor.execute(f"select Balance from money_data where Phone_Number = {taker_phone_no}")
    try:
        taker_balance = cursor.fetchone()[0]
        cursor.execute(f"select Balance from money_data where Phone_Number = {my_phone_number}")
        my_balance = cursor.fetchone()[0]
        Balance_word = p.number_to_words(my_balance)
        print("\nYour Balance ", my_balance)
        print(Balance_word, "only")
        while 1:
            pay_amount = int(input("\nEnter the amount you want to pay -: "))
            if pay_amount > my_balance:
                print("Not enough money")

            else:
                break

        updated_my_balance, updated_taker_balance = my_balance - pay_amount, taker_balance + pay_amount
        print(updated_taker_balance, updated_my_balance)
        cursor.execute(
            f"Update money_data set Balance = {updated_my_balance} where Phone_Number = {my_phone_number}")
        cursor.execute(
            f"Update money_data set Balance = {updated_taker_balance} where Phone_Number = {taker_phone_no}")
        mydb.commit()
        print("\nLeft balance in your account is", updated_my_balance)

    except TypeError:
        print("\nNo account found")

def pay_phone_number():
    while 1:
        taker_phone_no = int(input("Enter the Phone number -: "))
        if taker_phone_no == my_phone_number:
            print("Don't enter your phone number")

        else:
            break

    cursor.execute(f"select Balance from money_data where Phone_Number = {taker_phone_no}")
    try:
        taker_balance = cursor.fetchone()[0]
        cursor.execute(f"select Balance from money_data where Phone_Number = {my_phone_number}")
        my_balance = cursor.fetchone()[0]
        Balance_word = p.number_to_words(my_balance)
        print("\nYour Balance ", my_balance)
        print(Balance_word, "only")
        while 1:
            pay_amount = int(input("\nEnter the amount you want to pay -: "))
            if pay_amount > my_balance:
                print("Not enough money")

            else:
                break

        updated_my_balance, updated_taker_balance = my_balance - pay_amount, taker_balance + pay_amount
        print(updated_taker_balance, updated_my_balance)
        cursor.execute(
            f"Update money_data set Balance = {updated_my_balance} where Phone_Number = {my_phone_number}")
        cursor.execute(
            f"Update money_data set Balance = {updated_taker_balance} where Phone_Number = {taker_phone_no}")
        mydb.commit()
        print("\nLeft balance in your account is", updated_my_balance)

    except TypeError:
        print("\nNo account found")

def qr_code_generator():
    while 1:
        taker_phone_no = int(input("Enter the Phone number -: "))
        if taker_phone_no == my_phone_number:
            print("Don't enter your phone number")

        else:
            break

    a = taker_phone_no
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=2,
    )
    qr.add_data(a)
    qr.make(fit=True)

    img = qr.make_image(back_color="#5499C7", fill_color='black')
    img.save("test.png")
    image = cv2.imread("Money_pay(GUI)/test.png")
    cv2.imshow("Qr_Code", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    os.remove("test.png")

pay_qr_code()