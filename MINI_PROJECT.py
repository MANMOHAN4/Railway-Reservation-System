from tkinter import*
import tkinter.messagebox as tmsg
from tkinter import filedialog
from PIL import Image, ImageDraw
import random
import string

root = Tk()
root.title("RAILWAY RESERVATION SYSTEM")
root.geometry("1920x1080")
root.minsize(1400,786)
root.configure(bg="light cyan")

Label(root, text="RAILWAY RESERVATION SYSTEM", font="HANSON 44", fg="black", bg="light cyan").pack(side=TOP)

photo = PhotoImage(file="C:/Users/MANMOHAN C A/Downloads/44.png")
f1 = Frame(width=884, height=952)
f1.pack(side=LEFT, anchor="nw")
Label(f1, image=photo, bg="light cyan").pack()

qr=PhotoImage(file="C:/Users/MANMOHAN C A/Downloads/qr.png")
accomodation=PhotoImage(file="C:/Users/MANMOHAN C A/Downloads/Hotels.png")
vehicle=PhotoImage(file="C:/Users/MANMOHAN C A/Downloads/Taxis.png")

def war():
    tmsg.showwarning("SUBMIT", "PLEASE CHECK THE CREDENTIALS ONCE")

def new():
    def save_to_file(username, password):
        with open('C:/Users/MANMOHAN C A/Desktop/new.txt', "a") as file:
            file.write(f"Username: {username.get()}, Password: {password.get()}\n")

    def create():
        a = tmsg.askquestion("SUBMIT", "ARE YOU SURE")
        if a == "yes":
            save_to_file(cuser, pas)
            b = "ACCOUNT CREATED SUCCESSFULLY!"
            login()
        else:
            b = "TRY AGAIN!"
        tmsg.showinfo("SUBMIT", b)

    f3 = Frame(root, width=584, height=384)
    f3.place(x=784, y=244)
    c2 = Canvas(f3, bg="lavender blush", width=584, height=384)
    c2.pack()

    c2.create_text(294, 28, text="NEW ACCOUNT", font="HANSON 24", fill="deep pink")
    c2.create_text(88, 80, text="Name:", font="HANSON 18", anchor="nw", fill="deep sky blue")
    c2.create_text(88, 120, text="Mail Id:", font="HANSON 18", anchor="nw", fill="deep sky blue")
    c2.create_text(88, 160, text="Password:", font="HANSON 18", anchor="nw", fill="deep sky blue")
    c2.create_text(88, 200, text="Age:", font="HANSON 18", anchor="nw", fill="deep sky blue")
    c2.create_text(88, 240, text="Mobile No:", font="HANSON 18", anchor="nw", fill="deep sky blue")

    ck = IntVar()
    cb = Checkbutton(c2, text="ACCEPT TERMS AND CONDITIONS", variable=ck, command=war, bg="mint cream")
    c2.create_window(184, 294, window=cb, anchor="nw")

    cuser = StringVar()
    mail = StringVar()
    pas = StringVar()
    age = IntVar()
    num = IntVar()

    if not cuser or not mail or not pas or not age or not num:
        tmsg.showerror("Error", "Please fill in all fields.")
        return

    e1 = Entry(c2, textvariable=cuser, bg="snow", fg="black", font=8, width=28)
    e2 = Entry(c2, textvariable=mail, bg="snow", fg="black", font=8, width=28)
    e3 = Entry(c2, textvariable=pas, bg="snow", fg="black", font=8)
    e4 = Entry(c2, textvariable=age, bg="snow", fg="black", font=8)
    e5 = Entry(c2, textvariable=num, bg="snow", fg="black", font=8)

    c2.create_window(210, 82, window=e1, anchor="nw")
    c2.create_window(210, 122, window=e2, anchor="nw")
    c2.create_window(281, 162, window=e3, anchor="nw")
    c2.create_window(281, 202, window=e4, anchor="nw")
    c2.create_window(281, 242, window=e5, anchor="nw")

    b3 = Button(c2, text="CREATE", font="HANSON 14", bg="azure", fg="black", command=create,  cursor="hand2")
    c2.create_window(218, 334, window=b3, anchor="nw")

    b4 = Button(c2, text="BACK", font="HANSON 12", bg="misty rose", fg="gray48", command=home,  cursor="hand2")
    c2.create_window(444, 338, window=b4, anchor="ne")

def login():
    def check_credentials():
        entered_username = luser.get()
        entered_password = lpas.get()

        with open("C:/Users/MANMOHAN C A/Desktop/new.txt", "r") as file:
            for line in file:
                if f"Username: {entered_username}, Password: {entered_password}" in line:
                    return True
        return False

    def sign_in():
        if not luser or not lpas:
            tmsg.showerror("Error", "Please enter both username and password.")
            return

        if check_credentials():
            sign()
        else:
            tmsg.showerror("Error", "Invalid username or password.")

    f4 = Frame(root, width=584, height=384)
    f4.place(x=784, y=244)
    c3 = Canvas(f4, bg="lavender blush", width=584, height=384)
    c3.pack()

    c3.create_text(294, 34, text="Welcome Back!", font="HANSON 24", fill="deep pink")

    luser=StringVar()
    lpas=StringVar()

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name == '':
            user.insert(0,'Username')

    user = Entry(c3,width=34, textvariable=luser,bg="lavender blush", fg="black", font=8, border=0)
    user.insert(0,"Username")
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>", on_leave)
    c3.create_window(138, 104, window=user, anchor="nw")
    Frame(c3,width=324,height=2,bg="deep pink").place(x=133,y=128)

    def on_enter(e):
        pasw.delete(0, 'end')

    def on_leave(e):
        name=pasw.get()
        if name == '':
            user.insert(0,'Password')

    pasw = Entry(c3, width=34,textvariable=lpas, bg="lavender blush", fg="black", font=8, border=0)
    pasw.insert(0, "Password")
    pasw.bind("<FocusIn>", on_enter)
    pasw.bind("<FocusOut>", on_leave)
    c3.create_window(138, 174, window=pasw, anchor="nw")
    Frame(c3, width=324, height=2, bg="deep pink").place(x=133, y=198)

    b5 = Button(c3, width=18, text="Log in", font="HANSON 14", bg="azure", fg="black",border=1,command=sign_in,  cursor="hand2")
    c3.create_window(138, 234, window=b5, anchor="nw")
    c3.create_text(158, 304, text="Don't have an account?", font=("Microsoft YaHei UI Light",10, "bold"), anchor="nw", fill="DeepPink2")

    b6 = Button(c3, width=8, text="Sign up", font=("Microsoft YaHei UI Light",12, "bold"),  cursor="hand2", bg="lavender blush", activebackground="lavender blush", fg="deep sky blue", border=0, command=new)
    c3.create_window(328, 296, window=b6, anchor="nw")

def sign():
    f5 = Frame(root, width=904, height=684,bg="light cyan")
    f5.place(x=608, y=84)
    c4 = Canvas(f5, bg="light cyan", width=904, height=684, highlightbackground="light cyan")
    c4.pack()
    b7 = Button(c4, text="Trains", font="HANSON 18", bg="misty rose", fg="black",command=train_list, border=1, width=8, height=1,  cursor="hand2", relief=RAISED)
    c4.create_window(248, 184, window=b7, anchor="nw")

    b8 = Button(c4, text="Meals", font="HANSON 18", bg="misty rose", fg="black", command=meals, border=1, relief=RAISED, width=8, height=1, cursor="hand2")
    c4.create_window(248, 284, window=b8, anchor="nw")

    b15 = Button(c4, text="FAQ's", font="HANSON 18", bg="misty rose", fg="black", command=faq, border=1, relief=RAISED,
                width=8, height=1, cursor="hand2")
    c4.create_window(248, 384, window=b15, anchor="nw")

    b19 = Button(c4, text="Book Ticket", font="HANSON 18", bg="misty rose", fg="black", command=book1, border=1, relief=RAISED,
                 width=12, height=1, cursor="hand2")
    c4.create_window(454, 184, window=b19, anchor="nw")

    b24 = Button(c4, text="Cancel Ticket", font="HANSON 18", bg="misty rose", fg="black", command=cancel1, border=1,
                 relief=RAISED,
                 width=12, height=1, cursor="hand2")
    c4.create_window(454, 284, window=b24, anchor="nw")

    b32 = Button(c4, text="Taxi", font="HANSON 18", bg="misty rose", fg="black", command=taxi, border=1, relief=RAISED,
                 width=8, height=1, cursor="hand2")
    c4.create_window(248, 484, window=b32, anchor="nw")

    b33 = Button(c4, text="Hotels", font="HANSON 18", bg="misty rose", fg="black", command=hotel, border=1,
                 relief=RAISED,
                 width=12, height=1, cursor="hand2")
    c4.create_window(454, 384, window=b33, anchor="nw")

    b36 = Button(c4, text="Log Out", font="HANSON 18", bg="misty rose", fg="black", command=login, border=1,
                 relief=RAISED,
                 width=12, height=1, cursor="hand2")
    c4.create_window(454, 484, window=b36, anchor="nw")

def train_list():
    f6 = Frame(root,  width=904, height=494, bg="light cyan")
    f6.place(x=608, y=174)
    c5 = Canvas(f6, bg="lavender blush", width=904, height=478)
    c5.pack()

    l1=Label(c5, text="Train Number", fg='firebrick1', bg="lavender blush", font="HANSON 15", relief=RAISED, border=1,height=2)
    c5.create_window(1, 1, window=l1, anchor="nw")
    l2 = Label(c5, text="Train Name", fg='firebrick1', bg="lavender blush", font="HANSON 15", relief=RAISED, border=1,height=2 )
    c5.create_window(208, 1, window=l2, anchor="nw")
    l3 = Label(c5, text="Capacity",fg='firebrick1', bg="lavender blush", font="HANSON 15", relief=RAISED, border=1,height=2 )
    c5.create_window(381, 1, window=l3, anchor="nw")
    l4 = Label(c5, text="Departure", fg='firebrick1', bg="lavender blush", font="HANSON 15", relief=RAISED, border=1, height=2)
    c5.create_window(519, 1, window=l4, anchor="nw")
    l5 = Label(c5, text="Destination", fg='firebrick1', bg="lavender blush", font="HANSON 15", relief=RAISED, border=1, height=2)
    c5.create_window(679, 1, window=l5, anchor="nw")
    l6 = Label(c5, text="Drn", fg='firebrick1', bg="lavender blush", font="HANSON 15", relief=RAISED, border=1, height=2)
    c5.create_window(851, 1, window=l6, anchor="nw")
    l7 = Label(c5, text="3587482", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN, border=1, width= 15, height=2 )
    c5.create_window(4, 56, window=l7, anchor="nw")
    l8 = Label(c5, text="347583", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN, border=1, width=15, height=2)
    c5.create_window(4, 116, window=l8, anchor="nw")
    l9 = Label(c5, text="234838", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN, border=1,
               width=15, height=2)
    c5.create_window(4, 176, window=l9, anchor="nw")
    l10 = Label(c5, text="234785", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN, border=1,
               width=15, height=2)
    c5.create_window(4, 236, window=l10, anchor="nw")
    l11 = Label(c5, text="438743", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN, border=1,
               width=15, height=2)
    c5.create_window(4, 296, window=l11, anchor="nw")
    l12 = Label(c5, text="443494", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN, border=1,
               width=15, height=2)
    c5.create_window(4, 356, window=l12, anchor="nw")
    l13 = Label(c5, text="324738", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN, border=1,
                width=15, height=2)
    c5.create_window(4, 416, window=l13, anchor="nw")
    l14 = Label(c5, text="Hindustan\nExpress", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN, border=1, width=12)
    c5.create_window(212, 56, window=l14, anchor="nw")
    l15 = Label(c5, text="Shatabdi\nExpress", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN,
                border=1, width=12)
    c5.create_window(212, 116, window=l15, anchor="nw")
    l16 = Label(c5, text="Duronto\nExpress", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN,
                border=1, width=12)
    c5.create_window(212, 176, window=l16, anchor="nw")
    l17 = Label(c5, text="Garib\nRath", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN,
                border=1, width=12)
    c5.create_window(212, 236, window=l17, anchor="nw")
    l18 = Label(c5, text="Humsafar\nExpress", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN,
                border=1, width=12)
    c5.create_window(212, 296, window=l18, anchor="nw")
    l19 = Label(c5, text="Jan\nShatabdi", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN,
                border=1, width=12)
    c5.create_window(212, 356, window=l19, anchor="nw")
    l20 = Label(c5, text="Tejas\nExpress", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN,
                border=1, width=12)
    c5.create_window(212, 416, window=l20, anchor="nw")
    l21 = Label(c5, text="532", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN, border=1,
               width=9, height=2)
    c5.create_window(388, 56, window=l21, anchor="nw")
    l22 = Label(c5, text="345", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN, border=1,
               width=9, height=2)
    c5.create_window(388, 116, window=l22, anchor="nw")
    l23 = Label(c5, text="420", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN, border=1,
               width=9, height=2)
    c5.create_window(388, 176, window=l23, anchor="nw")
    l24 = Label(c5, text="334", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN, border=1,
                width=9, height=2)
    c5.create_window(388, 236, window=l24, anchor="nw")
    l25 = Label(c5, text="435", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN, border=1,
                width=9, height=2)
    c5.create_window(388, 296, window=l25, anchor="nw")
    l26 = Label(c5, text="343", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN, border=1,
                width=9, height=2)
    c5.create_window(388, 356, window=l26, anchor="nw")
    l27 = Label(c5, text="543", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN, border=1,
                width=9, height=2)
    c5.create_window(388, 416, window=l27, anchor="nw")
    l28 = Label(c5, text="New Delhi", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN,
                border=1, width=12, height=2)
    c5.create_window(518, 56, window=l28, anchor="nw")
    l29 = Label(c5, text="Chennai", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN,
                border=1, width=12, height=2)
    c5.create_window(518, 116, window=l29, anchor="nw")
    l30 = Label(c5, text="Kolkata", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN,
                border=1, width=12, height=2)
    c5.create_window(518, 176, window=l30, anchor="nw")
    l31 = Label(c5, text="Pune", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN,
                border=1, width=12, height=2)
    c5.create_window(518, 236, window=l31, anchor="nw")
    l32 = Label(c5, text="Hyderabad", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN,
                border=1, width=12, height=2)
    c5.create_window(518, 296, window=l32, anchor="nw")
    l33 = Label(c5, text="Jaipur", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN,
                border=1, width=12, height=2)
    c5.create_window(518, 356, window=l33, anchor="nw")
    l34 = Label(c5, text="Mysuru", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN,
                border=1, width=12, height=2)
    c5.create_window(518, 416, window=l34, anchor="nw")
    l35 = Label(c5, text="Mumbai", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN,
                border=1, width=12, height=2)
    c5.create_window(684, 56, window=l35, anchor="nw")
    l36 = Label(c5, text="Bangalore", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN,
                border=1, width=12, height=2)
    c5.create_window(684, 116, window=l36, anchor="nw")
    l37 = Label(c5, text="Delhi", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN,
                border=1, width=12, height=2)
    c5.create_window(684, 176, window=l37, anchor="nw")
    l38 = Label(c5, text="Ahmedabad", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN,
                border=1, width=12, height=2)
    c5.create_window(684, 236, window=l38, anchor="nw")
    l39 = Label(c5, text="Bhopal", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN,
                border=1, width=12, height=2)
    c5.create_window(684, 296, window=l39, anchor="nw")
    l40 = Label(c5, text="Lucknow", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN,
                border=1, width=12, height=2)
    c5.create_window(684, 356, window=l40, anchor="nw")
    l41 = Label(c5, text="Chennai", fg='deep pink', bg="snow", font=("Arial Black", 14), relief=SUNKEN,
                border=1, width=12, height=2)
    c5.create_window(684, 416, window=l41, anchor="nw")
    l42 = Label(c5, text="12 hrs", fg='deep pink', bg="snow", font=("Arial Black", 10), relief=SUNKEN,
                border=1, width=5, height=3)
    c5.create_window(853, 56, window=l42, anchor="nw")
    l43 = Label(c5, text="6 hrs", fg='deep pink', bg="snow", font=("Arial Black", 10), relief=SUNKEN,
                border=1, width=5, height=3)
    c5.create_window(853, 116, window=l43, anchor="nw")
    l44 = Label(c5, text="10 hrs", fg='deep pink', bg="snow", font=("Arial Black", 10), relief=SUNKEN,
                border=1, width=5, height=3)
    c5.create_window(853, 176, window=l44, anchor="nw")
    l45 = Label(c5, text="8 hrs", fg='deep pink', bg="snow", font=("Arial Black", 10), relief=SUNKEN,
                border=1, width=5, height=3)
    c5.create_window(853, 236, window=l45, anchor="nw")
    l46 = Label(c5, text="14 hrs", fg='deep pink', bg="snow", font=("Arial Black", 10), relief=SUNKEN,
                border=1, width=5, height=3)
    c5.create_window(853, 296, window=l46, anchor="nw")
    l47 = Label(c5, text="9 hrs", fg='deep pink', bg="snow", font=("Arial Black", 10), relief=SUNKEN,
                border=1, width=5, height=3)
    c5.create_window(853, 356, window=l47, anchor="nw")
    l48 = Label(c5, text="5 hrs", fg='deep pink', bg="snow", font=("Arial Black", 10), relief=SUNKEN,
                border=1, width=5, height=3)
    c5.create_window(853, 416, window=l48, anchor="nw")
    b9=Button(f6, text="BACK", font="HANSON 12", bg="azure", fg="gray21", command=sign,  cursor="hand2")
    b9.pack(side=BOTTOM)

