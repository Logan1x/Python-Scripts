import os
import tkinter


root = tkinter.Tk()
root.geometry('1250x700')


# General Function:


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


# Defining the create function:

def create():
    def sub_create():
        def sub1():
            def sub2():
                f1.destroy()
            b = TextArea.get("1.0", 'end')
            if(b != '0'):
                f.write(b)
                f.write("\n")
            f2.destroy()
            f1 = tkinter.Frame(bg="#CCCCFF")
            f1.pack(fill="both", expand="true")
            l1 = tkinter.Label(f1, text="Congratulations! Your Entry Is Made.",
                               bg="#330033", fg="#FFFFFF", relief="groove", pady=30, font=16)
            l1.pack(fill="x", expand="true")
            b1 = tkinter.Button(f1, text="Return To MainMenu", bg="#FFFFFF", fg="blue",
                                relief="groove", command=combine_funcs(sub2, start), height=2, width=25)
            b1.pack(side="right")
        a = e.get()
        a = a.upper()
        f1.destroy()
        f = open(a, "w")
        f2 = tkinter.Frame(bg="#CCCCFF")
        f2.pack(fill="both", expand="true")
        l1 = tkinter.Label(f2, text="Make An Entry:\n\nExample: Item1 Rs amount\nItem2 Rs amount",
                           bg="#FFFFFF", fg="#680000", relief="groove", anchor="n", pady=50, font=25)
        l1.pack(fill="x", expand="true")
        TextArea = tkinter.Text(f2)
        ScrollBar = tkinter.Scrollbar(f2, bg="white")
        ScrollBar.config(command=TextArea.yview)
        TextArea.config(yscrollcommand=ScrollBar.set)
        ScrollBar.pack(side="right", fill="y")
        TextArea.pack(fill="x")
        b1 = tkinter.Button(f2, text="Submit", bg="#FFFFFF",
                            fg="blue", relief="groove", command=sub1)
        b1.pack()
    frame.destroy()
    f1 = tkinter.Frame(bg="#CCCCFF")
    f1.pack(fill="both", expand="true")
    l1 = tkinter.Label(f1, text="Welcome To Expense Manager",
                       bg="#330033", fg="#FFFFFF", relief="groove", pady=30, font=16)
    l1.pack(fill="x", expand="true", anchor="n")
    l1 = tkinter.Label(f1, text="Enter Date:", bg="#330033",
                       fg="#FFFFFF", relief="groove", font=9, padx=50)
    l1.place(relx=0.35, rely=0.5)
    e = tkinter.Entry(f1)
    e.place(relx=0.52, rely=0.5)
    b1 = tkinter.Button(f1, text="Make Entry", bg="#9999FF", fg="#660099",
                        relief="groove", command=sub_create, height=2, width=10)
    b1.place(relx=0.45, rely=0.56)


# Defining the get function:

def get():
    def sub_get():
        def sub2():
            f2.destroy()
        a = e.get()
        a = a.upper()
        f1.destroy()
        f = open(a, 'r')
        f2 = tkinter.Frame()
        f2.pack(fill="both", expand="true")
        l1 = tkinter.Label(f2, text="Your Entries For The Date "+a+" Are: ",
                           bg="#FFFFFF", fg="#680000", relief="groove", anchor="center", pady=50)
        l1.pack(fill="x", expand="true")
        TextArea = tkinter.Text(f2)
        ScrollBar = tkinter.Scrollbar(f2)
        ScrollBar.config(command=TextArea.yview)
        ScrollBar.pack(side="right", fill="y")
        TextArea.insert('insert', f.read())
        TextArea.config(yscrollcommand=ScrollBar.set, state="disabled")
        TextArea.pack(fill="both", expand="true")
        b1 = tkinter.Button(f2, text="Return To MainMenu", bg="#FFFFFF", fg="blue",
                            relief="groove", command=combine_funcs(sub2, start), height=2, width=25)
        b1.pack(side="right")
    frame.destroy()
    f1 = tkinter.Frame(bg="#CCCCFF")
    f1.pack(fill="both", expand="true")
    l1 = tkinter.Label(f1, text="Welcome To Expense Manager",
                       bg="#330033", fg="#FFFFFF", relief="groove", pady=30, font=16)
    l1.pack(fill="x", expand="true", anchor="n")
    l1 = tkinter.Label(f1, text="Enter Date:", bg="#330033",
                       fg="#FFFFFF", relief="groove", font=9, padx=50)
    l1.place(relx=0.35, rely=0.5)
    e = tkinter.Entry(f1)
    e.place(relx=0.52, rely=0.5)
    b1 = tkinter.Button(f1, text="Get Entry", bg="#9999FF", fg="#660099",
                        relief="groove", command=sub_get, height=2, width=10)
    b1.place(relx=0.45, rely=0.56)

