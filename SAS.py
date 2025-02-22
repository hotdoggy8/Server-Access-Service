from tkinter import *
from tkinter import ttk
import random
import time

name = None
UsrnameField = None
LWindow = None
SWindow = None
SVWindow = None
MWindow = None
LDWindow = None

def scanv2():
    global SVWindow
    SVWindow.destroy()

def scanv1():
    global SVWindow
    SVWindow = Tk()
    SVWindow.title("Scan Viruses")
    ScanText = Label(SVWindow, text="Scanning Viruses...")
    ScanText.pack()
    Progress = ttk.Progressbar(SVWindow, orient="horizontal", length=200, mode="determinate")
    Progress.pack()
    Progress["value"] = 0
    def scanprogress(value=0):
        global ScanDone
        if Progress["value"] >= 100:
            scanv2()
        if value <= 100:
            Progress["value"] = value
            choice1 = random.randint(0, 1)
            if choice1 == 1:
                choice2 = random.randint(0, 1)
                if choice2 == 1:
                    time.sleep(random.uniform(0.5, 1.0))
            SVWindow.after(10, scanprogress, value + 1)
    scanprogress()

def hackwindow():
    global LDWindow
    LDWindow.destroy()
    HWindow = Tk()
    HWindow.title("Control Panel")
    BrandTxt = Label(HWindow, text="Server Access Service",width=20,height=2,bg="black",fg="green",font=("Times New Roman", 20, "bold"))
    CtrlTxt = Label(HWindow, text="Control Panel",width=25,height=2)
    ScanVirus = Button(HWindow, text = "Scan Viruses", command=scanv1)
    BrandTxt.pack()
    CtrlTxt.pack()
    ScanVirus.pack()

def cntwindow():
    global LDWindow
    MWindow.destroy()
    LDWindow = Tk()
    LDWindow.title("Progress")
    CntText = Label(LDWindow, text="Connecting...")
    Progress = ttk.Progressbar(LDWindow, orient="horizontal", length=200, mode="determinate")
    CntText.pack()
    Progress.pack()
    Progress["value"] = 0
    def connectprogress(value=0):
        if Progress["value"] >= 100:
            hackwindow()
        if value <= 100:
            Progress["value"] = value
            choice1 = random.randint(0, 1)
            if choice1 == 1:
                choice2 = random.randint(0, 1)
                if choice2 == 1:
                    time.sleep(random.uniform(0.5, 1.0))
            LDWindow.after(10, connectprogress, value + 1)
    connectprogress()

def startwindow():
    global name
    global MWindow
    MWindow = Tk()
    MWindow.title("Server information")
    BrandTxt = Label(MWindow, text="Server Access Service",width=20,height=2,bg="black",fg="green",font=("Times New Roman", 20, "bold"))
    UsrText = Label(MWindow, text="You're logged in as: "+name)
    Serverask = Label(MWindow, text="Server address:",width=40,height=2)
    Serveradd = ttk.Combobox(MWindow)
    Serveradd["values"] = ("192.168.1.3", "192.168.3.255", "127.0.0.1")
    Confirm = Button(MWindow, text="Connect", command=cntwindow)
    BrandTxt.pack()
    UsrText.pack()
    Serverask.pack()
    Serveradd.pack()
    Confirm.pack()

def finish():
    global name
    global UsrnameField
    name = UsrnameField.get()
    if LWindow != None:
        if LWindow.winfo_exists() == 1:
            LWindow.destroy()
    elif SWindow != None:
        if SWindow.winfo_exists() == 1:
            SWindow.destroy()
    startwindow()

def login():
    window.destroy()
    global LWindow
    global UsrnameField
    LWindow = Tk()
    LWindow.title("Login")
    BrandTxt = Label(LWindow, text="Server Access Service",width=20,height=2,bg="black",fg="green",font=("Times New Roman", 20, "bold"))
    Text = Label(LWindow, text="Log in", width=20, height=2, font=("Calibri", 20, "bold"))
    Usrname = Label(LWindow, text="Username:")
    UsrnameField = Entry(LWindow)
    Psword = Label(LWindow, text="Password:")
    PswordField = Entry(LWindow, show="*")
    LoginBtn = Button(LWindow, text="Log in", command=finish)
    BrandTxt.pack()
    Text.pack()
    Usrname.pack()
    UsrnameField.pack()
    Psword.pack()
    PswordField.pack()
    LoginBtn.pack()

def signin():
    window.destroy()
    global SWindow
    global UsrnameField
    SWindow = Tk()
    SWindow.title("Register")
    BrandTxt = Label(SWindow, text="Server Access Service",width=20,height=2,bg="black",fg="green",font=("Times New Roman", 20, "bold"))
    Text = Label(SWindow, text="Register", width=20, height=2, font=("Calibri", 20, "bold"))
    Intro = Label(SWindow, text="Create an account.")
    Usrname = Label(SWindow, text="Username:")
    UsrnameField = Entry(SWindow)
    Psword = Label(SWindow, text="Password:")
    PswordField = Entry(SWindow, show="*")
    Ntn = Label(SWindow, text="Nationality:")
    NtnField = ttk.Combobox(SWindow)
    NtnField["values"] = ("English", "Tiếng việt", "日本語", "한국인", "中國人")
    LoginBtn = Button(SWindow, text="Register account", command=finish)
    BrandTxt.pack()
    Text.pack()
    Intro.pack()
    Usrname.pack()
    UsrnameField.pack()
    Psword.pack()
    PswordField.pack()
    Ntn.pack()
    NtnField.pack()
    LoginBtn.pack()

window =  Tk()
window.title("Server Access Service")
BrandTxt = Label(window, text="Server Access Service",width=20,height=2,bg="black",fg="green",font=("Times New Roman", 20, "bold"))
WelcomeTxt = Label(window, text="Welcome, Admin. Login to use this service", width=38, height=2)
LoginBtn = Button(window, text="Log in", command=login)
NoAcc = Label(window, text="No account? Register an account")
SigninBtn = Button(window, text="Register", command=signin)

BrandTxt.pack()
WelcomeTxt.pack()
LoginBtn.pack()
NoAcc.pack()
SigninBtn.pack()
mainloop()