def veg_menu():
    f8 = Frame(root, width=584, height=384)
    f8.place(x=784, y=244)
    c7 = Canvas(f8, bg="lavender blush", width=584, height=384)
    c7.pack()
    c7.create_text(294, 28, text="Vegetarian Recipes", font="HANSON 28", fill="green3")
    v1=Label(c7,text="Veg Biryani",fg='deep pink', bg="snow", font=("Arial Black", 18), relief=SUNKEN,
                border=1, width=21)
    c7.create_window(21, 84, window=v1, anchor="nw")
    v2 = Label(c7, text="Paneer Fried Rice", fg='deep pink', bg="snow", font=("Arial Black", 18), relief=SUNKEN,
               border=1, width=21)
    c7.create_window(21, 134, window=v2, anchor="nw")
    v3 = Label(c7, text="Veg Roll", fg='deep pink', bg="snow", font=("Arial Black", 18), relief=SUNKEN,
               border=1, width=21)
    c7.create_window(21, 184, window=v3, anchor="nw")
    v4 = Label(c7, text="Butter Naan With Curry", fg='deep pink', bg="snow", font=("Arial Black", 18), relief=SUNKEN,
               border=1, width=21)
    c7.create_window(21, 234, window=v4, anchor="nw")
    v5 = Label(c7, text="Mushroom Manchurian", fg='deep pink', bg="snow", font=("Arial Black", 18), relief=SUNKEN,
               border=1, width=21)
    c7.create_window(21, 284, window=v5, anchor="nw")
    v6 = Label(c7, text="₹ 150", fg='deep pink', bg="snow", font=("Arial Black", 18), relief=SUNKEN,
               border=1, width=8)
    c7.create_window(404, 84, window=v6, anchor="nw")
    v7 = Label(c7, text="₹ 180", fg='deep pink', bg="snow", font=("Arial Black", 18), relief=SUNKEN,
               border=1, width=8)
    c7.create_window(404, 134, window=v7, anchor="nw")
    v8 = Label(c7, text="₹ 120", fg='deep pink', bg="snow", font=("Arial Black", 18), relief=SUNKEN,
               border=1, width=8)
    c7.create_window(404, 184, window=v8, anchor="nw")
    v9 = Label(c7, text="₹ 200", fg='deep pink', bg="snow", font=("Arial Black", 18), relief=SUNKEN,
               border=1, width=8)
    c7.create_window(404, 234, window=v9, anchor="nw")
    v10 = Label(c7, text="₹ 170", fg='deep pink', bg="snow", font=("Arial Black", 18), relief=SUNKEN,
               border=1, width=8)
    c7.create_window(404, 284, window=v10, anchor="nw")
    b12 = Button(c7, text="BACK", font="HANSON 12", bg="PaleGreen1", fg="gray21", command=meals, cursor="hand2")
    c7.create_window(248, 348, window=b12, anchor="nw")

def non_veg_menu():
    f9 = Frame(root, width=584, height=384)
    f9.place(x=784, y=244)
    c8 = Canvas(f9, bg="lavender blush", width=584, height=384)
    c8.pack()
    c8.create_text(294, 28, text="Non-Veg Recipes", font="HANSON 28", fill="OrangeRed1")
    n1 = Label(c8, text="Chicken Biryani", fg='deep pink', bg="snow", font=("Arial Black", 18), relief=SUNKEN,
               border=1, width=21)
    c8.create_window(21, 84, window=n1, anchor="nw")
    n2 = Label(c8, text="Chicken Kebab", fg='deep pink', bg="snow", font=("Arial Black", 18), relief=SUNKEN,
               border=1, width=21)
    c8.create_window(21, 134, window=n2, anchor="nw")
    n3 = Label(c8, text="Butter Chicken With Naan", fg='deep pink', bg="snow", font=("Arial Black", 18), relief=SUNKEN,
               border=1, width=21)
    c8.create_window(21, 184, window=n3, anchor="nw")
    n4 = Label(c8, text="Fish Fry", fg='deep pink', bg="snow", font=("Arial Black", 18), relief=SUNKEN,
               border=1, width=21)
    c8.create_window(21, 234, window=n4, anchor="nw")
    n5 = Label(c8, text="Chicken Manchurian", fg='deep pink', bg="snow", font=("Arial Black", 18), relief=SUNKEN,
               border=1, width=21)
    c8.create_window(21, 284, window=n5, anchor="nw")
    n6 = Label(c8, text="₹ 170", fg='deep pink', bg="snow", font=("Arial Black", 18), relief=SUNKEN,
               border=1, width=8)
    c8.create_window(404, 84, window=n6, anchor="nw")
    n7 = Label(c8, text="₹ 150", fg='deep pink', bg="snow", font=("Arial Black", 18), relief=SUNKEN,
               border=1, width=8)
    c8.create_window(404, 134, window=n7, anchor="nw")
    n8 = Label(c8, text="₹ 200", fg='deep pink', bg="snow", font=("Arial Black", 18), relief=SUNKEN,
               border=1, width=8)
    c8.create_window(404, 184, window=n8, anchor="nw")
    n9 = Label(c8, text="₹ 210", fg='deep pink', bg="snow", font=("Arial Black", 18), relief=SUNKEN,
               border=1, width=8)
    c8.create_window(404, 234, window=n9, anchor="nw")
    n10 = Label(c8, text="₹ 190", fg='deep pink', bg="snow", font=("Arial Black", 18), relief=SUNKEN,
                border=1, width=8)
    c8.create_window(404, 284, window=n10, anchor="nw")
    b13 = Button(c8, text="BACK", font="HANSON 12", bg="light salmon", fg="gray21", command=meals, cursor="hand2")
    c8.create_window(248, 348, window=b13, anchor="nw")

def meals():
    f7 = Frame(root,  width=584, height=384)
    f7.place(x=784, y=244)
    c6 = Canvas(f7, bg="lavender blush", width=584, height=384)
    c6.pack()
    c6.create_text(288, 28, text="Meals", font="HANSON 28", fill="deep pink")
    c6.create_text(288, 118, text="Choose one among\n      the following", font=("Arial Black", 18), fill="MediumOrchid")
    b10 = Button(c6, text="Veg", font="HANSON 18", bg="thistle1", fg="black", command=veg_menu, border=1, width=8, height=1, cursor="hand2", relief=RAISED)
    c6.create_window(201, 184, window=b10, anchor="nw")
    b11 = Button(c6, text="Non-Veg", font="HANSON 18", bg="thistle1", fg="black", command=non_veg_menu, border=1, relief=RAISED, width=12, height=1, cursor="hand2")
    c6.create_window(158, 248, window=b11, anchor="nw")
    b14 = Button(c6, text="BACK", font="HANSON 12", bg="azure", fg="gray21", command=sign, cursor="hand2")
    c6.create_window(248, 324, window=b14, anchor="nw")

def faq():
    f10 = Frame(root, width=904, height=684, bg="light cyan")
    f10.place(x=608, y=84)
    c9 = Canvas(f10, bg="lavender blush", width=904, height=684, highlightbackground="black")
    c9.pack()
    c9.create_text(452, 24, text="FAQ's", font="HANSON 28", fill="firebrick1")
    c9.create_text(428, 104, text="(1) How many passengers can be booked in a single ticket/transaction?\n--> A maximum of 6 passengers", font=("Arial Black", 15), fill="blue")
    c9.create_text(318, 224,
                   text="(2) How are payments made for online reservation?\n--> The following modes are available:\n    - Credit/Debit Card\n    - GPay/PhonePe\n    - UPI transfer",
                   font=("Arial Black", 15), fill="blue")
    c9.create_text(412, 344,
                   text="(3) What is the cancellation policy? What is the cancellation charge?\n--> Yes, you can cancel the ticket by putting your PNR number ",
                   font=("Arial Black", 15), fill="blue")
    c9.create_text(354, 438,
                   text="(4) Does the railways give a discount for children?\n--> Yes, half the price of the ticket is charged for children\n     below the age of 10 years",
                   font=("Arial Black", 15), fill="blue")
    c9.create_text(404, 568,
                   text="(5) What happens if my ticket does not reach me through my mail?\n--> Please contact on the mentioned mail id clearly stating the\n     unique code entered by you during reservation and the name\n     of passenger(s): tickets@trainreservation.com)",
                   font=("Arial Black", 15), fill="blue")
    b16 = Button(c9, text="BACK", font="HANSON 15", bg="azure", fg="gray21", command=sign, cursor="hand2")
    c9.create_window(8, 664, window=b16, anchor="w")
    b17 = Button(c9, text="Next->", font="HANSON 18", bg="lavender blush",fg="maroon1",activeforeground="blue2",activebackground="lavender blush" ,command=faq2, relief=SUNKEN,borderwidth=0,cursor="hand2")
    c9.create_window(888, 654, window=b17, anchor="e")

