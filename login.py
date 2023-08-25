import tkinter as tk
from pathlib import Path
import tkinter.messagebox as tkmb
import turtle
import main

class loginApp():
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def login(self):

        if username.get() == self.username and password.get() == self.password:
            window.destroy()
            main.front()
        elif username.get() == self.username and password.get() != self.password:
            tkmb.showwarning(title='mot de passe éronné',message='Verifier votre mot de passe')
        elif username.get() != self.username and password.get() == self.password:
            tkmb.showwarning(title='Erreur identifiant',message='Veuillez verfiez votre identfiant')
        else:
            tkmb.showerror(title="Erreur d'authentification",message="erreur sur l'identifant et le mot de passe")
        

ASSETS_PATH = Path(__file__).resolve().parent / "assets"
window = tk.Tk()
logo = tk.PhotoImage(file=ASSETS_PATH / "iconbitmap.gif")
window.call('wm', 'iconphoto', window._w, logo)
window.title("Lorem Lorem")

window.geometry("862x519")
window.configure(bg="#3A7FF6")
canvas = tk.Canvas(
    window, bg="#3A7FF6", height=541, width=862,
    bd=0, highlightthickness=0)
canvas.place(x=0, y=0)
# canvas.create_rectangle(431, 0, 431 + 431, 0 + 519, fill="#FCFCFC", outline="")
canvas.create_rectangle(431, 0, 870,519, fill="#FCFCFC", outline="")

username = tk.Entry(bd=0, bg="#F6F7F9",fg="#000716",  highlightthickness=0)
username.place(x=490.0, y=176, width=321.0, height=35)
username.focus()

password = tk.Entry(bd=0, bg="#F6F7F9", fg="#000716",show="•",highlightthickness=0)
password.place(x=490.0, y=254, width=321.0, height=35)


canvas.create_text(
    490.0, 156.0, text="Username", fill="#515486",
    font=("Arial-BoldMT", int(13.0)), anchor="w")
canvas.create_text(
    490.0, 234.5, text="Password", fill="#515486",
    font=("Arial-BoldMT", int(13.0)), anchor="w")

connex = loginApp("C","n")
login = tk.Button(bd=0,text="LOGIN" ,bg="#318de2", fg="#ffffff",font=("Arial",12,"bold italic"),  highlightthickness=0,command=connex.login)
login.place(x=490.0, y=300+25, width=321.0, height=35)


title = tk.Label(
    text="Welcome to our Libary", bg="#3A7FF6",
    fg="white",justify="left", font=("Arial-BoldMT", int(20.0)))
title.place(x=20.0, y=120.0)


def scroll_title():
    text = title["text"]
    text1 = ""
    for i in text:
        text1 += i
        title["text"] = text1
        title.update()
        window.after(100)
# canvas.create_rectangle(25, 160, 250, 165, fill="#FCFCFC", outline="")
scroll_title()



canvas2 = tk.Canvas(
    window, bg="#3A7FF6", height=20, width=300,
    bd=0, highlightthickness=0, relief="ridge")
t = turtle.RawTurtle(canvas2)
t.getscreen().bgcolor("#3A7FF6")
canvas2.place(x=12,y=156)
t.hideturtle()
# t.shape("circle")
t.width(4)
t.color("#fff")
t.penup()
t.goto(-140, 1)
t.pendown()
count = 0


def slide():
    global count
    t.forward(10)
    count +=1
    if count < 550:
        canvas.after(10,slide)
slide()
window.mainloop()
