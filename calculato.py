from tkinter import*
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        pass
    elif text=="c":
        pass
    else:
        scvalue.set(scvalue.get()+text)
root=Tk()
root.geometry("644x900")
root.title("Calculator by Silent Killer")
root.wm_iconbitmap("1.ico")

Scvalue=StringVar()
Scvalue.set("")
screen=Entry(root,textvar=Scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,padx=10)

f=Frame(root, bg="grey")
b=Button(f,text="9", padx=28,pady=22, font="lucida 35 bold")
b.pack()
f.pack()


root.mainloop()