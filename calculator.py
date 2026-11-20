from tkinter import *
root=Tk()
root.geometry("644x429")
root.title("Basic Calculator")
def result(event):
    global calvalue
    text=event.widget.cget("text")
    if text=="=":
        if calvalue.get().isdigit():
            value=int(calvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                calvalue.set("error")

        calvalue.set(value)        
    elif text=="AC":
        calvalue.set("")
    
    else:
        calvalue.set(calvalue.get() + text)
        
calvalue=StringVar()
calvalue.set("")
screen=Entry(root,textvariable=calvalue,font="comicsansms 19 bold",bg="grey")
screen.pack(fill=X,pady=29,padx=15)

frame=Frame(root,bg="grey")
button=Button(frame,text="1",fg="blue",padx=10,pady=2,font="comicsansms 19 bold")
button.grid(row=1,column=1,padx=5,pady=5)
button.bind("<Button-1>",result)

button=Button(frame,text="2",fg="blue",padx=10,pady=2,font="comicsansms 19 bold")
button.grid(row=1,column=2,padx=5,pady=5)
button.bind("<Button-1>",result)

button=Button(frame,text="3",fg="blue",padx=10,pady=2,font="comicsansms 19 bold")
button.grid(row=1,column=3,padx=5,pady=5)
button.bind("<Button-1>",result)

button=Button(frame,text="4",fg="blue",padx=10,pady=2,font="comicsansms 19 bold")
button.grid(row=2,column=1,padx=5,pady=5)
button.bind("<Button-1>",result)

button=Button(frame,text="5",fg="blue",padx=10,pady=2,font="comicsansms 19 bold")
button.grid(row=2,column=2,padx=5,pady=5)
button.bind("<Button-1>",result)

button=Button(frame,text="6",fg="blue",padx=10,pady=2,font="comicsansms 19 bold")
button.grid(row=2,column=3,padx=5,pady=5)
button.bind("<Button-1>",result)

button=Button(frame,text="7",fg="blue",padx=10,pady=2,font="comicsansms 19 bold")
button.grid(row=3,column=1,padx=5,pady=5)
button.bind("<Button-1>",result)

button=Button(frame,text="8",fg="blue",padx=10,pady=2,font="comicsansms 19 bold")
button.grid(row=3,column=2,padx=5,pady=5)
button.bind("<Button-1>",result)

button=Button(frame,text="9",fg="blue",padx=10,pady=2,font="comicsansms 19 bold")
button.grid(row=3,column=3,padx=5,pady=5)
button.bind("<Button-1>",result)

button=Button(frame,text="0",fg="blue",padx=10,pady=2,font="comicsansms 19 bold")
button.grid(row=4,column=1,padx=5,pady=5)
button.bind("<Button-1>",result)

button=Button(frame,text="+",fg="red",padx=13,pady=2,font="comicsansms 19 bold")
button.grid(row=1,column=4,padx=2,pady=2)
button.bind("<Button-1>",result)

button=Button(frame,text="-",fg="red",padx=16,pady=3,font="comicsansms 19 bold")
button.grid(row=2,column=4,padx=2,pady=2)
button.bind("<Button-1>",result)

button=Button(frame,text="*",fg="red",padx=15,pady=3,font="comicsansms 19 bold")
button.grid(row=3,column=4,padx=2,pady=2)
button.bind("<Button-1>",result)

button=Button(frame,text="/",fg="red",padx=15,pady=2,font="comicsansms 19 bold")
button.grid(row=4,column=2,padx=2,pady=2)
button.bind("<Button-1>",result)

button=Button(frame,text=".",fg="red",padx=16,pady=3,font="comicsansms 19 bold")
button.grid(row=4,column=4,padx=2,pady=2)
button.bind("<Button-1>",result)

button=Button(frame,text="%",fg="red",padx=9,pady=2,font="comicsansms 19 bold")
button.grid(row=4,column=3,padx=2,pady=2)
button.bind("<Button-1>",result)

button=Button(frame,text="=",fg="red",padx=10,pady=5,font="comicsansms 19 bold")
button.grid(row=6,column=1,padx=2,pady=2)
button.bind("<Button-1>",result)

button=Button(frame,text="AC",fg="red",padx=3,pady=5,font="comicsansms 19 bold")
button.grid(row=6,column=4,padx=2,pady=2)
button.bind("<Button-1>",result)

frame.pack()
root.mainloop()