# Defining the get entry by month function:


def getm():
    def sub_getm():
        def sub2():
            f2.destroy()
        a = e.get()
        a = a.upper()
        f1.destroy()
        f2 = tkinter.Frame()
        f2.pack(fill="both", expand="true")
        l1 = tkinter.Label(f2, text="Your Entries For The Month Are: ",
                           bg="#FFFFFF", fg="#680000", relief="groove", anchor="center", pady=50)
        l1.pack(fill="x", expand="true")
        TextArea = tkinter.Text(f2)
        ScrollBar = tkinter.Scrollbar(f2)
        ScrollBar.config(command=TextArea.yview)
        ScrollBar.pack(side="right", fill="y")
        for i in range(1, 32):
            try:
                f = open(str(i)+' '+a, 'r')
            except IOError:
                continue
            TextArea.insert('insert', "\n"+str(i)+' '+a+": \n\n"+f.read())
        TextArea.config(yscrollcommand=ScrollBar.set, state="disabled")
        TextArea.pack(fill="both", expand="true")
        b1 = tkinter.Button(f2, text="Return To MainMenu", bg="#FFFFFF", fg="blue",
                            relief="groove", command=combine_funcs(sub2, start), height=2, width=25)
        b1.pack(side="right")
    frame.destroy()
    f1 = tkinter.Frame(bg="#CCCCFF")
    f1.pack(fill="both", expand="true")
    l1 = tkinter.Label(f1, text="Welcome To Expense Manager",
                       bg="#330033", fg="#FFFFFF", relief="groove", pady=30, font=16)
    l1.pack(fill="x", expand="true", anchor="n")
    l1 = tkinter.Label(f1, text="Enter Month And Year:", bg="#330033",
                       fg="#FFFFFF", relief="groove", font=9, padx=50)
    l1.place(relx=0.3, rely=0.5)
    e = tkinter.Entry(f1)
    e.place(relx=0.52, rely=0.5)
    b1 = tkinter.Button(f1, text="Get Entry", bg="#9999FF", fg="#660099",
                        relief="groove", command=sub_getm, height=2, width=10)
    b1.place(relx=0.47, rely=0.56)


# Get Total Expense By Date:


def Sum():
    def sub_Sum():
        def sub2():
            f2.destroy()
        t = e.get()
        t = t.upper()
        try:
            f = open(t, 'r')
            a = f.readlines()
            c = 0
            for i in range(0, len(a)):
                b = ''
                for j in range(len(a[i])-1, 0, -1):
                    if(a[i][j] != ' ' and a[i][j] >= '0' and a[i][j] <= '9'):
                        b = b+a[i][j]
                    if(a[i][j] >= '9'):
                        break
                if(b != ''):
                    c = c+int(b[::-1])
            f1.destroy()
            f2 = tkinter.Frame()
            f2.pack(fill="both", expand="true")
            l1 = tkinter.Label(f2, text="Total Expenses On "+t+" Are: \nRs "+str(
                c), bg="#FFFFFF", fg="#680000", relief="groove", anchor="center", pady=50, font=50)
            l1.pack(fill="both", expand="true")
        except IOError:
            l1 = tkinter.Label(f2, text="No Such Entry Is Made "+t+" Are: \nRs "+str(
                c), bg="#FFFFFF", fg="#680000", relief="groove", anchor="center", pady=50, font=50)
            l1.pack(fill="both", expand="true")
        b1 = tkinter.Button(f2, text="Return To MainMenu", bg="#FFFFFF", fg="blue",
                            relief="groove", command=combine_funcs(sub2, start), height=2, width=25)
        b1.pack(side="right")
    frame.destroy()
    f1 = tkinter.Frame(bg="#CCCCFF")
    f1.pack(fill="both", expand="true")
    l1 = tkinter.Label(f1, text="Welcome To Expense Manager",
                       bg="#330033", fg="#FFFFFF", relief="groove", pady=30, font=16)
    l1.pack(fill="x", expand="true", anchor="n")
    l1 = tkinter.Label(f1, text="Enter Date:", bg="#330033",
                       fg="#FFFFFF", relief="groove", font=9, padx=50)
    l1.place(relx=0.35, rely=0.5)
    e = tkinter.Entry(f1)
    e.place(relx=0.52, rely=0.5)
    b1 = tkinter.Button(f1, text="Get Expenses", bg="#9999FF", fg="#660099",
                        relief="groove", command=sub_Sum, height=2, width=10)
    b1.place(relx=0.47, rely=0.56)

# Defining Get total expense in a month:


def Summ():
    def sub_Summ():
        def sub2():
            f2.destroy()
        a = e.get()
        a = a.upper()
        c = 0
        for i in range(1, 32):
            try:
                f = open(str(i)+' '+a, 'r')
                t = f.readlines()
                for i in range(0, len(t)):
                    b = ''
                    for j in range(len(t[i])-1, 0, -1):
                        if(t[i][j] != ' ' and t[i][j] >= '0' and t[i][j] <= '9'):
                            b = b+t[i][j]
                    if(b != ''):
                        c = c+int(b[::-1])
            except IOError:
                continue
        f1.destroy()
        f2 = tkinter.Frame()
        f2.pack(fill="both", expand="true")
        l1 = tkinter.Label(f2, text="Total Expenses In "+a+" Are: \nRs "+str(
            c), bg="#FFFFFF", fg="#680000", relief="groove", anchor="center", pady=50, font=50)
        l1.pack(fill="both", expand="true")
        b1 = tkinter.Button(f2, text="Return To MainMenu", bg="#FFFFFF", fg="blue",
                            relief="groove", command=combine_funcs(sub2, start), height=2, width=25)
        b1.pack(side="right")
    frame.destroy()
    f1 = tkinter.Frame(bg="#CCCCFF")
    f1.pack(fill="both", expand="true")
    l1 = tkinter.Label(f1, text="Welcome To Expense Manager",
                       bg="#330033", fg="#FFFFFF", relief="groove", pady=30, font=16)
    l1.pack(fill="x", expand="true", anchor="n")
    l1 = tkinter.Label(f1, text="Enter Month And Year:", bg="#330033",
                       fg="#FFFFFF", relief="groove", font=9, padx=50)
    l1.place(relx=0.3, rely=0.5)
    e = tkinter.Entry(f1)
    e.place(relx=0.52, rely=0.5)
    b1 = tkinter.Button(f1, text="Get Expenses", bg="#9999FF", fg="#660099",
                        relief="groove", command=sub_Summ, height=2, width=10)
    b1.place(relx=0.47, rely=0.56)


# Defining Add to entry:

