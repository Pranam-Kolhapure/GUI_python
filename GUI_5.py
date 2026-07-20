from tkinter import*
root=Tk()
root.title("Radiobutton demo")
r1=Radiobutton(root,text="male",fg="red",bg="yellow",variable="a",value=1)
r1.pack()
r2=Radiobutton(root,text="female",fg="red",bg="yellow",variable="b",value=2)
r2.pack()
root.minsize(400,400)
root.maxsize(500,500)
root.mainloop()





