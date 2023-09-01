import tkinter
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from CTkTable import CTkTable
# import tkinter as tk
from PIL import ImageTk,Image
import os
import book_ticket
import login
import search_train
import search_station
import wallet
# import locale

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
app = ctk.CTk() 

def close_wm():
    app.quit()
    app.destroy()

def login_button_function(entry1, entry2):
    if "data" not in os.listdir():
        os.mkdir("data")

    usr = entry1.get()
    pas = entry2.get()

    logged = login.login(usr, pas)

    if (logged):
        app.withdraw()            # destroy current window and creating new one 
        main_page()
    
    else:
        msg1 = CTkMessagebox(title="Login Error", message="Wrong username and password !", master = app, justify = "center", icon="cancel")
        msg1.after(250, lambda : msg1.iconbitmap("assets\\icon.ico"))

def signup_button_function(app_sign, entry1, entry2, entry3):
    if "data" not in os.listdir():
        os.mkdir("data")

    usr = entry1.get()
    pas = entry2.get()
    conpas = entry3.get()

    if (pas == "" or usr == ""):
        msg1 = CTkMessagebox(title="Signup Error", message="Username and password can't be empty !", master = app_sign, justify = "center", icon="cancel")
        msg1.after(250, lambda : msg1.iconbitmap("assets\\icon.ico"))
    else:
        if (pas == conpas):
            registered = login.signup(usr, pas)
            if (registered):
                msg1 = CTkMessagebox(title="Signed In", message="Signed up successfully !", master = app_sign, justify = "center",
                    icon="check")
                msg1.after(250, lambda : msg1.iconbitmap("assets\\icon.ico"))
            else:
                msg1 = CTkMessagebox(title="Signup Error", message="Username not available !", master = app_sign, justify = "center", icon="cancel")
                msg1.after(250, lambda : msg1.iconbitmap("assets\\icon.ico"))
        else:
            msg1 = CTkMessagebox(title="Signup Error", message="Passwords do not match !", master = app_sign, justify = "center", icon="cancel")
            msg1.after(250, lambda : msg1.iconbitmap("assets\\icon.ico"))

def sign_up_invoke_function():
    app.withdraw()
    signup_page()
    # main_page()

def log_in_invoke_function(app_sign):
    app_sign.destroy()
    app.deiconify()
    app.grab_set()
    login_page()
    

