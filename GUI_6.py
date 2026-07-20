from tkinter import*
root=Tk()
root.title("listbox demo")
lb=Listbox(root,fg="red",bg="green")
lb.insert(1,"python")
lb.insert(2,"CPP")
lb.insert(3,"React")
lb.insert(4,"Rust")
lb.pack()
root.minsize(500,500)
root.maxsize(600,600)
root.mainloop()


