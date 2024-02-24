from tkinter import *
from tkinter import messagebox
import os
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Programming is fun and challenging.",
    "Artificial Intelligence is shaping the future.",
    "Keep calm and code on.",
]

encrypted_message = ""
decrypted_message = ""
password = ""  # Initialize password variable

def encryption(msg, sentences):
    global encrypted_message
    randsen = random.choice(sentences)
    encrypted_message = randsen
    return randsen


def decryption(decmsg):
    global encrypted_message, decrypted_message
    if decmsg.strip() == encrypted_message.strip():
        decrypted_message = message
    else:
        decrypted_message = "Decryption failed."
    return decrypted_message

def decrypt():
    entered_password = code.get()

    if entered_password == password:
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        decmsg = text1.get(1.0, END)
       
        decrypted_message = decryption(decmsg) 

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypted_message)

    elif entered_password == "":
        messagebox.showerror("Decryption", "Enter Password")

    else:
        messagebox.showerror("Decryption", "Invalid Password")

def encrypt():
    entered_password = code.get()

    if entered_password == password:
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")
        global message
        message = text1.get(1.0, END)
        
        encrypted_message = encryption(message, sentences) 
        
        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypted_message)
        
    elif entered_password == "":
        messagebox.showerror("Encryption", "Enter Password")

    else:
        messagebox.showerror("Encryption", "Invalid Password") 
    
def set_password():
    global password
    new_password = new_password_entry.get()
    if new_password:
        password = new_password
        messagebox.showinfo("Password Set", "Password has been set successfully.")
        set_password_window.destroy()
    else:
        messagebox.showerror("Password Set", "Please enter a valid password.")



def show_set_password_window():
    global set_password_window
    set_password_window = Toplevel(screen)
    set_password_window.title("Set Password")
    set_password_window.geometry("300x100")

    Label(set_password_window, text="Enter New Password:").pack()
    global new_password_entry
    new_password_entry = Entry(set_password_window, show="*")
    new_password_entry.pack()
    Button(set_password_window, text="Set Password", command=set_password).pack()



def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")

    # icon
    image_icon = PhotoImage(file="keys.png")
    screen.iconphoto(False, image_icon)
    screen.title("PctApp")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="Enter text for encryption and decryption", fg="black", font=("calbri", 13)).place(x=10, y=10)
    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calbri", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)
    Button(text="Set Password", height="2", width=50, bg="#ffcc00", fg="white", bd=0, command=show_set_password_window).place(x=10, y=350)
    
    screen.mainloop()

main_screen()
