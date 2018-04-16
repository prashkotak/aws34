from tkinter import  *
from tkinter import ttk
from tkinter import filedialog


def callback():
    print("Clicked")

def source_button():
    filename = filedialog.askdirectory()
    print(filename)
    return filename


root = Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

label_1 = Label(root,text = "Source Path")
label_1 = Label(root,text= "Destination Path")

#Label(root, text="Please Select the File to Copy").pack()

button1 = ttk.Button(topFrame,text ="Source" )
#button1.grid(row=0, sticky=E)
button1.pack(side=LEFT)
button1.config(command = source_button)

button2 = ttk.Button(topFrame,text ="Destination" )
#button2.grid(row=1, sticky=E)
button2.pack(side=LEFT)
button2.config(command = source_button)

button3 = ttk.Button(bottomFrame,text ="Copy-Directory" )
button3.pack(side=BOTTOM)
button3.config(command = source_button)



root.mainloop()