def faq2():
    f11 = Frame(root, width=904, height=684, bg="light cyan")
    f11.place(x=608, y=84)
    c10 = Canvas(f11, bg="lavender blush", width=904, height=684, highlightbackground="black")
    c10.pack()
    c10.create_text(454, 224,
                   text="(6) What all documents need to be carried to the train?\n--> You need to have any identity proof (with a photograph of the passenger),\n     train ticket (both soft copy and hard copy would be fine).\n     The following will be accepted as Identity proof:\n    - Voter Photo identity card issued by Election Commission of India.\n    - Passport.\n    - PAN Card issued by the Income Tax Department\n    - Driving License issued by RTO\n    - Photo identity card having a serial number issued by Central/State Government\n    - Nationalized Bank Passbook with a photograph\n    - Credit cards issued by banks with a laminated photograph\n    - Unique Identification Card “Aadhaar”.\n    - Photo identity cards having a serial number issued by the Public Sector\n    - Anything apart from this shall not be accepted.\n    For further queries, please contact management12@trainreservation.com",
                   font=("Arial Black", 15), fill="blue")
    b18 = Button(c10, text="<-Previous", font="HANSON 18", bg="lavender blush", fg="maroon1", activeforeground="blue2",
                 activebackground="lavender blush", command=faq, relief=SUNKEN, borderwidth=0, cursor="hand2")
    c10.create_window(8, 654, window=b18, anchor="w")

var1 = StringVar()
var1.set("Radio")

var2 = StringVar()
var2.set("Radio")

def hotel():
    f21 = Frame(root, width=584, height=384)
    f21.place(x=784, y=244)
    c17 = Canvas(f21, bg="lavender blush", width=584, height=384)
    c17.pack()
    c17.pack(fill="both", expand=True)
    c17.create_image(0, 0, image=accomodation, anchor="nw")
    b34 = Button(c17, width=4, text="BACK", font="HANSON 8", bg="lavender blush", fg="gray4",border=1,command=sign,cursor="hand2")
    c17.create_window(4, 364, window=b34, anchor="nw")

def taxi():
    f22 = Frame(root, width=584, height=384)
    f22.place(x=784, y=244)
    c18 = Canvas(f22, bg="lavender blush", width=584, height=384)
    c18.pack()
    c18.pack(fill="both", expand=True)
    c18.create_image(0, 0, image=vehicle, anchor="nw")
    b35 = Button(c18, width=4, text="BACK", font="HANSON 8", bg="lavender blush", fg="gray4",border=1,command=sign,cursor="hand2")
    c18.create_window(4, 364, window=b35, anchor="nw")

def pay():
    f20 = Frame(root, width=584, height=384)
    f20.place(x=784, y=244)
    c16 = Canvas(f20, bg="lavender blush", width=584, height=384)
    c16.pack()
    c16.pack(fill="both", expand=True)
    c16.create_image(0, 0, image=qr, anchor="nw")
    c16.create_text(484, 34, text="   Scan\nQR Code", font="HANSON 18", fill="deep pink")
    c16.create_text(484, 184, text="R\nA\nI\nL\nW\nA\nY", font="HANSON 18", fill="pink", justify=CENTER)
    b31 = Button(c16, width=8, text="BACK", font="HANSON 12", bg="pink", fg="gray12",border=1,command=sign,cursor="hand2")
    c16.create_window(424, 312, window=b31, anchor="nw")

def book1():
    f12 = Frame(root, width=584, height=384)
    f12.place(x=784, y=244)
    c11 = Canvas(f12, bg="lavender blush", width=584, height=384)
    c11.pack()
    c11.create_text(288, 54, text="          SELECT\nSource & Destination", font="HANSON 21", fill="deep pink")

    f13 = Frame(c11, width=100, height=184, bg="lavender blush")
    f13.place(x=84,y=88)

    list1 = ["New Delhi","Jaipur","Chennai","Mysuru","Kolkata","Hyderabad","Pune",]
    for i in range(len(list1)):
        r1 = Radiobutton(f13, text=list1[i],font=("Arial Black", 14), fg="Black", bg="lavender blush", variable=var1, value=list1[i], cursor="hand2")
        r1.pack(side=TOP,anchor="w")

    f14 = Frame(c11, width=100, height=184, bg="lavender blush")
    f14.place(x=298, y=88)

    list2 = ["Bangalore","Mumbai","Chennai","Delhi","Ahmedabad","Bhopal","Lucknow"]
    for i in range(len(list2)):
        r2 = Radiobutton(f14, text=list2[i], font=("Arial Black", 14), fg="Black", bg="lavender blush", variable=var2,
                         value=list2[i], cursor="hand2")
        r2.pack(side=TOP, anchor="w")

    b20 = Button(c11, text="BACK", font="HANSON 12", bg="misty rose", fg="gray21", command=sign, cursor="hand2")
    c11.create_window(4, 368, window=b20, anchor="w")
    b21 = Button(c11, text="NEXT", font="HANSON 15", bg="azure", fg="gray21", command=book2, cursor="hand2")
    c11.create_window(448, 348, window=b21, anchor="w")

passenger1=StringVar()
passenger2=StringVar()
passenger3=StringVar()
passenger4=StringVar()
passenger5=StringVar()

age1=StringVar()
age2=StringVar()
age3=StringVar()
age4=StringVar()
age5=StringVar()

date1=StringVar()

coach = ["1A","2A","3A","SL","GN"]

coach1=StringVar()
coach1.set(0)

kids1=IntVar()
kids2=IntVar()

ck1=IntVar()

def generate_random_code(length):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_pnr():
    return generate_random_code(6)

def generate_ticket_number():
    return ''.join(random.choice(string.digits) for _ in range(10))

pnr = generate_pnr()
ticket_number = generate_ticket_number()

