from tkinter import*
window=Tk()
window.title("Checkbutton Demo")

c1=Checkbutton(window,text="Reading",fg="red",bg="yellow")
c1.pack()
c2=Checkbutton(window,text="Writing",fg="red",bg="yellow")
c2.pack()
c3=Checkbutton(window,text="Running",fg="red",bg="yellow")
c3.pack()

window.minsize(400,400)
window.maxsize(550,550)
window.mainloop()