def add():
    def sub_add():
        def sub1():
            def sub2():
                f1.destroy()
            b = TextArea.get("1.0", 'end')
            if(b != '0'):
                f.write(b)
                f.write("\n")
            f2.destroy()
            f1 = tkinter.Frame(bg="#CCCCFF")
            f1.pack(fill="both", expand="true")
            l1 = tkinter.Label(f1, text="Congratulations! Your Entry Is Made.",
                               bg="#330033", fg="#FFFFFF", relief="groove", pady=30, font=16)
            l1.pack(fill="x", expand="true")
            b1 = tkinter.Button(f1, text="Return To MainMenu", bg="#FFFFFF", fg="blue",
                                relief="groove", command=combine_funcs(sub2, start), height=2, width=25)
            b1.pack(side="right")
        a = e.get()
        a = a.upper()
        f1.destroy()
        f = open(a, "a")
        f2 = tkinter.Frame(bg="#CCCCFF")
        f2.pack(fill="both", expand="true")
        l1 = tkinter.Label(f2, text="Make An Entry:\n\nExample: Item1 Rs amount\nItem2 Rs amount",
                           bg="#FFFFFF", fg="#680000", relief="groove", anchor="n", pady=50, font=25)
        l1.pack(fill="x", expand="true")
        TextArea = tkinter.Text(f2)
        ScrollBar = tkinter.Scrollbar(f2, bg="white")
        ScrollBar.config(command=TextArea.yview)
        TextArea.config(yscrollcommand=ScrollBar.set)
        ScrollBar.pack(side="right", fill="y")
        TextArea.pack(fill="x")
        b1 = tkinter.Button(f2, text="Submit", bg="#FFFFFF",
                            fg="blue", relief="groove", command=sub1)
        b1.pack()
    frame.destroy()
    f1 = tkinter.Frame(bg="#CCCCFF")
    f1.pack(fill="both", expand="true")
    l1 = tkinter.Label(f1, text="Welcome To Expense Manager",
                       bg="#330033", fg="#FFFFFF", relief="groove", pady=30, font=16)
    l1.pack(fill="x", expand="true", anchor="n")
    l1 = tkinter.Label(f1, text="Enter Date:", bg="#330033",
                       fg="#FFFFFF", relief="groove", font=9, padx=50)
    l1.place(relx=0.35, rely=0.5)
    e = tkinter.Entry(f1)
    e.place(relx=0.52, rely=0.5)
    b1 = tkinter.Button(f1, text="Make Entry", bg="#9999FF", fg="#660099",
                        relief="groove", command=sub_add, height=2, width=10)
    b1.place(relx=0.45, rely=0.56)

# Defining Delete Existing Entry:


def delete():

    def delete(x): return os.remove(x)

    def sub_delete():
        def sub2():
            f2.destroy()
        a = e.get()
        a = a.upper()
        delete(a)
        f1.destroy()
        f2 = tkinter.Frame(bg="#CCCCFF")
        f2.pack(fill="both", expand="true")
        l1 = tkinter.Label(f2, text="Congratulations! Your Entry Is Deleted.",
                           bg="#330033", fg="#FFFFFF", relief="groove", pady=30, font=16)
        l1.pack(fill="x", expand="true")
        b1 = tkinter.Button(f2, text="Return To MainMenu", bg="#FFFFFF", fg="blue",
                            relief="groove", command=combine_funcs(sub2, start), height=2, width=25)
        b1.pack(side="right")
    frame.destroy()
    f1 = tkinter.Frame(bg="#CCCCFF")
    f1.pack(fill="both", expand="true")
    l1 = tkinter.Label(f1, text="Welcome To Expense Manager",
                       bg="#330033", fg="#FFFFFF", relief="groove", pady=30, font=16)
    l1.pack(fill="x", expand="true", anchor="n")
    l1 = tkinter.Label(f1, text="Enter Date:", bg="#330033",
                       fg="#FFFFFF", relief="groove", font=9, padx=50)
    l1.place(relx=0.35, rely=0.5)
    e = tkinter.Entry(f1)
    e.place(relx=0.52, rely=0.5)
    b1 = tkinter.Button(f1, text="Delete", bg="#9999FF", fg="#660099",
                        relief="groove", command=sub_delete, height=2, width=10)
    b1.place(relx=0.47, rely=0.56)