def book2():
    def book_ticket():
        with open('C:/Users/MANMOHAN C A/Desktop/ticket.txt', "a") as file:
            file.write(f"PNR: {pnr}, Ticket_Number: {ticket_number}, Date: {date1.get()}, Coach: {coach1.get()}, Train_Number: {train_num}, Train: {train_name}\n")

    def book1_ticket():
        a = tmsg.askquestion("BOOK", "ARE YOU SURE")
        if a == "yes":
            book_ticket()
            ticket_print()
        else:
            b = "TRY AGAIN!"
            tmsg.showinfo("BOOK", b)


    f15 = Frame(root, width=584, height=384)
    f15.place(x=784, y=244)
    c12 = Canvas(f15, bg="lavender blush", width=584, height=384)
    c12.pack()

    if ((var1.get()=="New Delhi") and (var2.get()=="Mumbai")):
        c12.create_text(288, 21, text="Train Name: Hindustan Express", font="HANSON 18", fill="deep pink")
        c12.create_text(218, 48, text="Train Number: 3587482", font="HANSON 18", fill="deep pink")

        train_num= 3587482
        train_name= "Hindustan Express"

        def on_enter(e):
            p1.delete(0, 'end')

        def on_leave(e):
            name = p1.get()
            if name == '':
                p1.insert(0, 'Passenger1')

        p1 = Entry(c12, width=32, textvariable=passenger1, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p1.insert(0, "Passenger1")
        p1.bind("<FocusIn>", on_enter)
        p1.bind("<FocusOut>", on_leave)
        c12.create_window(21, 74, window=p1, anchor="nw")

        def on_enter(e):
            p2.delete(0, 'end')

        def on_leave(e):
            name = p2.get()
            if name == '':
                p2.insert(0, 'Passenger2')

        p2 = Entry(c12, width=32, textvariable=passenger2, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p2.insert(0, "Passenger2")
        p2.bind("<FocusIn>", on_enter)
        p2.bind("<FocusOut>", on_leave)
        c12.create_window(21, 104, window=p2, anchor="nw")

        def on_enter(e):
            p3.delete(0, 'end')

        def on_leave(e):
            name = p3.get()
            if name == '':
                p3.insert(0, 'Passenger3')

        p3 = Entry(c12, width=32, textvariable=passenger3, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p3.insert(0, "Passenger3")
        p3.bind("<FocusIn>", on_enter)
        p3.bind("<FocusOut>", on_leave)
        c12.create_window(21, 134, window=p3, anchor="nw")

        def on_enter(e):
            p4.delete(0, 'end')

        def on_leave(e):
            name = p4.get()
            if name == '':
                p4.insert(0, 'Passenger4')

        p4 = Entry(c12, width=32, textvariable=passenger4, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p4.insert(0, "Passenger4")
        p4.bind("<FocusIn>", on_enter)
        p4.bind("<FocusOut>", on_leave)
        c12.create_window(21, 164, window=p4, anchor="nw")

        def on_enter(e):
            p5.delete(0, 'end')

        def on_leave(e):
            name = p5.get()
            if name == '':
                p5.insert(0, 'Passenger5')

        p5 = Entry(c12, width=32, textvariable=passenger5, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p5.insert(0, "Passenger5")
        p5.bind("<FocusIn>", on_enter)
        p5.bind("<FocusOut>", on_leave)
        c12.create_window(21, 194, window=p5, anchor="nw")

        def on_enter(e):
            g1.delete(0, 'end')

        def on_leave(e):
            name = g1.get()
            if name == '':
                g1.insert(0, 'Gender')

        g1 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g1.insert(0, "Gender")
        g1.bind("<FocusIn>", on_enter)
        g1.bind("<FocusOut>", on_leave)
        c12.create_window(384, 74, window=g1, anchor="nw")

        def on_enter(e):
            g2.delete(0, 'end')

        def on_leave(e):
            name = g2.get()
            if name == '':
                g2.insert(0, 'Gender')

        g2 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g2.insert(0, "Gender")
        g2.bind("<FocusIn>", on_enter)
        g2.bind("<FocusOut>", on_leave)
        c12.create_window(384, 104, window=g2, anchor="nw")

        def on_enter(e):
            g3.delete(0, 'end')

        def on_leave(e):
            name = g3.get()
            if name == '':
                g3.insert(0, 'Gender')

        g3 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g3.insert(0, "Gender")
        g3.bind("<FocusIn>", on_enter)
        g3.bind("<FocusOut>", on_leave)
        c12.create_window(384, 134, window=g3, anchor="nw")

        def on_enter(e):
            g4.delete(0, 'end')

        def on_leave(e):
            name = g4.get()
            if name == '':
                g4.insert(0, 'Gender')

        g4 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g4.insert(0, "Gender")
        g4.bind("<FocusIn>", on_enter)
        g4.bind("<FocusOut>", on_leave)
        c12.create_window(384, 164, window=g4, anchor="nw")

        def on_enter(e):
            g5.delete(0, 'end')

        def on_leave(e):
            name = g5.get()
            if name == '':
                g5.insert(0, 'Gender')

        g5 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g5.insert(0, "Gender")
        g5.bind("<FocusIn>", on_enter)
        g5.bind("<FocusOut>", on_leave)
        c12.create_window(384, 194, window=g5, anchor="nw")

        def on_enter(e):
            a1.delete(0, 'end')

        def on_leave(e):
            name = a1.get()
            if name == '':
                a1.insert(0, 'Age')

        a1 = Entry(c12, width=8,  textvariable=age1,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a1.insert(0, "Age")
        a1.bind("<FocusIn>", on_enter)
        a1.bind("<FocusOut>", on_leave)
        c12.create_window(480, 74, window=a1, anchor="nw")

        def on_enter(e):
            a2.delete(0, 'end')

        def on_leave(e):
            name = a2.get()
            if name == '':
                a2.insert(0, 'Age')

        a2 = Entry(c12, width=8,  textvariable=age2,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a2.insert(0, "Age")
        a2.bind("<FocusIn>", on_enter)
        a2.bind("<FocusOut>", on_leave)
        c12.create_window(480, 104, window=a2, anchor="nw")

        def on_enter(e):
            a2.delete(0, 'end')

        def on_leave(e):
            name = a3.get()
            if name == '':
                a3.insert(0, 'Age')

        a3 = Entry(c12, width=8,  textvariable=age3,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a3.insert(0, "Age")
        a3.bind("<FocusIn>", on_enter)
        a3.bind("<FocusOut>", on_leave)
        c12.create_window(480, 134, window=a3, anchor="nw")

        def on_enter(e):
            a4.delete(0, 'end')

        def on_leave(e):
            name = a4.get()
            if name == '':
                a4.insert(0, 'Age')

        a4 = Entry(c12, width=8,  textvariable=age4,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a4.insert(0, "Age")
        a4.bind("<FocusIn>", on_enter)
        a4.bind("<FocusOut>", on_leave)
        c12.create_window(480, 164, window=a4, anchor="nw")

        def on_enter(e):
            a5.delete(0, 'end')

        def on_leave(e):
            name = a5.get()
            if name == '':
                a5.insert(0, 'Age')

        a5 = Entry(c12, width=8,  textvariable=age5,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a5.insert(0, "Age")
        a5.bind("<FocusIn>", on_enter)
        a5.bind("<FocusOut>", on_leave)
        c12.create_window(480, 194, window=a5, anchor="nw")

        def on_enter(e):
            d1.delete(0, 'end')

        def on_leave(e):
            name = d1.get()
            if name == '':
                d1.insert(0, 'Date (yyyy-mm-dd)')

        d1 = Entry(c12, width=18, textvariable=date1, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        d1.insert(0, "Date (yyyy-mm-dd)")
        d1.bind("<FocusIn>", on_enter)
        d1.bind("<FocusOut>", on_leave)
        c12.create_window(370, 228, window=d1, anchor="nw")

        f16 = Frame(c12, width=248, height=21, bg="lavender blush")
        f16.place(x=48, y=225)


        for i in range(len(coach)):
            rb1 = Radiobutton(f16, text=coach[i], font=("Arial Black", 12), fg="Black", bg="lavender blush",
                             variable=coach1, value=coach[i], cursor="hand2", padx=1)
            rb1.pack(side=LEFT, anchor="w")

            def on_enter(e):
                k1.delete(0, 'end')

            def on_leave(e):
                name = k1.get()
                if name == '':
                    k1.insert(0, "No of KIDS (<10yrs)")

            k1 = Entry(c12, width=17,textvariable=kids1, bg="snow", fg="gray21", font=4, border=1, relief=SUNKEN,
                       justify=CENTER)
            k1.insert(0, "No of KIDS (<10yrs)")
            k1.bind("<FocusIn>", on_enter)
            k1.bind("<FocusOut>", on_leave)
            c12.create_window(94, 261, window=k1, anchor="nw")

            def on_enter(e):
                k2.delete(0, 'end')

            def on_leave(e):
                name = k2.get()
                if name == '':
                    k2.insert(0, 'Total Passengers')

            k2 = Entry(c12, width=30, textvariable=kids2, bg="snow", fg="gray21", font=8, border=1, relief=SUNKEN,
                       justify=CENTER)
            k2.insert(0, "Total Passengers")
            k2.bind("<FocusIn>", on_enter)
            k2.bind("<FocusOut>", on_leave)
            c12.create_window(24, 298, window=k2, anchor="nw")
            b22 = Button(c12, text="BACK", font="HANSON 10", bg="misty rose", fg="gray21", command=book1, cursor="hand2")
            c12.create_window(444, 371, window=b22, anchor="w")

            cb1 = Checkbutton(c12, text="ACCEPT TERMS AND CONDITIONS", variable=ck1, font=("Arial Black", 10), command=war, bg="mint cream")
            c12.create_window(48, 344, window=cb1, anchor="nw")

            b23 = Button(c12, text="BOOK\nTICKET", font="HANSON 14", bg="hot pink", fg="white", command=book1_ticket,
                         cursor="hand2")
            c12.create_window(418, 298, window=b23, anchor="w")

    elif ((var1.get()=="Chennai") and (var2.get()=="Bangalore")):
        c12.create_text(288, 21, text="Train Name: Shatabdi Express", font="HANSON 18", fill="deep pink")
        c12.create_text(218, 48, text="Train Number: 3587482", font="HANSON 18", fill="deep pink")

        train_num = 3587482
        train_name = "Shatabdi Express"

        def on_enter(e):
            p1.delete(0, 'end')

        def on_leave(e):
            name = p1.get()
            if name == '':
                p1.insert(0, 'Passenger1')

        p1 = Entry(c12, width=32, textvariable=passenger1, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p1.insert(0, "Passenger1")
        p1.bind("<FocusIn>", on_enter)
        p1.bind("<FocusOut>", on_leave)
        c12.create_window(21, 74, window=p1, anchor="nw")

        def on_enter(e):
            p2.delete(0, 'end')

        def on_leave(e):
            name = p2.get()
            if name == '':
                p2.insert(0, 'Passenger2')

        p2 = Entry(c12, width=32, textvariable=passenger2, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p2.insert(0, "Passenger2")
        p2.bind("<FocusIn>", on_enter)
        p2.bind("<FocusOut>", on_leave)
        c12.create_window(21, 104, window=p2, anchor="nw")

        def on_enter(e):
            p3.delete(0, 'end')

        def on_leave(e):
            name = p3.get()
            if name == '':
                p3.insert(0, 'Passenger3')

        p3 = Entry(c12, width=32, textvariable=passenger3, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p3.insert(0, "Passenger3")
        p3.bind("<FocusIn>", on_enter)
        p3.bind("<FocusOut>", on_leave)
        c12.create_window(21, 134, window=p3, anchor="nw")

        def on_enter(e):
            p4.delete(0, 'end')

        def on_leave(e):
            name = p4.get()
            if name == '':
                p4.insert(0, 'Passenger4')

        p4 = Entry(c12, width=32, textvariable=passenger4, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p4.insert(0, "Passenger4")
        p4.bind("<FocusIn>", on_enter)
        p4.bind("<FocusOut>", on_leave)
        c12.create_window(21, 164, window=p4, anchor="nw")

        def on_enter(e):
            p5.delete(0, 'end')

        def on_leave(e):
            name = p5.get()
            if name == '':
                p5.insert(0, 'Passenger5')

        p5 = Entry(c12, width=32, textvariable=passenger5, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p5.insert(0, "Passenger5")
        p5.bind("<FocusIn>", on_enter)
        p5.bind("<FocusOut>", on_leave)
        c12.create_window(21, 194, window=p5, anchor="nw")

        def on_enter(e):
            g1.delete(0, 'end')

        def on_leave(e):
            name = g1.get()
            if name == '':
                g1.insert(0, 'Gender')

        g1 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g1.insert(0, "Gender")
        g1.bind("<FocusIn>", on_enter)
        g1.bind("<FocusOut>", on_leave)
        c12.create_window(384, 74, window=g1, anchor="nw")

        def on_enter(e):
            g2.delete(0, 'end')

        def on_leave(e):
            name = g2.get()
            if name == '':
                g2.insert(0, 'Gender')

        g2 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g2.insert(0, "Gender")
        g2.bind("<FocusIn>", on_enter)
        g2.bind("<FocusOut>", on_leave)
        c12.create_window(384, 104, window=g2, anchor="nw")

        def on_enter(e):
            g3.delete(0, 'end')

        def on_leave(e):
            name = g3.get()
            if name == '':
                g3.insert(0, 'Gender')

        g3 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g3.insert(0, "Gender")
        g3.bind("<FocusIn>", on_enter)
        g3.bind("<FocusOut>", on_leave)
        c12.create_window(384, 134, window=g3, anchor="nw")

        def on_enter(e):
            g4.delete(0, 'end')

        def on_leave(e):
            name = g4.get()
            if name == '':
                g4.insert(0, 'Gender')

        g4 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g4.insert(0, "Gender")
        g4.bind("<FocusIn>", on_enter)
        g4.bind("<FocusOut>", on_leave)
        c12.create_window(384, 164, window=g4, anchor="nw")

        def on_enter(e):
            g5.delete(0, 'end')

        def on_leave(e):
            name = g5.get()
            if name == '':
                g5.insert(0, 'Gender')

        g5 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g5.insert(0, "Gender")
        g5.bind("<FocusIn>", on_enter)
        g5.bind("<FocusOut>", on_leave)
        c12.create_window(384, 194, window=g5, anchor="nw")

        def on_enter(e):
            a1.delete(0, 'end')

        def on_leave(e):
            name = a1.get()
            if name == '':
                a1.insert(0, 'Age')

        a1 = Entry(c12, width=8,  textvariable=age1,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a1.insert(0, "Age")
        a1.bind("<FocusIn>", on_enter)
        a1.bind("<FocusOut>", on_leave)
        c12.create_window(480, 74, window=a1, anchor="nw")

        def on_enter(e):
            a2.delete(0, 'end')

        def on_leave(e):
            name = a2.get()
            if name == '':
                a2.insert(0, 'Age')

        a2 = Entry(c12, width=8,  textvariable=age2,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a2.insert(0, "Age")
        a2.bind("<FocusIn>", on_enter)
        a2.bind("<FocusOut>", on_leave)
        c12.create_window(480, 104, window=a2, anchor="nw")

        def on_enter(e):
            a2.delete(0, 'end')

        def on_leave(e):
            name = a3.get()
            if name == '':
                a3.insert(0, 'Age')

        a3 = Entry(c12, width=8,  textvariable=age3,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a3.insert(0, "Age")
        a3.bind("<FocusIn>", on_enter)
        a3.bind("<FocusOut>", on_leave)
        c12.create_window(480, 134, window=a3, anchor="nw")

        def on_enter(e):
            a4.delete(0, 'end')

        def on_leave(e):
            name = a4.get()
            if name == '':
                a4.insert(0, 'Age')

        a4 = Entry(c12, width=8,  textvariable=age4,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a4.insert(0, "Age")
        a4.bind("<FocusIn>", on_enter)
        a4.bind("<FocusOut>", on_leave)
        c12.create_window(480, 164, window=a4, anchor="nw")

        def on_enter(e):
            a5.delete(0, 'end')

        def on_leave(e):
            name = a5.get()
            if name == '':
                a5.insert(0, 'Age')

        a5 = Entry(c12, width=8,  textvariable=age5,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a5.insert(0, "Age")
        a5.bind("<FocusIn>", on_enter)
        a5.bind("<FocusOut>", on_leave)
        c12.create_window(480, 194, window=a5, anchor="nw")

        def on_enter(e):
            d1.delete(0, 'end')

        def on_leave(e):
            name = d1.get()
            if name == '':
                d1.insert(0, 'Date (yyyy-mm-dd)')

        d1 = Entry(c12, width=18, textvariable=date1, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        d1.insert(0, "Date (yyyy-mm-dd)")
        d1.bind("<FocusIn>", on_enter)
        d1.bind("<FocusOut>", on_leave)
        c12.create_window(370, 228, window=d1, anchor="nw")

        f16 = Frame(c12, width=248, height=21, bg="lavender blush")
        f16.place(x=48, y=225)


        for i in range(len(coach)):
            rb1 = Radiobutton(f16, text=coach[i], font=("Arial Black", 12), fg="Black", bg="lavender blush",
                             variable=coach1, value=coach[i], cursor="hand2", padx=1)
            rb1.pack(side=LEFT, anchor="w")

            def on_enter(e):
                k1.delete(0, 'end')

            def on_leave(e):
                name = k1.get()
                if name == '':
                    k1.insert(0, "No of KIDS (<10yrs)")

            k1 = Entry(c12, width=17,textvariable=kids1, bg="snow", fg="gray21", font=4, border=1, relief=SUNKEN,
                       justify=CENTER)
            k1.insert(0, "No of KIDS (<10yrs)")
            k1.bind("<FocusIn>", on_enter)
            k1.bind("<FocusOut>", on_leave)
            c12.create_window(94, 261, window=k1, anchor="nw")

            def on_enter(e):
                k2.delete(0, 'end')

            def on_leave(e):
                name = k2.get()
                if name == '':
                    k2.insert(0, 'Total Passengers')

            k2 = Entry(c12, width=30, textvariable=kids2, bg="snow", fg="gray21", font=8, border=1, relief=SUNKEN,
                       justify=CENTER)
            k2.insert(0, "Total Passengers")
            k2.bind("<FocusIn>", on_enter)
            k2.bind("<FocusOut>", on_leave)
            c12.create_window(24, 298, window=k2, anchor="nw")
            b22 = Button(c12, text="BACK", font="HANSON 10", bg="misty rose", fg="gray21", command=book1, cursor="hand2")
            c12.create_window(444, 371, window=b22, anchor="w")

            cb1 = Checkbutton(c12, text="ACCEPT TERMS AND CONDITIONS", variable=ck1, font=("Arial Black", 10), command=war, bg="mint cream")
            c12.create_window(48, 344, window=cb1, anchor="nw")

            b23 = Button(c12, text="BOOK\nTICKET", font="HANSON 14", bg="hot pink", fg="white", command=book1_ticket,
                         cursor="hand2")
            c12.create_window(418, 298, window=b23, anchor="w")

    elif ((var1.get()=="Kolkata") and (var2.get()=="Delhi")):
        c12.create_text(288, 21, text="Train Name: Duronto Express", font="HANSON 18", fill="deep pink")
        c12.create_text(218, 48, text="Train Number: 3587482", font="HANSON 18", fill="deep pink")

        train_num= 3587482
        train_name= "Duronto Express"

        def on_enter(e):
            p1.delete(0, 'end')

        def on_leave(e):
            name = p1.get()
            if name == '':
                p1.insert(0, 'Passenger1')

        p1 = Entry(c12, width=32, textvariable=passenger1, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p1.insert(0, "Passenger1")
        p1.bind("<FocusIn>", on_enter)
        p1.bind("<FocusOut>", on_leave)
        c12.create_window(21, 74, window=p1, anchor="nw")

        def on_enter(e):
            p2.delete(0, 'end')

        def on_leave(e):
            name = p2.get()
            if name == '':
                p2.insert(0, 'Passenger2')

        p2 = Entry(c12, width=32, textvariable=passenger2, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p2.insert(0, "Passenger2")
        p2.bind("<FocusIn>", on_enter)
        p2.bind("<FocusOut>", on_leave)
        c12.create_window(21, 104, window=p2, anchor="nw")

        def on_enter(e):
            p3.delete(0, 'end')

        def on_leave(e):
            name = p3.get()
            if name == '':
                p3.insert(0, 'Passenger3')

        p3 = Entry(c12, width=32, textvariable=passenger3, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p3.insert(0, "Passenger3")
        p3.bind("<FocusIn>", on_enter)
        p3.bind("<FocusOut>", on_leave)
        c12.create_window(21, 134, window=p3, anchor="nw")

        def on_enter(e):
            p4.delete(0, 'end')

        def on_leave(e):
            name = p4.get()
            if name == '':
                p4.insert(0, 'Passenger4')

        p4 = Entry(c12, width=32, textvariable=passenger4, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p4.insert(0, "Passenger4")
        p4.bind("<FocusIn>", on_enter)
        p4.bind("<FocusOut>", on_leave)
        c12.create_window(21, 164, window=p4, anchor="nw")

        def on_enter(e):
            p5.delete(0, 'end')

        def on_leave(e):
            name = p5.get()
            if name == '':
                p5.insert(0, 'Passenger5')

        p5 = Entry(c12, width=32, textvariable=passenger5, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p5.insert(0, "Passenger5")
        p5.bind("<FocusIn>", on_enter)
        p5.bind("<FocusOut>", on_leave)
        c12.create_window(21, 194, window=p5, anchor="nw")

        def on_enter(e):
            g1.delete(0, 'end')

        def on_leave(e):
            name = g1.get()
            if name == '':
                g1.insert(0, 'Gender')

        g1 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g1.insert(0, "Gender")
        g1.bind("<FocusIn>", on_enter)
        g1.bind("<FocusOut>", on_leave)
        c12.create_window(384, 74, window=g1, anchor="nw")

        def on_enter(e):
            g2.delete(0, 'end')

        def on_leave(e):
            name = g2.get()
            if name == '':
                g2.insert(0, 'Gender')

        g2 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g2.insert(0, "Gender")
        g2.bind("<FocusIn>", on_enter)
        g2.bind("<FocusOut>", on_leave)
        c12.create_window(384, 104, window=g2, anchor="nw")

        def on_enter(e):
            g3.delete(0, 'end')

        def on_leave(e):
            name = g3.get()
            if name == '':
                g3.insert(0, 'Gender')

        g3 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g3.insert(0, "Gender")
        g3.bind("<FocusIn>", on_enter)
        g3.bind("<FocusOut>", on_leave)
        c12.create_window(384, 134, window=g3, anchor="nw")

        def on_enter(e):
            g4.delete(0, 'end')

        def on_leave(e):
            name = g4.get()
            if name == '':
                g4.insert(0, 'Gender')

        g4 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g4.insert(0, "Gender")
        g4.bind("<FocusIn>", on_enter)
        g4.bind("<FocusOut>", on_leave)
        c12.create_window(384, 164, window=g4, anchor="nw")

        def on_enter(e):
            g5.delete(0, 'end')

        def on_leave(e):
            name = g5.get()
            if name == '':
                g5.insert(0, 'Gender')

        g5 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g5.insert(0, "Gender")
        g5.bind("<FocusIn>", on_enter)
        g5.bind("<FocusOut>", on_leave)
        c12.create_window(384, 194, window=g5, anchor="nw")

        def on_enter(e):
            a1.delete(0, 'end')

        def on_leave(e):
            name = a1.get()
            if name == '':
                a1.insert(0, 'Age')

        a1 = Entry(c12, width=8,  textvariable=age1,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a1.insert(0, "Age")
        a1.bind("<FocusIn>", on_enter)
        a1.bind("<FocusOut>", on_leave)
        c12.create_window(480, 74, window=a1, anchor="nw")

        def on_enter(e):
            a2.delete(0, 'end')

        def on_leave(e):
            name = a2.get()
            if name == '':
                a2.insert(0, 'Age')

        a2 = Entry(c12, width=8,  textvariable=age2,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a2.insert(0, "Age")
        a2.bind("<FocusIn>", on_enter)
        a2.bind("<FocusOut>", on_leave)
        c12.create_window(480, 104, window=a2, anchor="nw")

        def on_enter(e):
            a2.delete(0, 'end')

        def on_leave(e):
            name = a3.get()
            if name == '':
                a3.insert(0, 'Age')

        a3 = Entry(c12, width=8,  textvariable=age3,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a3.insert(0, "Age")
        a3.bind("<FocusIn>", on_enter)
        a3.bind("<FocusOut>", on_leave)
        c12.create_window(480, 134, window=a3, anchor="nw")

        def on_enter(e):
            a4.delete(0, 'end')

        def on_leave(e):
            name = a4.get()
            if name == '':
                a4.insert(0, 'Age')

        a4 = Entry(c12, width=8,  textvariable=age4,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a4.insert(0, "Age")
        a4.bind("<FocusIn>", on_enter)
        a4.bind("<FocusOut>", on_leave)
        c12.create_window(480, 164, window=a4, anchor="nw")

        def on_enter(e):
            a5.delete(0, 'end')

        def on_leave(e):
            name = a5.get()
            if name == '':
                a5.insert(0, 'Age')

        a5 = Entry(c12, width=8,  textvariable=age5,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a5.insert(0, "Age")
        a5.bind("<FocusIn>", on_enter)
        a5.bind("<FocusOut>", on_leave)
        c12.create_window(480, 194, window=a5, anchor="nw")

        def on_enter(e):
            d1.delete(0, 'end')

        def on_leave(e):
            name = d1.get()
            if name == '':
                d1.insert(0, 'Date (yyyy-mm-dd)')

        d1 = Entry(c12, width=18, textvariable=date1, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        d1.insert(0, "Date (yyyy-mm-dd)")
        d1.bind("<FocusIn>", on_enter)
        d1.bind("<FocusOut>", on_leave)
        c12.create_window(370, 228, window=d1, anchor="nw")

        f16 = Frame(c12, width=248, height=21, bg="lavender blush")
        f16.place(x=48, y=225)


        for i in range(len(coach)):
            rb1 = Radiobutton(f16, text=coach[i], font=("Arial Black", 12), fg="Black", bg="lavender blush",
                             variable=coach1, value=coach[i], cursor="hand2", padx=1)
            rb1.pack(side=LEFT, anchor="w")

            def on_enter(e):
                k1.delete(0, 'end')

            def on_leave(e):
                name = k1.get()
                if name == '':
                    k1.insert(0, "No of KIDS (<10yrs)")

            k1 = Entry(c12, width=17,textvariable=kids1, bg="snow", fg="gray21", font=4, border=1, relief=SUNKEN,
                       justify=CENTER)
            k1.insert(0, "No of KIDS (<10yrs)")
            k1.bind("<FocusIn>", on_enter)
            k1.bind("<FocusOut>", on_leave)
            c12.create_window(94, 261, window=k1, anchor="nw")

            def on_enter(e):
                k2.delete(0, 'end')

            def on_leave(e):
                name = k2.get()
                if name == '':
                    k2.insert(0, 'Total Passengers')

            k2 = Entry(c12, width=30, textvariable=kids2, bg="snow", fg="gray21", font=8, border=1, relief=SUNKEN,
                       justify=CENTER)
            k2.insert(0, "Total Passengers")
            k2.bind("<FocusIn>", on_enter)
            k2.bind("<FocusOut>", on_leave)
            c12.create_window(24, 298, window=k2, anchor="nw")
            b22 = Button(c12, text="BACK", font="HANSON 10", bg="misty rose", fg="gray21", command=book1, cursor="hand2")
            c12.create_window(444, 371, window=b22, anchor="w")

            cb1 = Checkbutton(c12, text="ACCEPT TERMS AND CONDITIONS", variable=ck1, font=("Arial Black", 10), command=war, bg="mint cream")
            c12.create_window(48, 344, window=cb1, anchor="nw")

            b23 = Button(c12, text="BOOK\nTICKET", font="HANSON 14", bg="hot pink", fg="white", command=book1_ticket,
                         cursor="hand2")
            c12.create_window(418, 298, window=b23, anchor="w")

    elif ((var1.get()=="Pune") and (var2.get()=="Ahmedabad")):
        c12.create_text(288, 21, text="Train Name: Garib Rath             ", font="HANSON 18", fill="deep pink")
        c12.create_text(218, 48, text="Train Number: 3587482", font="HANSON 18", fill="deep pink")

        train_num = 3587482
        train_name = "Garib Rath"

        def on_enter(e):
            p1.delete(0, 'end')

        def on_leave(e):
            name = p1.get()
            if name == '':
                p1.insert(0, 'Passenger1')

        p1 = Entry(c12, width=32, textvariable=passenger1, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p1.insert(0, "Passenger1")
        p1.bind("<FocusIn>", on_enter)
        p1.bind("<FocusOut>", on_leave)
        c12.create_window(21, 74, window=p1, anchor="nw")

        def on_enter(e):
            p2.delete(0, 'end')

        def on_leave(e):
            name = p2.get()
            if name == '':
                p2.insert(0, 'Passenger2')

        p2 = Entry(c12, width=32, textvariable=passenger2, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p2.insert(0, "Passenger2")
        p2.bind("<FocusIn>", on_enter)
        p2.bind("<FocusOut>", on_leave)
        c12.create_window(21, 104, window=p2, anchor="nw")

        def on_enter(e):
            p3.delete(0, 'end')

        def on_leave(e):
            name = p3.get()
            if name == '':
                p3.insert(0, 'Passenger3')

        p3 = Entry(c12, width=32, textvariable=passenger3, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p3.insert(0, "Passenger3")
        p3.bind("<FocusIn>", on_enter)
        p3.bind("<FocusOut>", on_leave)
        c12.create_window(21, 134, window=p3, anchor="nw")

        def on_enter(e):
            p4.delete(0, 'end')

        def on_leave(e):
            name = p4.get()
            if name == '':
                p4.insert(0, 'Passenger4')

        p4 = Entry(c12, width=32, textvariable=passenger4, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p4.insert(0, "Passenger4")
        p4.bind("<FocusIn>", on_enter)
        p4.bind("<FocusOut>", on_leave)
        c12.create_window(21, 164, window=p4, anchor="nw")

        def on_enter(e):
            p5.delete(0, 'end')

        def on_leave(e):
            name = p5.get()
            if name == '':
                p5.insert(0, 'Passenger5')

        p5 = Entry(c12, width=32, textvariable=passenger5, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p5.insert(0, "Passenger5")
        p5.bind("<FocusIn>", on_enter)
        p5.bind("<FocusOut>", on_leave)
        c12.create_window(21, 194, window=p5, anchor="nw")

        def on_enter(e):
            g1.delete(0, 'end')

        def on_leave(e):
            name = g1.get()
            if name == '':
                g1.insert(0, 'Gender')

        g1 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g1.insert(0, "Gender")
        g1.bind("<FocusIn>", on_enter)
        g1.bind("<FocusOut>", on_leave)
        c12.create_window(384, 74, window=g1, anchor="nw")

        def on_enter(e):
            g2.delete(0, 'end')

        def on_leave(e):
            name = g2.get()
            if name == '':
                g2.insert(0, 'Gender')

        g2 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g2.insert(0, "Gender")
        g2.bind("<FocusIn>", on_enter)
        g2.bind("<FocusOut>", on_leave)
        c12.create_window(384, 104, window=g2, anchor="nw")

        def on_enter(e):
            g3.delete(0, 'end')

        def on_leave(e):
            name = g3.get()
            if name == '':
                g3.insert(0, 'Gender')

        g3 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g3.insert(0, "Gender")
        g3.bind("<FocusIn>", on_enter)
        g3.bind("<FocusOut>", on_leave)
        c12.create_window(384, 134, window=g3, anchor="nw")

        def on_enter(e):
            g4.delete(0, 'end')

        def on_leave(e):
            name = g4.get()
            if name == '':
                g4.insert(0, 'Gender')

        g4 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g4.insert(0, "Gender")
        g4.bind("<FocusIn>", on_enter)
        g4.bind("<FocusOut>", on_leave)
        c12.create_window(384, 164, window=g4, anchor="nw")

        def on_enter(e):
            g5.delete(0, 'end')

        def on_leave(e):
            name = g5.get()
            if name == '':
                g5.insert(0, 'Gender')

        g5 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g5.insert(0, "Gender")
        g5.bind("<FocusIn>", on_enter)
        g5.bind("<FocusOut>", on_leave)
        c12.create_window(384, 194, window=g5, anchor="nw")

        def on_enter(e):
            a1.delete(0, 'end')

        def on_leave(e):
            name = a1.get()
            if name == '':
                a1.insert(0, 'Age')

        a1 = Entry(c12, width=8,  textvariable=age1,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a1.insert(0, "Age")
        a1.bind("<FocusIn>", on_enter)
        a1.bind("<FocusOut>", on_leave)
        c12.create_window(480, 74, window=a1, anchor="nw")

        def on_enter(e):
            a2.delete(0, 'end')

        def on_leave(e):
            name = a2.get()
            if name == '':
                a2.insert(0, 'Age')

        a2 = Entry(c12, width=8,  textvariable=age2,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a2.insert(0, "Age")
        a2.bind("<FocusIn>", on_enter)
        a2.bind("<FocusOut>", on_leave)
        c12.create_window(480, 104, window=a2, anchor="nw")

        def on_enter(e):
            a2.delete(0, 'end')

        def on_leave(e):
            name = a3.get()
            if name == '':
                a3.insert(0, 'Age')

        a3 = Entry(c12, width=8,  textvariable=age3,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a3.insert(0, "Age")
        a3.bind("<FocusIn>", on_enter)
        a3.bind("<FocusOut>", on_leave)
        c12.create_window(480, 134, window=a3, anchor="nw")

        def on_enter(e):
            a4.delete(0, 'end')

        def on_leave(e):
            name = a4.get()
            if name == '':
                a4.insert(0, 'Age')

        a4 = Entry(c12, width=8,  textvariable=age4,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a4.insert(0, "Age")
        a4.bind("<FocusIn>", on_enter)
        a4.bind("<FocusOut>", on_leave)
        c12.create_window(480, 164, window=a4, anchor="nw")

        def on_enter(e):
            a5.delete(0, 'end')

        def on_leave(e):
            name = a5.get()
            if name == '':
                a5.insert(0, 'Age')

        a5 = Entry(c12, width=8,  textvariable=age5,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a5.insert(0, "Age")
        a5.bind("<FocusIn>", on_enter)
        a5.bind("<FocusOut>", on_leave)
        c12.create_window(480, 194, window=a5, anchor="nw")

        def on_enter(e):
            d1.delete(0, 'end')

        def on_leave(e):
            name = d1.get()
            if name == '':
                d1.insert(0, 'Date (yyyy-mm-dd)')

        d1 = Entry(c12, width=18, textvariable=date1, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        d1.insert(0, "Date (yyyy-mm-dd)")
        d1.bind("<FocusIn>", on_enter)
        d1.bind("<FocusOut>", on_leave)
        c12.create_window(370, 228, window=d1, anchor="nw")

        f16 = Frame(c12, width=248, height=21, bg="lavender blush")
        f16.place(x=48, y=225)


        for i in range(len(coach)):
            rb1 = Radiobutton(f16, text=coach[i], font=("Arial Black", 12), fg="Black", bg="lavender blush",
                             variable=coach1, value=coach[i], cursor="hand2", padx=1)
            rb1.pack(side=LEFT, anchor="w")

            def on_enter(e):
                k1.delete(0, 'end')

            def on_leave(e):
                name = k1.get()
                if name == '':
                    k1.insert(0, "No of KIDS (<10yrs)")

            k1 = Entry(c12, width=17,textvariable=kids1, bg="snow", fg="gray21", font=4, border=1, relief=SUNKEN,
                       justify=CENTER)
            k1.insert(0, "No of KIDS (<10yrs)")
            k1.bind("<FocusIn>", on_enter)
            k1.bind("<FocusOut>", on_leave)
            c12.create_window(94, 261, window=k1, anchor="nw")

            def on_enter(e):
                k2.delete(0, 'end')

            def on_leave(e):
                name = k2.get()
                if name == '':
                    k2.insert(0, 'Total Passengers')

            k2 = Entry(c12, width=30, textvariable=kids2, bg="snow", fg="gray21", font=8, border=1, relief=SUNKEN,
                       justify=CENTER)
            k2.insert(0, "Total Passengers")
            k2.bind("<FocusIn>", on_enter)
            k2.bind("<FocusOut>", on_leave)
            c12.create_window(24, 298, window=k2, anchor="nw")
            b22 = Button(c12, text="BACK", font="HANSON 10", bg="misty rose", fg="gray21", command=book1, cursor="hand2")
            c12.create_window(444, 371, window=b22, anchor="w")

            cb1 = Checkbutton(c12, text="ACCEPT TERMS AND CONDITIONS", variable=ck1, font=("Arial Black", 10), command=war, bg="mint cream")
            c12.create_window(48, 344, window=cb1, anchor="nw")

            b23 = Button(c12, text="BOOK\nTICKET", font="HANSON 14", bg="hot pink", fg="white", command=book1_ticket,
                         cursor="hand2")
            c12.create_window(418, 298, window=b23, anchor="w")

    elif ((var1.get()=="Hyderabad") and (var2.get()=="Bhopal")):
        c12.create_text(288, 21, text="Train Name: Humsafar Express", font="HANSON 18", fill="deep pink")
        c12.create_text(218, 48, text="Train Number: 3587482", font="HANSON 18", fill="deep pink")

        train_num = 3587482
        train_name = "Humsafar Express"

        def on_enter(e):
            p1.delete(0, 'end')

        def on_leave(e):
            name = p1.get()
            if name == '':
                p1.insert(0, 'Passenger1')

        p1 = Entry(c12, width=32, textvariable=passenger1, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p1.insert(0, "Passenger1")
        p1.bind("<FocusIn>", on_enter)
        p1.bind("<FocusOut>", on_leave)
        c12.create_window(21, 74, window=p1, anchor="nw")

        def on_enter(e):
            p2.delete(0, 'end')

        def on_leave(e):
            name = p2.get()
            if name == '':
                p2.insert(0, 'Passenger2')

        p2 = Entry(c12, width=32, textvariable=passenger2, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p2.insert(0, "Passenger2")
        p2.bind("<FocusIn>", on_enter)
        p2.bind("<FocusOut>", on_leave)
        c12.create_window(21, 104, window=p2, anchor="nw")

        def on_enter(e):
            p3.delete(0, 'end')

        def on_leave(e):
            name = p3.get()
            if name == '':
                p3.insert(0, 'Passenger3')

        p3 = Entry(c12, width=32, textvariable=passenger3, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p3.insert(0, "Passenger3")
        p3.bind("<FocusIn>", on_enter)
        p3.bind("<FocusOut>", on_leave)
        c12.create_window(21, 134, window=p3, anchor="nw")

        def on_enter(e):
            p4.delete(0, 'end')

        def on_leave(e):
            name = p4.get()
            if name == '':
                p4.insert(0, 'Passenger4')

        p4 = Entry(c12, width=32, textvariable=passenger4, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p4.insert(0, "Passenger4")
        p4.bind("<FocusIn>", on_enter)
        p4.bind("<FocusOut>", on_leave)
        c12.create_window(21, 164, window=p4, anchor="nw")

        def on_enter(e):
            p5.delete(0, 'end')

        def on_leave(e):
            name = p5.get()
            if name == '':
                p5.insert(0, 'Passenger5')

        p5 = Entry(c12, width=32, textvariable=passenger5, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p5.insert(0, "Passenger5")
        p5.bind("<FocusIn>", on_enter)
        p5.bind("<FocusOut>", on_leave)
        c12.create_window(21, 194, window=p5, anchor="nw")

        def on_enter(e):
            g1.delete(0, 'end')

        def on_leave(e):
            name = g1.get()
            if name == '':
                g1.insert(0, 'Gender')

        g1 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g1.insert(0, "Gender")
        g1.bind("<FocusIn>", on_enter)
        g1.bind("<FocusOut>", on_leave)
        c12.create_window(384, 74, window=g1, anchor="nw")

        def on_enter(e):
            g2.delete(0, 'end')

        def on_leave(e):
            name = g2.get()
            if name == '':
                g2.insert(0, 'Gender')

        g2 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g2.insert(0, "Gender")
        g2.bind("<FocusIn>", on_enter)
        g2.bind("<FocusOut>", on_leave)
        c12.create_window(384, 104, window=g2, anchor="nw")

        def on_enter(e):
            g3.delete(0, 'end')

        def on_leave(e):
            name = g3.get()
            if name == '':
                g3.insert(0, 'Gender')

        g3 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g3.insert(0, "Gender")
        g3.bind("<FocusIn>", on_enter)
        g3.bind("<FocusOut>", on_leave)
        c12.create_window(384, 134, window=g3, anchor="nw")

        def on_enter(e):
            g4.delete(0, 'end')

        def on_leave(e):
            name = g4.get()
            if name == '':
                g4.insert(0, 'Gender')

        g4 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g4.insert(0, "Gender")
        g4.bind("<FocusIn>", on_enter)
        g4.bind("<FocusOut>", on_leave)
        c12.create_window(384, 164, window=g4, anchor="nw")

        def on_enter(e):
            g5.delete(0, 'end')

        def on_leave(e):
            name = g5.get()
            if name == '':
                g5.insert(0, 'Gender')

        g5 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g5.insert(0, "Gender")
        g5.bind("<FocusIn>", on_enter)
        g5.bind("<FocusOut>", on_leave)
        c12.create_window(384, 194, window=g5, anchor="nw")

        def on_enter(e):
            a1.delete(0, 'end')

        def on_leave(e):
            name = a1.get()
            if name == '':
                a1.insert(0, 'Age')

        a1 = Entry(c12, width=8,  textvariable=age1,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a1.insert(0, "Age")
        a1.bind("<FocusIn>", on_enter)
        a1.bind("<FocusOut>", on_leave)
        c12.create_window(480, 74, window=a1, anchor="nw")

        def on_enter(e):
            a2.delete(0, 'end')

        def on_leave(e):
            name = a2.get()
            if name == '':
                a2.insert(0, 'Age')

        a2 = Entry(c12, width=8,  textvariable=age2,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a2.insert(0, "Age")
        a2.bind("<FocusIn>", on_enter)
        a2.bind("<FocusOut>", on_leave)
        c12.create_window(480, 104, window=a2, anchor="nw")

        def on_enter(e):
            a2.delete(0, 'end')

        def on_leave(e):
            name = a3.get()
            if name == '':
                a3.insert(0, 'Age')

        a3 = Entry(c12, width=8,  textvariable=age3,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a3.insert(0, "Age")
        a3.bind("<FocusIn>", on_enter)
        a3.bind("<FocusOut>", on_leave)
        c12.create_window(480, 134, window=a3, anchor="nw")

        def on_enter(e):
            a4.delete(0, 'end')

        def on_leave(e):
            name = a4.get()
            if name == '':
                a4.insert(0, 'Age')

        a4 = Entry(c12, width=8,  textvariable=age4,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a4.insert(0, "Age")
        a4.bind("<FocusIn>", on_enter)
        a4.bind("<FocusOut>", on_leave)
        c12.create_window(480, 164, window=a4, anchor="nw")

        def on_enter(e):
            a5.delete(0, 'end')

        def on_leave(e):
            name = a5.get()
            if name == '':
                a5.insert(0, 'Age')

        a5 = Entry(c12, width=8,  textvariable=age5,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a5.insert(0, "Age")
        a5.bind("<FocusIn>", on_enter)
        a5.bind("<FocusOut>", on_leave)
        c12.create_window(480, 194, window=a5, anchor="nw")

        def on_enter(e):
            d1.delete(0, 'end')

        def on_leave(e):
            name = d1.get()
            if name == '':
                d1.insert(0, 'Date (yyyy-mm-dd)')

        d1 = Entry(c12, width=18, textvariable=date1, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        d1.insert(0, "Date (yyyy-mm-dd)")
        d1.bind("<FocusIn>", on_enter)
        d1.bind("<FocusOut>", on_leave)
        c12.create_window(370, 228, window=d1, anchor="nw")

        f16 = Frame(c12, width=248, height=21, bg="lavender blush")
        f16.place(x=48, y=225)


        for i in range(len(coach)):
            rb1 = Radiobutton(f16, text=coach[i], font=("Arial Black", 12), fg="Black", bg="lavender blush",
                             variable=coach1, value=coach[i], cursor="hand2", padx=1)
            rb1.pack(side=LEFT, anchor="w")

            def on_enter(e):
                k1.delete(0, 'end')

            def on_leave(e):
                name = k1.get()
                if name == '':
                    k1.insert(0, "No of KIDS (<10yrs)")

            k1 = Entry(c12, width=17,textvariable=kids1, bg="snow", fg="gray21", font=4, border=1, relief=SUNKEN,
                       justify=CENTER)
            k1.insert(0, "No of KIDS (<10yrs)")
            k1.bind("<FocusIn>", on_enter)
            k1.bind("<FocusOut>", on_leave)
            c12.create_window(94, 261, window=k1, anchor="nw")

            def on_enter(e):
                k2.delete(0, 'end')

            def on_leave(e):
                name = k2.get()
                if name == '':
                    k2.insert(0, 'Total Passengers')

            k2 = Entry(c12, width=30, textvariable=kids2, bg="snow", fg="gray21", font=8, border=1, relief=SUNKEN,
                       justify=CENTER)
            k2.insert(0, "Total Passengers")
            k2.bind("<FocusIn>", on_enter)
            k2.bind("<FocusOut>", on_leave)
            c12.create_window(24, 298, window=k2, anchor="nw")
            b22 = Button(c12, text="BACK", font="HANSON 10", bg="misty rose", fg="gray21", command=book1, cursor="hand2")
            c12.create_window(444, 371, window=b22, anchor="w")

            cb1 = Checkbutton(c12, text="ACCEPT TERMS AND CONDITIONS", variable=ck1, font=("Arial Black", 10), command=war, bg="mint cream")
            c12.create_window(48, 344, window=cb1, anchor="nw")

            b23 = Button(c12, text="BOOK\nTICKET", font="HANSON 14", bg="hot pink", fg="white", command=book1_ticket,
                         cursor="hand2")
            c12.create_window(418, 298, window=b23, anchor="w")

    elif ((var1.get()=="Jaipur") and (var2.get()=="Lucknow")):
        c12.create_text(288, 21, text="Train Name: Jan Shatabdi         ", font="HANSON 18", fill="deep pink")
        c12.create_text(218, 48, text="Train Number: 3587482", font="HANSON 18", fill="deep pink")

        train_num = 3587482
        train_name = "Jan Shatabdi"

        def on_enter(e):
            p1.delete(0, 'end')

        def on_leave(e):
            name = p1.get()
            if name == '':
                p1.insert(0, 'Passenger1')

        p1 = Entry(c12, width=32, textvariable=passenger1, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p1.insert(0, "Passenger1")
        p1.bind("<FocusIn>", on_enter)
        p1.bind("<FocusOut>", on_leave)
        c12.create_window(21, 74, window=p1, anchor="nw")

        def on_enter(e):
            p2.delete(0, 'end')

        def on_leave(e):
            name = p2.get()
            if name == '':
                p2.insert(0, 'Passenger2')

        p2 = Entry(c12, width=32, textvariable=passenger2, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p2.insert(0, "Passenger2")
        p2.bind("<FocusIn>", on_enter)
        p2.bind("<FocusOut>", on_leave)
        c12.create_window(21, 104, window=p2, anchor="nw")

        def on_enter(e):
            p3.delete(0, 'end')

        def on_leave(e):
            name = p3.get()
            if name == '':
                p3.insert(0, 'Passenger3')

        p3 = Entry(c12, width=32, textvariable=passenger3, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p3.insert(0, "Passenger3")
        p3.bind("<FocusIn>", on_enter)
        p3.bind("<FocusOut>", on_leave)
        c12.create_window(21, 134, window=p3, anchor="nw")

        def on_enter(e):
            p4.delete(0, 'end')

        def on_leave(e):
            name = p4.get()
            if name == '':
                p4.insert(0, 'Passenger4')

        p4 = Entry(c12, width=32, textvariable=passenger4, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p4.insert(0, "Passenger4")
        p4.bind("<FocusIn>", on_enter)
        p4.bind("<FocusOut>", on_leave)
        c12.create_window(21, 164, window=p4, anchor="nw")

        def on_enter(e):
            p5.delete(0, 'end')

        def on_leave(e):
            name = p5.get()
            if name == '':
                p5.insert(0, 'Passenger5')

        p5 = Entry(c12, width=32, textvariable=passenger5, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p5.insert(0, "Passenger5")
        p5.bind("<FocusIn>", on_enter)
        p5.bind("<FocusOut>", on_leave)
        c12.create_window(21, 194, window=p5, anchor="nw")

        def on_enter(e):
            g1.delete(0, 'end')

        def on_leave(e):
            name = g1.get()
            if name == '':
                g1.insert(0, 'Gender')

        g1 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g1.insert(0, "Gender")
        g1.bind("<FocusIn>", on_enter)
        g1.bind("<FocusOut>", on_leave)
        c12.create_window(384, 74, window=g1, anchor="nw")

        def on_enter(e):
            g2.delete(0, 'end')

        def on_leave(e):
            name = g2.get()
            if name == '':
                g2.insert(0, 'Gender')

        g2 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g2.insert(0, "Gender")
        g2.bind("<FocusIn>", on_enter)
        g2.bind("<FocusOut>", on_leave)
        c12.create_window(384, 104, window=g2, anchor="nw")

        def on_enter(e):
            g3.delete(0, 'end')

        def on_leave(e):
            name = g3.get()
            if name == '':
                g3.insert(0, 'Gender')

        g3 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g3.insert(0, "Gender")
        g3.bind("<FocusIn>", on_enter)
        g3.bind("<FocusOut>", on_leave)
        c12.create_window(384, 134, window=g3, anchor="nw")

        def on_enter(e):
            g4.delete(0, 'end')

        def on_leave(e):
            name = g4.get()
            if name == '':
                g4.insert(0, 'Gender')

        g4 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g4.insert(0, "Gender")
        g4.bind("<FocusIn>", on_enter)
        g4.bind("<FocusOut>", on_leave)
        c12.create_window(384, 164, window=g4, anchor="nw")

        def on_enter(e):
            g5.delete(0, 'end')

        def on_leave(e):
            name = g5.get()
            if name == '':
                g5.insert(0, 'Gender')

        g5 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g5.insert(0, "Gender")
        g5.bind("<FocusIn>", on_enter)
        g5.bind("<FocusOut>", on_leave)
        c12.create_window(384, 194, window=g5, anchor="nw")

        def on_enter(e):
            a1.delete(0, 'end')

        def on_leave(e):
            name = a1.get()
            if name == '':
                a1.insert(0, 'Age')

        a1 = Entry(c12, width=8,  textvariable=age1,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a1.insert(0, "Age")
        a1.bind("<FocusIn>", on_enter)
        a1.bind("<FocusOut>", on_leave)
        c12.create_window(480, 74, window=a1, anchor="nw")

        def on_enter(e):
            a2.delete(0, 'end')

        def on_leave(e):
            name = a2.get()
            if name == '':
                a2.insert(0, 'Age')

        a2 = Entry(c12, width=8,  textvariable=age2,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a2.insert(0, "Age")
        a2.bind("<FocusIn>", on_enter)
        a2.bind("<FocusOut>", on_leave)
        c12.create_window(480, 104, window=a2, anchor="nw")

        def on_enter(e):
            a2.delete(0, 'end')

        def on_leave(e):
            name = a3.get()
            if name == '':
                a3.insert(0, 'Age')

        a3 = Entry(c12, width=8,  textvariable=age3,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a3.insert(0, "Age")
        a3.bind("<FocusIn>", on_enter)
        a3.bind("<FocusOut>", on_leave)
        c12.create_window(480, 134, window=a3, anchor="nw")

        def on_enter(e):
            a4.delete(0, 'end')

        def on_leave(e):
            name = a4.get()
            if name == '':
                a4.insert(0, 'Age')

        a4 = Entry(c12, width=8,  textvariable=age4,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a4.insert(0, "Age")
        a4.bind("<FocusIn>", on_enter)
        a4.bind("<FocusOut>", on_leave)
        c12.create_window(480, 164, window=a4, anchor="nw")

        def on_enter(e):
            a5.delete(0, 'end')

        def on_leave(e):
            name = a5.get()
            if name == '':
                a5.insert(0, 'Age')

        a5 = Entry(c12, width=8,  textvariable=age5,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a5.insert(0, "Age")
        a5.bind("<FocusIn>", on_enter)
        a5.bind("<FocusOut>", on_leave)
        c12.create_window(480, 194, window=a5, anchor="nw")

        def on_enter(e):
            d1.delete(0, 'end')

        def on_leave(e):
            name = d1.get()
            if name == '':
                d1.insert(0, 'Date (yyyy-mm-dd)')

        d1 = Entry(c12, width=18, textvariable=date1, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        d1.insert(0, "Date (yyyy-mm-dd)")
        d1.bind("<FocusIn>", on_enter)
        d1.bind("<FocusOut>", on_leave)
        c12.create_window(370, 228, window=d1, anchor="nw")

        f16 = Frame(c12, width=248, height=21, bg="lavender blush")
        f16.place(x=48, y=225)


        for i in range(len(coach)):
            rb1 = Radiobutton(f16, text=coach[i], font=("Arial Black", 12), fg="Black", bg="lavender blush",
                             variable=coach1, value=coach[i], cursor="hand2", padx=1)
            rb1.pack(side=LEFT, anchor="w")

            def on_enter(e):
                k1.delete(0, 'end')

            def on_leave(e):
                name = k1.get()
                if name == '':
                    k1.insert(0, "No of KIDS (<10yrs)")

            k1 = Entry(c12, width=17,textvariable=kids1, bg="snow", fg="gray21", font=4, border=1, relief=SUNKEN,
                       justify=CENTER)
            k1.insert(0, "No of KIDS (<10yrs)")
            k1.bind("<FocusIn>", on_enter)
            k1.bind("<FocusOut>", on_leave)
            c12.create_window(94, 261, window=k1, anchor="nw")

            def on_enter(e):
                k2.delete(0, 'end')

            def on_leave(e):
                name = k2.get()
                if name == '':
                    k2.insert(0, 'Total Passengers')

            k2 = Entry(c12, width=30, textvariable=kids2, bg="snow", fg="gray21", font=8, border=1, relief=SUNKEN,
                       justify=CENTER)
            k2.insert(0, "Total Passengers")
            k2.bind("<FocusIn>", on_enter)
            k2.bind("<FocusOut>", on_leave)
            c12.create_window(24, 298, window=k2, anchor="nw")
            b22 = Button(c12, text="BACK", font="HANSON 10", bg="misty rose", fg="gray21", command=book1, cursor="hand2")
            c12.create_window(444, 371, window=b22, anchor="w")

            cb1 = Checkbutton(c12, text="ACCEPT TERMS AND CONDITIONS", variable=ck1, font=("Arial Black", 10), command=war, bg="mint cream")
            c12.create_window(48, 344, window=cb1, anchor="nw")

            b23 = Button(c12, text="BOOK\nTICKET", font="HANSON 14", bg="hot pink", fg="white", command=book1_ticket,
                         cursor="hand2")
            c12.create_window(418, 298, window=b23, anchor="w")

    elif ((var1.get()=="Mysuru") and (var2.get()=="Chennai")):
        c12.create_text(288, 21, text="Train Name: Tejas Express       ", font="HANSON 18", fill="deep pink")
        c12.create_text(218, 48, text="Train Number: 3587482", font="HANSON 18", fill="deep pink")

        train_num = 3587482
        train_name = "Tejas Express"

        def on_enter(e):
            p1.delete(0, 'end')

        def on_leave(e):
            name = p1.get()
            if name == '':
                p1.insert(0, 'Passenger1')

        p1 = Entry(c12, width=32, textvariable=passenger1, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p1.insert(0, "Passenger1")
        p1.bind("<FocusIn>", on_enter)
        p1.bind("<FocusOut>", on_leave)
        c12.create_window(21, 74, window=p1, anchor="nw")

        def on_enter(e):
            p2.delete(0, 'end')

        def on_leave(e):
            name = p2.get()
            if name == '':
                p2.insert(0, 'Passenger2')

        p2 = Entry(c12, width=32, textvariable=passenger2, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p2.insert(0, "Passenger2")
        p2.bind("<FocusIn>", on_enter)
        p2.bind("<FocusOut>", on_leave)
        c12.create_window(21, 104, window=p2, anchor="nw")

        def on_enter(e):
            p3.delete(0, 'end')

        def on_leave(e):
            name = p3.get()
            if name == '':
                p3.insert(0, 'Passenger3')

        p3 = Entry(c12, width=32, textvariable=passenger3, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p3.insert(0, "Passenger3")
        p3.bind("<FocusIn>", on_enter)
        p3.bind("<FocusOut>", on_leave)
        c12.create_window(21, 134, window=p3, anchor="nw")

        def on_enter(e):
            p4.delete(0, 'end')

        def on_leave(e):
            name = p4.get()
            if name == '':
                p4.insert(0, 'Passenger4')

        p4 = Entry(c12, width=32, textvariable=passenger4, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p4.insert(0, "Passenger4")
        p4.bind("<FocusIn>", on_enter)
        p4.bind("<FocusOut>", on_leave)
        c12.create_window(21, 164, window=p4, anchor="nw")

        def on_enter(e):
            p5.delete(0, 'end')

        def on_leave(e):
            name = p5.get()
            if name == '':
                p5.insert(0, 'Passenger5')

        p5 = Entry(c12, width=32, textvariable=passenger5, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        p5.insert(0, "Passenger5")
        p5.bind("<FocusIn>", on_enter)
        p5.bind("<FocusOut>", on_leave)
        c12.create_window(21, 194, window=p5, anchor="nw")

        def on_enter(e):
            g1.delete(0, 'end')

        def on_leave(e):
            name = g1.get()
            if name == '':
                g1.insert(0, 'Gender')

        g1 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g1.insert(0, "Gender")
        g1.bind("<FocusIn>", on_enter)
        g1.bind("<FocusOut>", on_leave)
        c12.create_window(384, 74, window=g1, anchor="nw")

        def on_enter(e):
            g2.delete(0, 'end')

        def on_leave(e):
            name = g2.get()
            if name == '':
                g2.insert(0, 'Gender')

        g2 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g2.insert(0, "Gender")
        g2.bind("<FocusIn>", on_enter)
        g2.bind("<FocusOut>", on_leave)
        c12.create_window(384, 104, window=g2, anchor="nw")

        def on_enter(e):
            g3.delete(0, 'end')

        def on_leave(e):
            name = g3.get()
            if name == '':
                g3.insert(0, 'Gender')

        g3 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g3.insert(0, "Gender")
        g3.bind("<FocusIn>", on_enter)
        g3.bind("<FocusOut>", on_leave)
        c12.create_window(384, 134, window=g3, anchor="nw")

        def on_enter(e):
            g4.delete(0, 'end')

        def on_leave(e):
            name = g4.get()
            if name == '':
                g4.insert(0, 'Gender')

        g4 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g4.insert(0, "Gender")
        g4.bind("<FocusIn>", on_enter)
        g4.bind("<FocusOut>", on_leave)
        c12.create_window(384, 164, window=g4, anchor="nw")

        def on_enter(e):
            g5.delete(0, 'end')

        def on_leave(e):
            name = g5.get()
            if name == '':
                g5.insert(0, 'Gender')

        g5 = Entry(c12, width=8,  bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        g5.insert(0, "Gender")
        g5.bind("<FocusIn>", on_enter)
        g5.bind("<FocusOut>", on_leave)
        c12.create_window(384, 194, window=g5, anchor="nw")

        def on_enter(e):
            a1.delete(0, 'end')

        def on_leave(e):
            name = a1.get()
            if name == '':
                a1.insert(0, 'Age')

        a1 = Entry(c12, width=8,  textvariable=age1,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a1.insert(0, "Age")
        a1.bind("<FocusIn>", on_enter)
        a1.bind("<FocusOut>", on_leave)
        c12.create_window(480, 74, window=a1, anchor="nw")

        def on_enter(e):
            a2.delete(0, 'end')

        def on_leave(e):
            name = a2.get()
            if name == '':
                a2.insert(0, 'Age')

        a2 = Entry(c12, width=8,  textvariable=age2,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a2.insert(0, "Age")
        a2.bind("<FocusIn>", on_enter)
        a2.bind("<FocusOut>", on_leave)
        c12.create_window(480, 104, window=a2, anchor="nw")

        def on_enter(e):
            a2.delete(0, 'end')

        def on_leave(e):
            name = a3.get()
            if name == '':
                a3.insert(0, 'Age')

        a3 = Entry(c12, width=8,  textvariable=age3,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a3.insert(0, "Age")
        a3.bind("<FocusIn>", on_enter)
        a3.bind("<FocusOut>", on_leave)
        c12.create_window(480, 134, window=a3, anchor="nw")

        def on_enter(e):
            a4.delete(0, 'end')

        def on_leave(e):
            name = a4.get()
            if name == '':
                a4.insert(0, 'Age')

        a4 = Entry(c12, width=8,  textvariable=age4,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a4.insert(0, "Age")
        a4.bind("<FocusIn>", on_enter)
        a4.bind("<FocusOut>", on_leave)
        c12.create_window(480, 164, window=a4, anchor="nw")

        def on_enter(e):
            a5.delete(0, 'end')

        def on_leave(e):
            name = a5.get()
            if name == '':
                a5.insert(0, 'Age')

        a5 = Entry(c12, width=8,  textvariable=age5,bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        a5.insert(0, "Age")
        a5.bind("<FocusIn>", on_enter)
        a5.bind("<FocusOut>", on_leave)
        c12.create_window(480, 194, window=a5, anchor="nw")

        def on_enter(e):
            d1.delete(0, 'end')

        def on_leave(e):
            name = d1.get()
            if name == '':
                d1.insert(0, 'Date (yyyy-mm-dd)')

        d1 = Entry(c12, width=18, textvariable=date1, bg="snow", fg="black", font=8, border=1, relief=SUNKEN, justify=CENTER)
        d1.insert(0, "Date (yyyy-mm-dd)")
        d1.bind("<FocusIn>", on_enter)
        d1.bind("<FocusOut>", on_leave)
        c12.create_window(370, 228, window=d1, anchor="nw")

        f16 = Frame(c12, width=248, height=21, bg="lavender blush")
        f16.place(x=48, y=225)


        for i in range(len(coach)):
            rb1 = Radiobutton(f16, text=coach[i], font=("Arial Black", 12), fg="Black", bg="lavender blush",
                             variable=coach1, value=coach[i], cursor="hand2", padx=1)
            rb1.pack(side=LEFT, anchor="w")

            def on_enter(e):
                k1.delete(0, 'end')

            def on_leave(e):
                name = k1.get()
                if name == '':
                    k1.insert(0, "No of KIDS (<10yrs)")

            k1 = Entry(c12, width=17,textvariable=kids1, bg="snow", fg="gray21", font=4, border=1, relief=SUNKEN,
                       justify=CENTER)
            k1.insert(0, "No of KIDS (<10yrs)")
            k1.bind("<FocusIn>", on_enter)
            k1.bind("<FocusOut>", on_leave)
            c12.create_window(94, 261, window=k1, anchor="nw")

            def on_enter(e):
                k2.delete(0, 'end')

            def on_leave(e):
                name = k2.get()
                if name == '':
                    k2.insert(0, 'Total Passengers')

            k2 = Entry(c12, width=30, textvariable=kids2, bg="snow", fg="gray21", font=8, border=1, relief=SUNKEN,
                       justify=CENTER)
            k2.insert(0, "Total Passengers")
            k2.bind("<FocusIn>", on_enter)
            k2.bind("<FocusOut>", on_leave)
            c12.create_window(24, 298, window=k2, anchor="nw")
            b22 = Button(c12, text="BACK", font="HANSON 10", bg="misty rose", fg="gray21", command=book1, cursor="hand2")
            c12.create_window(444, 371, window=b22, anchor="w")

            cb1 = Checkbutton(c12, text="ACCEPT TERMS AND CONDITIONS", variable=ck1, font=("Arial Black", 10), command=war, bg="mint cream")
            c12.create_window(48, 344, window=cb1, anchor="nw")

            b23 = Button(c12, text="BOOK\nTICKET", font="HANSON 14", bg="hot pink", fg="white", command=book1_ticket,
                         cursor="hand2")
            c12.create_window(418, 298, window=b23, anchor="w")

    else:
        tmsg.showinfo("TRAIN STATUS", f"No Train runs between {var1.get()} and {var2.get()}")
        book1()

def ticket_print():
    def save_canvas_as_image(c13, filename):
        c13.postscript(file=filename, colormode='color')
        img = Image.open(filename)
        img.save(filename + '.png', 'png')
        img.close()

    def on_save_button_click():
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if filename:
            save_canvas_as_image(c13, filename)

    f17 = Frame(root, width=584, height=384)
    f17.place(x=784, y=244)
    c13 = Canvas(f17, bg="floral white", width=584, height=384)
    c13.pack()
    c13.create_text(294, 21, text="RAILWAY RESERVATION SYSTEM", font="HANSON 18", fill="PeachPuff2")
    c13.create_text(294, 44, text="HAPPY JOURNEY !", font="HANSON 12", fill="PeachPuff1")
    if ((var1.get() == "New Delhi") and (var2.get() == "Mumbai")):
        c13.create_text(104, 68, text="Hindustan Express", font=("Oswald Regular",18), fill="RosyBrown3")
        c13.create_text(494, 68, text="3587482", font=("Oswald Regular", 18), fill="RosyBrown3")
    elif ((var1.get() == "Chennai") and (var2.get() == "Bangalore")):
        c13.create_text(104, 68, text="Shatabdi Express", font=("Oswald Regular", 18), fill="RosyBrown3")
        c13.create_text(494, 68, text="347583", font=("Oswald Regular", 18), fill="RosyBrown3")
    elif ((var1.get() == "Kolkata") and (var2.get() == "Delhi")):
        c13.create_text(104, 68, text="Duronto Express", font=("Oswald Regular", 18), fill="RosyBrown3")
        c13.create_text(494, 68, text="234838", font=("Oswald Regular", 18), fill="RosyBrown3")
    elif ((var1.get() == "Pune") and (var2.get() == "Ahmedabad")):
        c13.create_text(104, 68, text="Garib Rath", font=("Oswald Regular", 18), fill="RosyBrown3")
        c13.create_text(494, 68, text="234785", font=("Oswald Regular", 18), fill="RosyBrown3")
    elif ((var1.get() == "Hyderabad") and (var2.get() == "Bhopal")):
        c13.create_text(104, 68, text="Humsafar Express", font=("Oswald Regular", 18), fill="RosyBrown3")
        c13.create_text(494, 68, text="438743", font=("Oswald Regular", 18), fill="RosyBrown3")
    elif ((var1.get() == "Jaipur") and (var2.get() == "Lucknow")):
        c13.create_text(104, 68, text="Jan Shatabdi", font=("Oswald Regular", 18), fill="RosyBrown3")
        c13.create_text(494, 68, text="443494", font=("Oswald Regular", 18), fill="RosyBrown3")
    elif ((var1.get() == "Mysuru") and (var2.get() == "Chennai")):
        c13.create_text(104, 68, text="Tejas Express", font=("Oswald Regular", 18), fill="RosyBrown3")
        c13.create_text(494, 68, text="324738", font=("Oswald Regular", 18), fill="RosyBrown3")
    c13.create_text(304, 68, text=f"{var1.get()} ----> {var2.get()}", font=("Coburn", 12), fill="RosyBrown2")
    c13.create_text(248, 144, text=f"Passenger1 - - - {passenger1.get()} - - - {age1.get()}yrs - - - ", font=("Coburn", 15), fill="RosyBrown2")
    c13.create_text(248, 174, text=f"Passenger2 - - - {passenger2.get()} - - - {age2.get()}yrs - - - ",
                    font=("Coburn", 15), fill="RosyBrown2")
    c13.create_text(248, 204, text=f"Passenger3 - - - {passenger3.get()} - - - {age3.get()}yrs - - - ",
                    font=("Coburn", 15), fill="RosyBrown2")
    c13.create_text(248, 234, text=f"Passenger4 - - - {passenger4.get()} - - - {age4.get()}yrs - - - ",
                    font=("Coburn", 15), fill="RosyBrown2")
    c13.create_text(248, 264, text=f"Passenger5 - - - {passenger5.get()} - - - {age5.get()}yrs - - - ",
                    font=("Coburn", 15), fill="RosyBrown2")
    c13.create_text(504, 44, text=f"{date1.get()}",
                    font=("Coburn", 14), fill="RosyBrown2")
    c13.create_text(248, 284, text=" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ",
                    font=("Coburn", 15), fill="RosyBrown1")
    c13.create_text(384, 104, text=f"- Ticket Number - {ticket_number} -",
                    font=("Coburn", 18), fill="RosyBrown2")
    c13.create_text(84, 104, text=f"- PNR - {pnr} -",
                    font=("Oswald Regular", 18), fill="RosyBrown2")
    c13.create_text(284, 304, text=f" - - - - {ticket_number} - - - - {pnr} - - - - ",
                    font=("Coburn", 24), fill="antique white")
    c13.create_text(248, 324,
                    text=" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ",
                    font=("Coburn", 15), fill="RosyBrown1")
    c13.create_text(284, 348, text=f" - - - - Happy Journey- - - - ",
                    font=("Coburn", 18), fill="bisque")

    b29 = Button(c13, width=4, text="BACK", font="HANSON 8", bg="bisque", fg="gray44",
                 border=1,
                 command=sign,
                 cursor="hand2")
    c13.create_window(538, 364, window=b29, anchor="nw")
    save_button = Button(c13, text="Print",font="HANSON 8", bg="bisque", fg="black", border=1, command=on_save_button_click, cursor="hand2")
    c13.create_window(484, 364, window=save_button, anchor="nw")
    b30 = Button(c13, width=4, text="PAY", font="HANSON 12", bg="gold", fg="black",border=1,command=pay,cursor="hand2")
    c13.create_window(84, 344, window=b30, anchor="nw")
    c13.create_text(44, 364, text="₹844", font=("Coburn", 21), fill="RosyBrown2")

def cancel1():
    f18 = Frame(root, width=584, height=384)
    f18.place(x=784, y=244)
    c14 = Canvas(f18, bg="lavender blush", width=584, height=384)
    c14.pack()

    def cancel3():
        a = tmsg.askquestion("CANCEL TICKET", "Are you Sure")
        if a=="yes":
            tmsg.showinfo("CANCELLATION", "TICKET CANCELLED")
            sign()
        else:
            cancel2()

    def cancel2():
        entered_pnr1 = entered_pnr.get()

        with open("C:/Users/MANMOHAN C A/Desktop/ticket.txt", "r") as file:
            for line in file:
                if f"PNR: {entered_pnr1}" in line:
                    elements = line.split(',')
                    stored_pnr= elements[0].strip()
                    stored_ticket_num= elements[1].strip()
                    stored_coach= elements[3].strip()
                    stored_train_num= elements[4].strip()
                    stored_train_name= elements[5].strip()

                    f19 = Frame(root, width=584, height=384)
                    f19.place(x=784, y=244)

                    c15= Canvas(f19, bg="lavender blush", width=584, height=384)
                    c15.pack()

                    c15.create_text(294, 24, text="CANCELLATION OF TICKET", font="HANSON 18", fill="deep pink")
                    c15.create_text(284, 84, text=f"PNR: {stored_pnr[5:]}", font=("Verdana",14, "bold"), fill="salmon1")
                    c15.create_text(244, 112, text=f"TICKET NUMBER: {stored_ticket_num[15:]}", font=("Verdana", 14, "bold"),
                                    fill="salmon1")
                    c15.create_text(228, 140, text=f"TRAIN NUMBER: {stored_train_num[14:]}",
                                    font=("Verdana", 14, "bold"),
                                    fill="salmon1")
                    c15.create_text(294, 168, text=f"TRAIN NAME: {stored_train_name[7:]}",
                                    font=("Verdana", 14, "bold"),
                                    fill="salmon1")
                    c15.create_text(184, 196, text=f"SELECTED COACH: {stored_coach[7:]}",
                                    font=("Verdana", 14, "bold"),
                                    fill="salmon1")

                    b26 = Button(c15, width=18, text="CANCEL TICKET", font="HANSON 14", bg="old lace", fg="red1", border=1,
                                 command=cancel3,
                                 cursor="hand2")
                    c15.create_window(134, 244, window=b26, anchor="nw")
                    b27 = Button(c15, width=8, text="BACK", font="HANSON 12", bg="azure", fg="gray21",
                                 border=1,
                                 command=cancel1,
                                 cursor="hand2")
                    c15.create_window(234, 312, window=b27, anchor="nw")

                else:
                    tmsg.showerror("Error", "Invalid PNR.")

    entered_pnr=StringVar()

    c14.create_text(294, 48, text="CANCELLATION\n    OF TICKET", font="HANSON 24", fill="deep pink")

    c14.create_text(298, 154, text="     Enter\nPNR Number", font="HANSON 18", fill="tomato")

    pnr_entry = Entry(c14, width=28, textvariable=entered_pnr, bg="azure", fg="black", font=34, border=0)
    c14.create_window(138, 204, window=pnr_entry, anchor="nw")
    b25 = Button(c14, width=8, text="NEXT", font="HANSON 14", bg="misty rose", fg="black", border=1, command=cancel2,
                cursor="hand2")
    c14.create_window(221, 244, window=b25, anchor="nw")
    b28 = Button(c14, width=8, text="BACK", font="HANSON 12", bg="azure", fg="gray21",
                 border=1,
                 command=sign,
                 cursor="hand2")
    c14.create_window(234, 312, window=b28, anchor="nw")


def home():
    f2 = Frame(root, width=584, height=384)
    f2.place(x=784, y=244)
    c1 = Canvas(f2, bg="lavender blush", width=584, height=384)
    c1.pack()
    c1.create_text(284, 64, text="WELCOME!", font="HANSON 28", fill="deep pink")
    b1 = Button(c1, text="Create New Account", font="HANSON 18", bg="azure", fg="black", command=new,  cursor="hand2")
    b2 = Button(c1, text="Login", font="HANSON 18", bg="azure", fg="black",command=login,  cursor="hand2")
    c1.create_window(84, 140, window=b1, anchor="nw")
    c1.create_window(221, 244, window=b2, anchor="nw")

home()

mainloop()