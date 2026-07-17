from tkinter import*
root=Tk()
root.title("Check button demo")

c1=Checkbutton(root,text="Reading",bg="blue",fg="red")
c1.pack()
c2=Checkbutton(root,text="writing",bg="blue",fg="red")
c2.pack()
c3=Checkbutton(root,text="Running",bg="blue",fg="red")
c3.pack()
c4=Checkbutton(root,text="Cooking",bg="blue",fg="red")
c4.pack()

root.minsize(500,500)
root.maxsize(500,500)
root.mainloop()