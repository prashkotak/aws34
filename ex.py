from tkinter import *
from tkinter import filedialog

root = Tk()
s = StringVar()
d = StringVar()
root.title("Welcome to LikeGeeks app")
root.geometry('350x200')

# lbl = Label(root, text="Source")
# lbl.grid(column=0, row=0)

def source_button():
    filename = filedialog.askdirectory()
    print(filename)
    s.set(filename)
    return filename

def dest_button():
    filename = filedialog.askdirectory()
    print(filename)
    d.set(filename)
    return filename



btn = Button(root, text="Source")
btn.grid(column=0, row=0)
btn.config(width=10, height=1 ,command = source_button)
btn2 = Button(root, text="Destination")
btn2.grid(column=0, row=1)
btn2.config(width=10, height=1,command = dest_button)

btn2 = Button(root, text="Destination")
btn2.grid(column=0, row=1)
btn2.config(width=10, height=1,command = dest_button)


e1 = Entry(root, width=35 , textvariable=s)
e2 = Entry(root, width=35 , textvariable=d)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

#e2.config(width=20, height=1)


#
# from tkinter import *
#
# master = Tk()
# Label(master, text="First Name").grid(row=0)
# Label(master, text="Last Name").grid(row=1)
#
# e1 = Entry(master)
# e2 = Entry(master)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
#
# mainloop( )
#

root.mainloop()