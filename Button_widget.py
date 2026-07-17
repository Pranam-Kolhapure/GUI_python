from tkinter import*
window=Tk()
window.title("Button widget demo")
b=Button(window,text="click me",fg="red",bg="yellow")
b.pack()
window.minsize(400,400)
window.maxsize(500,500)
window.mainloop()


