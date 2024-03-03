from tkinter import *

def click(number):
    global text_value
    if number == "AC":
        text_value.set("")

    elif number == "C":
        text_value.set("")

    elif number == "+/-":
        print("Not working")

    elif number == "=":
        if text_value.get().isdigit():
            value = int(text_value.get())
        else:
            try:
                value = eval(text_value.get())
            except Exception as e:
                value = "ERROR"

            text_value.set(value)



    else:
        text_value.set(text_value.get() + str(number))





root = Tk()
height = 240
width = 260
fore_ground = "black"
back_ground = "light gray"


root.title("CALCULATOR")
root.geometry("260x240")

root.maxsize(width, height)
root.minsize(width, height)
root.configure(bg="gray96")



text_value = StringVar()
text = Entry(root, fg=fore_ground, bg=back_ground, textvariable=text_value).place(x=5, y=5, height=50, width=250)

line = Canvas(root, width=250, height=1, bg=fore_ground).place(x=3, y=57)


b_ac = Button(root, text="AC", fg=fore_ground, bg=back_ground, borderwidth=0, activebackground=back_ground, command=lambda:click("AC")).place(x=5, y=65, width=58.7, height=30)
b_c = Button(root, text="C", fg=fore_ground, bg=back_ground, borderwidth=0, activebackground=back_ground, command=lambda:click("C")).place(x=68.7, y=65, width=58.7, height=30)
b_p_n = Button(root, text="+/-", fg=fore_ground, bg=back_ground, borderwidth=0, activebackground=back_ground, command=lambda:click("+/-")).place(x=132.4, y=65, width=58.7, height=30)
b_d = Button(root, text="/", fg=fore_ground, bg=back_ground, borderwidth=0, activebackground=back_ground, command=lambda:click("/")).place(x=196.1, y=65, width=58.7, height=30)

b_7 = Button(root, text="7", fg=fore_ground, bg=back_ground, borderwidth=0, activebackground=back_ground, command=lambda:click(7)).place(x=5, y=100, width=58.7, height=30)
b_8 = Button(root, text="8", fg=fore_ground, bg=back_ground, borderwidth=0, activebackground=back_ground, command=lambda:click(8)).place(x=68.7, y=100, width=58.7, height=30)
b_9 = Button(root, text="9", fg=fore_ground, bg=back_ground, borderwidth=0, activebackground=back_ground, command=lambda:click(9)).place(x=132.4, y=100, width=58.7, height=30)
b_x = Button(root, text="*", fg=fore_ground, bg=back_ground, borderwidth=0, activebackground=back_ground, command=lambda:click("*")).place(x=196.1, y=100, width=58.7, height=30)

b_4 = Button(root, text="4", fg=fore_ground, bg=back_ground, borderwidth=0, activebackground=back_ground, command=lambda:click(4)).place(x=5, y=135, width=58.7, height=30)
b_5 = Button(root, text="5", fg=fore_ground, bg=back_ground, borderwidth=0, activebackground=back_ground, command=lambda:click(5)).place(x=68.7, y=135, width=58.7, height=30)
b_6 = Button(root, text="6", fg=fore_ground, bg=back_ground, borderwidth=0, activebackground=back_ground, command=lambda:click(6)).place(x=132.4, y=135, width=58.7, height=30)
b_s = Button(root, text="-", fg=fore_ground, bg=back_ground, borderwidth=0, activebackground=back_ground, command=lambda:click("-")).place(x=196.1, y=135, width=58.7, height=30)

b_1 = Button(root, text="1", fg=fore_ground, bg=back_ground, borderwidth=0, activebackground=back_ground, command=lambda:click(1)).place(x=5, y=170, width=58.7, height=30)
b_2 = Button(root, text="2", fg=fore_ground, bg=back_ground, borderwidth=0, activebackground=back_ground, command=lambda:click(2)).place(x=68.7, y=170, width=58.7, height=30)
b_3 = Button(root, text="3", fg=fore_ground, bg=back_ground, borderwidth=0, activebackground=back_ground, command=lambda:click(3)).place(x=132.4, y=170, width=58.7, height=30)
b_a = Button(root, text="+", fg=fore_ground, bg=back_ground, borderwidth=0, activebackground=back_ground, command=lambda:click("+")).place(x=196.1, y=170, width=58.7, height=30)

b_p = Button(root, text="%", fg=fore_ground, bg=back_ground, borderwidth=0, activebackground=back_ground, command=lambda:click("%")).place(x=5, y=205, width=58.7, height=30)
b_0 = Button(root, text="0", fg=fore_ground, bg=back_ground, borderwidth=0, activebackground=back_ground, command=lambda:click(0)).place(x=68.7, y=205, width=58.7, height=30)
b_dot = Button(root, text=".", fg=fore_ground, bg=back_ground, borderwidth=0, activebackground=back_ground, command=lambda:click(".")).place(x=132.4, y=205, width=58.7, height=30)
b_e = Button(root, text="=", fg=fore_ground, bg=back_ground, borderwidth=0, activebackground=back_ground, command=lambda:click("=")).place(x=196.1, y=205, width=58.7, height=30)


root.mainloop()