def start():
    global frame
    frame = tkinter.Frame(bg="#CCCCFF")
    frame.pack(fill="both", expand="true",)
    l1 = tkinter.Label(frame, text="Welcome To Expense Manager",
                       bg="#330033", fg="#FFFFFF", relief="groove", pady=30, font=16)
    l1.pack(fill="x", expand="true", anchor="n")
    l1 = tkinter.Label(frame, text="Press To Create A new Entry", bg="#330066",
                       fg="#66FFFF", relief="groove", pady=15, font=16, padx=16)
    l1.place(relx=0.2, rely=0.2, anchor="n")
    b1 = tkinter.Button(frame, text="Create Entry Sheet", bg="#9999FF", fg="#660099",
                        relief="solid", command=create, font=11, pady=16, cursor="dot")
    b1.place(relx=0.2, rely=0.3, anchor="n")
    l1 = tkinter.Label(frame, text="Press To Get Entry By Date", bg="#330066",
                       fg="#66FFFF", relief="groove", pady=15, font=16, padx=16)
    l1.place(relx=0.4, rely=0.2, anchor="n")
    b1 = tkinter.Button(frame, text="Get Entry Sheet", bg="#9999FF", fg="#660099",
                        relief="solid", command=get, font=11, pady=16, cursor="dot")
    b1.place(relx=0.4, rely=0.3, anchor="n")
    l1 = tkinter.Label(frame, text="Press To Get Entry By Month", bg="#330066",
                       fg="#66FFFF", relief="groove", pady=15, font=16, padx=7)
    l1.place(relx=0.6, rely=0.2, anchor="n")
    b1 = tkinter.Button(frame, text="Get Monthly Entry Sheet", bg="#9999FF",
                        fg="#660099", relief="solid", command=getm, font=11, pady=16, cursor="dot")
    b1.place(relx=0.6, rely=0.3, anchor="n")
    l1 = tkinter.Label(frame, text="Press To Get Total Expense On Date",
                       bg="#330066", fg="#66FFFF", relief="groove", pady=15, font=16)
    l1.place(relx=0.8, rely=0.2, anchor="n")
    b1 = tkinter.Button(frame, text="Get Total Expense On Date", bg="#9999FF",
                        fg="#660099", relief="solid", command=Sum, font=11, pady=16, cursor="dot")
    b1.place(relx=0.8, rely=0.3, anchor="n")
    l1 = tkinter.Label(frame, text="Press To Get Total Expense In A Month",
                       bg="#330066", fg="#66FFFF", relief="groove", pady=15, font=16)
    l1.place(relx=0.3, rely=0.5, anchor="n")
    b1 = tkinter.Button(frame, text="Get Total Expense", bg="#9999FF", fg="#660099",
                        relief="solid", command=Summ, font=11, pady=16, cursor="dot")
    b1.place(relx=0.3, rely=0.6, anchor="n")
    l1 = tkinter.Label(frame, text="Press To Add To Existing Entry",
                       bg="#330066", fg="#66FFFF", relief="groove", pady=15, font=16)
    l1.place(relx=0.51, rely=0.5, anchor="n")
    b1 = tkinter.Button(frame, text="Add To Entry", bg="#9999FF", fg="#660099",
                        relief="solid", command=add, font=11, pady=16, cursor="dot")
    b1.place(relx=0.51, rely=0.6, anchor="n")
    l1 = tkinter.Label(frame, text="Press To Delete Existing Entry",
                       bg="#330066", fg="#66FFFF", relief="groove", pady=15, font=16)
    l1.place(relx=0.7, rely=0.5, anchor="n")
    b1 = tkinter.Button(frame, text="Delete Entry", bg="#9999FF", fg="#660099",
                        relief="solid", command=delete, font=11, pady=16, cursor="dot")
    b1.place(relx=0.7, rely=0.6, anchor="n")
    l1 = tkinter.Label(frame, text="\u00a9"+" copyright 2016\t\t\t\t\t\t\t\t\t\t\t\t" +
                       "Developed By: Akshit Grover", bg="#330033", fg="#FFFFFF", relief="groove", pady=30, font=16)
    l1.pack(fill="x", expand="true", anchor="s")
    root.mainloop()


start()