def login_page(): #creating cutstom tkinter window
    app.resizable(False, False)
    app.geometry("600x400")
    app.title('Login')
    app.iconbitmap("assets\\icon.ico")

    img1=ImageTk.PhotoImage(Image.open("./assets/pattern.jpg"))
    l1=ctk.CTkLabel(master=app,image=img1)
    l1.pack()

    #creating custom frame
    frame=ctk.CTkFrame(master=l1, width=320, height=300, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2=ctk.CTkLabel(master=frame, text="Log In",font=('Century Gothic',30))
    l2.place(x=110, y=40)

    entry1=ctk.CTkEntry(master=frame, width=220, placeholder_text='Username')
    entry1.place(x=50, y=110)

    entry2=ctk.CTkEntry(master=frame, width=220, placeholder_text='Password', show="●")
    entry2.place(x=50, y=155)

    l3=ctk.CTkLabel(master=frame, text="New user ?",font=('Century Gothic',14))
    l3.place(x=80,y=190)

    button0 = ctk.CTkButton(master=frame, width=50, text="Sign Up", command=lambda : sign_up_invoke_function(), corner_radius=6)
    button0.place(x=170, y=190)

    #Create custom button
    button1 = ctk.CTkButton(master=frame, width=220, text="Login", command=lambda : login_button_function(entry1, entry2), corner_radius=6)
    button1.place(x=50, y=225)

    app.protocol("WM_DELETE_WINDOW", close_wm)
    app.mainloop()

def signup_page():
    app_sign = ctk.CTkToplevel(app)  #creating cutstom tkinter window
    app_sign.resizable(False, False)
    app_sign.geometry("600x400")
    app_sign.title('Signup')
    app_sign.after(250, lambda : app_sign.iconbitmap("assets\\icon.ico"))
    app_sign.grab_set()
    # print(app.state())
    # app.state("normal")

    img1=ImageTk.PhotoImage(Image.open("./assets/pattern.jpg"))
    l1=ctk.CTkLabel(master=app_sign,image=img1)
    l1.pack()

    #creating custom frame
    frame=ctk.CTkFrame(master=l1, width=320, height=345, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2=ctk.CTkLabel(master=frame, text="Sign Up",font=('Century Gothic',30))
    l2.place(x=110, y=40)

    entry1=ctk.CTkEntry(master=frame, width=220, placeholder_text='Username')
    entry1.place(x=50, y=110)

    entry2=ctk.CTkEntry(master=frame, width=220, placeholder_text='Password', show="●")
    entry2.place(x=50, y=155)

    entry3=ctk.CTkEntry(master=frame, width=220, placeholder_text='Confirm Password', show="●")
    entry3.place(x=50, y=200)

    l3=ctk.CTkLabel(master=frame, text="Already registered ?",font=('Century Gothic',14))
    l3.place(x=63,y=235)

    button0 = ctk.CTkButton(master=frame, width=50, text="Log In", command=lambda : log_in_invoke_function(app_sign), corner_radius=6)
    button0.place(x=207, y=235)

    #Create custom button
    button1 = ctk.CTkButton(master=frame, width=220, text="Signup", command=lambda : signup_button_function(app, entry1, entry2, entry3), corner_radius=6)
    button1.place(x=50, y=270)

    app_sign.protocol("WM_DELETE_WINDOW", close_wm)
    # app.mainloop()

def book_button_function(app_book, adult_var, child_var, entry1, entry2):
    adults = int(adult_var.get())
    children = int(child_var.get())
    src = entry1.get().upper()
    dest = entry2.get().upper()

    booked, fare, tickets = book_ticket.book(src, dest, adults, children)

    if booked:
        conf = CTkMessagebox(title="Confirmation", message=f"Fare : Rs {fare}\nDo you want to continue ?", master = app_book, justify = "center", icon="question", option_1="yes", option_2="No")
        conf.after(250, lambda : conf.iconbitmap("assets\\icon.ico"))
        
        choice = conf.get()

        if (choice == "yes"):
            paid = book_ticket.ticket(tickets, fare)

            if paid:
                msg1 = CTkMessagebox(title="Ticket booked", message="Ticket booked successfully !", master = app_book, justify = "center",
                    icon="check")
                msg1.after(250, lambda : msg1.iconbitmap("assets\\icon.ico"))
                
        else:
            paid = False
        
        if not paid:
            msg1 = CTkMessagebox(title="Failed", message="Payment failed !", master = app_book, justify = "center", icon="cancel")
            msg1.after(250, lambda : msg1.iconbitmap("assets\\icon.ico"))

    else:
        msg1 = CTkMessagebox(title="Booking Error", message="No stations found !", master = app_book, justify = "center", icon="cancel")
        msg1.after(250, lambda : msg1.iconbitmap("assets\\icon.ico"))

def back_button(app_main, app_back):
    app_back.withdraw()
    app_main.deiconify()
    app_main.grab_set()

def book_page(app_main):
    app_book = ctk.CTkToplevel(app)
    app_book.resizable(False, False)
    app_book.geometry("600x400")
    app_book.title('Book ticket')
    app_book.after(250, lambda : app_book.iconbitmap("assets\\icon.ico"))
    app_book.grab_set()

    img1=ImageTk.PhotoImage(Image.open("./assets/pattern.jpg"))
    l1=ctk.CTkLabel(master=app_book,image=img1)
    l1.pack()

    #creating custom frame
    frame=ctk.CTkFrame(master=l1, width=320, height=325, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    h,w = 20,20

    img2=ctk.CTkImage(Image.open("./assets/back.png").resize((h,w), Image.ANTIALIAS))
    button2= ctk.CTkButton(master=frame, image=img2, text="", width=h, height=w, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF', command=lambda : back_button(app_main, app_book))
    button2.place(x=20, y=20)

    l2=ctk.CTkLabel(master=frame, text="Book ticket",font=('Century Gothic',30))
    l2.place(x=80, y=40)

    entry1=ctk.CTkEntry(master=frame, width=220, placeholder_text='Source station')
    entry1.place(x=50, y=110)

    entry2=ctk.CTkEntry(master=frame, width=220, placeholder_text='Destination station')
    entry2.place(x=50, y=155)

    adult_var = ctk.StringVar(value="1")
    child_var = ctk.StringVar(value="0")

    l3 = ctk.CTkLabel(master=frame, text="Adult : ", font=('Century Gothic',14))
    l3.place(x=50, y=200)

    # Occupation combo box
    opt1 = ctk.CTkOptionMenu(master=frame, values=[str(i) for i in range(1, 11)], width=50, variable=adult_var)
    opt1.place(x=100, y=200)

    l4 = ctk.CTkLabel(master=frame, text="Child : ", font=('Century Gothic',14))
    l4.place(x=168, y=200)

    # Occupation combo box
    opt2 = ctk.CTkOptionMenu(master=frame, values=[str(i) for i in range(1, 11)], width=50, variable=child_var)
    opt2.place(x=218, y=200)

    button1 = ctk.CTkButton(master=frame, width=220, text="Book now", command=lambda : book_button_function(app_book, adult_var, child_var, entry1, entry2), corner_radius=6)
    button1.place(x=50, y=245)

    app_book.protocol("WM_DELETE_WINDOW", close_wm)

def book_page_invoke(app_main):
    app_main.withdraw()
    book_page(app_main)

def search_train_button(app_train, entry1, entry2):
    src = entry1.get()
    dest = entry2.get()

    # print(f"{src}-->{dest}")

    status, data = search_train.searchT(src, dest)

    # print(f"{status}-->{data}")

    if (status):
        app_train_table = ctk.CTkToplevel(app)
        app_train_table.resizable(False, False)
        app_train_table.geometry("1000x563")
        app_train_table.title('Train time table')
        app_train_table.after(250, lambda : app_train_table.iconbitmap("assets\\icon.ico"))
        app_train_table.grab_set()

        img1=ImageTk.PhotoImage(Image.open("./assets/pattern.jpg"))
        l1=ctk.CTkLabel(master=app_train_table,image=img1)
        l1.pack()

        # #creating custom frame
        frame=ctk.CTkFrame(master=l1, width=855, height=520, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        l2=ctk.CTkLabel(master=frame, text="Time table",font=('Century Gothic',30))
        l2.place(x=350, y=20)

        frame1 = ctk.CTkScrollableFrame(master=frame, width=824, height=400, corner_radius=15)
        frame1.place(x=0, y=70)

        # h,w = 20,20

        # img2=ctk.CTkImage(Image.open("./assets/back.png").resize((h,w), Image.ANTIALIAS))
        # button2= ctk.CTkButton(master=frame, image=img2, text="", width=h, height=w, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF', command=lambda : back_button(app_train, app_train_table))
        # button2.place(x=20, y=20)

        table = CTkTable(master = frame1, values = data)
        table.pack()
        # print(table.winfo_width(), table.winfo_height())

    elif (len(data)==0):
        msg1 = CTkMessagebox(title="Error", message="No such stations present !", master = app_train, justify = "center", icon="cancel")
        msg1.after(250, lambda : msg1.iconbitmap("assets\\icon.ico"))

    else:
        msg1 = CTkMessagebox(title="Not found", message="No trains available between the stations now !", master = app_train, justify = "center", icon="info")
        msg1.after(250, lambda : msg1.iconbitmap("assets\\icon.ico"))

def train_page_invoke(app_main):
    app_main.withdraw()
    train_page(app_main)

def train_page(app_main):
    app_train = ctk.CTkToplevel(app)
    app_train.resizable(False, False)
    app_train.geometry("600x400")
    app_train.title('Search train')
    app_train.after(250, lambda : app_train.iconbitmap("assets\\icon.ico"))
    app_train.grab_set()

    img1=ImageTk.PhotoImage(Image.open("./assets/pattern.jpg"))
    l1=ctk.CTkLabel(master=app_train,image=img1)
    l1.pack()

    #creating custom frame
    frame=ctk.CTkFrame(master=l1, width=320, height=290, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    h,w = 20,20

    img2=ctk.CTkImage(Image.open("./assets/back.png").resize((h,w), Image.ANTIALIAS))
    button2= ctk.CTkButton(master=frame, image=img2, text="", width=h, height=w, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF', command=lambda : back_button(app_main, app_train))
    button2.place(x=20, y=20)

    l2=ctk.CTkLabel(master=frame, text="Search trains",font=('Century Gothic',30))
    l2.place(x=80, y=40)

    entry1=ctk.CTkEntry(master=frame, width=220, placeholder_text='Source station')
    entry1.place(x=50, y=110)

    entry2=ctk.CTkEntry(master=frame, width=220, placeholder_text='Destination station')
    entry2.place(x=50, y=155)


    button1 = ctk.CTkButton(master=frame, width=220, text="Search", command=lambda : search_train_button(app_train, entry1, entry2), corner_radius=6)
    button1.place(x=50, y=210)

    app_train.protocol("WM_DELETE_WINDOW", close_wm)

def station_page_invoke(app_main):
    app_main.withdraw()
    station_page(app_main)

def search_station_button(app_station, entry1):
    src = entry1.get()

    # print(f"{src}-->{dest}")

    status, data = search_station.searchS(src)
    # print(search_station.searchS(src))

    # print(f"{status}-->{data}")

    if (status):
        app_station_table = ctk.CTkToplevel(app)
        app_station_table.resizable(False, False)
        app_station_table.geometry("600x400")
        app_station_table.title('Stations')
        app_station_table.after(250, lambda : app_station_table.iconbitmap("assets\\icon.ico"))
        app_station_table.grab_set()

        img1=ImageTk.PhotoImage(Image.open("./assets/pattern.jpg"))
        l1=ctk.CTkLabel(master=app_station_table,image=img1)
        l1.pack()

        # #creating custom frame
        frame=ctk.CTkFrame(master=l1, width=351, height=380, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        l2=ctk.CTkLabel(master=frame, text="Stations",font=('Century Gothic',30))
        l2.place(x=120, y=20)

        frame1 = ctk.CTkScrollableFrame(master=frame, width=320, height=250, corner_radius=15)
        frame1.place(x=0, y=70)

        # h,w = 20,20

        # img2=ctk.CTkImage(Image.open("./assets/back.png").resize((h,w), Image.ANTIALIAS))
        # button2= ctk.CTkButton(master=frame, image=img2, text="", width=h, height=w, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF', command=lambda : back_button(app_train, app_train_table))
        # button2.place(x=20, y=20)

        table = CTkTable(master = frame1, values = data)
        # table.set_size(200, 300)
        table.pack()
        # print(table.winfo_width(), table.winfo_height())

    else:
        msg1 = CTkMessagebox(title="Error", message="No such stations present !", master = app_station, justify = "center", icon="cancel")
        msg1.after(250, lambda : msg1.iconbitmap("assets\\icon.ico"))
    
    
def station_page(app_main):
    app_station = ctk.CTkToplevel(app)
    app_station.resizable(False, False)
    app_station.geometry("450x338")
    app_station.title('Search station')
    app_station.after(250, lambda : app_station.iconbitmap("assets\\icon.ico"))
    app_station.grab_set()

    img1=ImageTk.PhotoImage(Image.open("./assets/pattern.jpg"))
    l1=ctk.CTkLabel(master=app_station,image=img1)
    l1.pack()

    #creating custom frame
    frame=ctk.CTkFrame(master=l1, width=320, height=235, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    h,w = 20,20

    img2=ctk.CTkImage(Image.open("./assets/back.png").resize((h,w), Image.ANTIALIAS))
    button2= ctk.CTkButton(master=frame, image=img2, text="", width=h, height=w, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF', command=lambda : back_button(app_main, app_station))
    button2.place(x=20, y=20)

    l2=ctk.CTkLabel(master=frame, text="Search stations",font=('Century Gothic',30))
    l2.place(x=58, y=40)

    entry1=ctk.CTkEntry(master=frame, width=220, placeholder_text='Station name')
    entry1.place(x=50, y=110)


    button1 = ctk.CTkButton(master=frame, width=220, text="Search", command=lambda : search_station_button(app_station, entry1), corner_radius=6)
    button1.place(x=50, y=155)

    app_station.protocol("WM_DELETE_WINDOW", close_wm)

def show_page(app_main):
    # print(f"{src}-->{dest}")
    book_ticket.refresh()

    status, data = book_ticket.show_ticket()
    # print(search_station.searchS(src))

    # print(f"{status}-->{data}")

    if (status):
        app_ticket = ctk.CTkToplevel(app)
        app_ticket.resizable(False, False)
        app_ticket.geometry("800x500")
        app_ticket.title('Show ticket')
        app_ticket.after(250, lambda : app_ticket.iconbitmap("assets\\icon.ico"))
        app_ticket.grab_set()

        img1=ImageTk.PhotoImage(Image.open("./assets/pattern.jpg"))
        l1=ctk.CTkLabel(master=app_ticket,image=img1)
        l1.pack()

        # creating custom frame
        frame=ctk.CTkFrame(master=l1, width=631, height=380, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        l2=ctk.CTkLabel(master=frame, text="Tickets",font=('Century Gothic',30))
        l2.place(x=270, y=20)

        frame1 = ctk.CTkScrollableFrame(master=frame, width=600, height=250, corner_radius=15)
        frame1.place(x=0, y=70)

        # h,w = 20,20

        # img2=ctk.CTkImage(Image.open("./assets/back.png").resize((h,w), Image.ANTIALIAS))
        # button2= ctk.CTkButton(master=frame, image=img2, text="", width=h, height=w, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF', command=lambda : back_button(app_train, app_train_table))
        # button2.place(x=20, y=20)

        table = CTkTable(master = frame1, values = data)
        # table.set_size(200, 300)
        table.pack()
        # print(table.winfo_width(), table.winfo_height())

    else:
        msg1 = CTkMessagebox(title="Error", message="No tickets booked yet !", master = app_main, justify = "center", icon="cancel")
        msg1.after(250, lambda : msg1.iconbitmap("assets\\icon.ico"))

def wallet_page_invoke(app_main):
    app_main.withdraw()
    obj = wallet_page()
    obj.app(app_main)



class wallet_page:
    def app(self, app_main):
        self.wallet1 = wallet.wallet()
        self.bal = self.wallet1.balance

        app_wallet = ctk.CTkToplevel(app)
        app_wallet.resizable(False, False)
        app_wallet.geometry("600x400")
        app_wallet.title('Wallet')
        app_wallet.after(250, lambda : app_wallet.iconbitmap("assets\\icon.ico"))
        app_wallet.grab_set()

        img1=ImageTk.PhotoImage(Image.open("./assets/pattern.jpg"))
        l1=ctk.CTkLabel(master=app_wallet,image=img1)
        l1.pack()

        #creating custom frame
        frame=ctk.CTkFrame(master=l1, width=320, height=250, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        h,w = 20,20

        img2=ctk.CTkImage(Image.open("./assets/back.png").resize((h,w), Image.ANTIALIAS))
        button2= ctk.CTkButton(master=frame, image=img2, text="", width=h, height=w, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF', command=lambda : back_button(app_main, app_wallet))
        button2.place(x=25, y=20)

        l2=ctk.CTkLabel(master=frame, text="Available balance :",font=('Century Gothic',20))
        l2.place(x=60, y=60)
        l3=ctk.CTkLabel(master=frame, text="Rs XX, XXX",font=('Century Gothic',30))
        l3.place(x=85, y=90)

        button1 = ctk.CTkButton(master=frame, width=220, text="Add money", command=lambda : self.add_money_button(app_wallet), corner_radius=6)
        button1.place(x=50, y=150)

        l3.bind("<Enter>", command = lambda event : (l3.configure(text=f"Rs {int((self.bal%100000)/10000)}{int((self.bal%10000)/1000)}, {int((self.bal%1000)/100)}{int((self.bal%100)/10)}{int((self.bal%10))}"),
                                                            l3.lift()))
        l3.bind("<Leave>", command = lambda event : (l3.configure(text="Rs XX, XXX"),
                                                            button1.lift()))

        app_wallet.protocol("WM_DELETE_WINDOW", close_wm)

    def add_money_button(self, app_wallet):
        credit = ctk.CTkInputDialog(text="Enter amount : ", title="Add money")
        credit.after(250, lambda : credit.iconbitmap("assets\\icon.ico"))
        # credit.iconbitmap("assets\\icon.ico")
        amount = credit.get_input()

        try: 
            added = self.wallet1.credit(int(amount))

            if added:
                self.bal += int(amount)
                msg1 = CTkMessagebox(title="Transaction successful", message=f"Rs {amount} added !", master = app_wallet, justify = "center",
                    icon="check")
                msg1.after(250, lambda : msg1.iconbitmap("assets\\icon.ico"))
                
            else:
                msg1 = CTkMessagebox(title="Transaction failed", message=f"Minimum deposit : Rs 100", master = app_wallet, justify = "center",
                    icon="info")
                msg1.after(250, lambda : msg1.iconbitmap("assets\\icon.ico"))

        except:
            msg1 = CTkMessagebox(title="Error", message="Enter a valid number !", master = app_wallet, justify = "center", icon="cancel")
            msg1.after(250, lambda : msg1.iconbitmap("assets\\icon.ico"))

def main_page():
    app_main = ctk.CTkToplevel(app)  #creating cutstom tkinter window
    app_main.resizable(False, False)
    app_main.geometry("600x400")
    app_main.title('E-Ticket')
    app_main.after(250, lambda : app_main.iconbitmap("assets\\icon.ico"))
    app_main.grab_set()

    img1=ImageTk.PhotoImage(Image.open("./assets/pattern.jpg"))
    l1=ctk.CTkLabel(master=app_main,image=img1)
    l1.pack()

    #creating custom frame
    frame=ctk.CTkFrame(master=l1, width=230, height=345, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2=ctk.CTkLabel(master=frame, text="E-Ticket",font=('Century Gothic',30))
    l2.place(x=60, y=40)

    h, w = 60, 60

    img1=ctk.CTkImage(Image.open("./assets/booking.png").resize((h,w), Image.ANTIALIAS))
    img2=ctk.CTkImage(Image.open("./assets/train.png").resize((h,w), Image.ANTIALIAS))
    img3=ctk.CTkImage(Image.open("./assets/station.png").resize((h,w), Image.ANTIALIAS))
    img4=ctk.CTkImage(Image.open("./assets/ticket.png").resize((h,w), Image.ANTIALIAS))
    img5=ctk.CTkImage(Image.open("./assets/wallet.png").resize((h,w), Image.ANTIALIAS))
    img6=ctk.CTkImage(Image.open("./assets/logout.png").resize((h,w), Image.ANTIALIAS))

    button1= ctk.CTkButton(master=frame, image=img1, text="", width=h, height=w, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF', command=lambda : book_page_invoke(app_main))
    button1.place(x=50, y=100)

    l3=ctk.CTkLabel(master=frame, text="", font=('Century Gothic',15), corner_radius=6, bg_color="darkslategray")
    l3.place(x=80, y=130)
    button1.lift() 

    button2= ctk.CTkButton(master=frame, image=img2, text="", width=h, height=w, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF', command=lambda : train_page_invoke(app_main))
    button2.place(x=120, y=100)

    l4=ctk.CTkLabel(master=frame, text="", font=('Century Gothic',15), corner_radius=6, bg_color="darkslategray")
    l4.place(x=150, y=130)
    button2.lift() 

    button3= ctk.CTkButton(master=frame, image=img3, text="", width=h, height=w, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF', command=lambda : station_page_invoke(app_main))
    button3.place(x=50, y=170)

    l5=ctk.CTkLabel(master=frame, text="", font=('Century Gothic',15), corner_radius=6, bg_color="darkslategray")
    l5.place(x=80, y=200)
    button3.lift() 

    button4= ctk.CTkButton(master=frame, image=img4, text="", width=h, height=w, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF', command=lambda : show_page(app_main))
    button4.place(x=120, y=170)

    l6=ctk.CTkLabel(master=frame, text="", font=('Century Gothic',15), corner_radius=6, bg_color="darkslategray")
    l6.place(x=150, y=200)
    button4.lift() 

    button5= ctk.CTkButton(master=frame, image=img5, text="", width=h, height=w, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF', command=lambda : wallet_page_invoke(app_main))
    button5.place(x=50, y=240)

    l7=ctk.CTkLabel(master=frame, text="", font=('Century Gothic',15), corner_radius=6, bg_color="darkslategray")
    l7.place(x=80, y=270)
    button5.lift()

    button6= ctk.CTkButton(master=frame, image=img6, text="", width=h, height=w, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF', command=lambda : log_in_invoke_function(app_main))
    button6.place(x=120, y=240)

    l8=ctk.CTkLabel(master=frame, text="", font=('Century Gothic',15), corner_radius=6, bg_color="darkslategray")
    l8.place(x=150, y=270)
    button6.lift()

    
    button1.bind("<Enter>", command = lambda event : (l3.configure(text="Book\nticket"),
                                                        l3.lift()))
    button1.bind("<Leave>", command = lambda event : (l3.configure(text=""),
                                                        button1.lift()))
    
    button2.bind("<Enter>", command = lambda event : (l4.configure(text="Search\ntrains"),
                                                        l4.lift()))
    button2.bind("<Leave>", command = lambda event : (l4.configure(text=""),
                                                        button2.lift()))
    
    button3.bind("<Enter>", command = lambda event : (l5.configure(text="Search\nstations"),
                                                        l5.lift()))
    button3.bind("<Leave>", command = lambda event : (l5.configure(text=""),
                                                        button3.lift()))
    
    button4.bind("<Enter>", command = lambda event : (l6.configure(text="Show\ntickets"),
                                                        l6.lift()))
    button4.bind("<Leave>", command = lambda event : (l6.configure(text=""),
                                                        button4.lift()))
    
    button5.bind("<Enter>", command = lambda event : (l7.configure(text="Wallet"),
                                                        l7.lift()))
    button5.bind("<Leave>", command = lambda event : (l7.configure(text=""),
                                                        button5.lift()))
    
    button6.bind("<Enter>", command = lambda event : (l8.configure(text="Log out"),
                                                        l8.lift()))
    button6.bind("<Leave>", command = lambda event : (l8.configure(text=""),
                                                        button6.lift()))

    app_main.protocol("WM_DELETE_WINDOW", close_wm)

if __name__ == "__main__":
    login_page()
    # signup_page()
