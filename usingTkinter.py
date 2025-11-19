from tkinter import *

mac = Tk()
mac.geometry("420x420")
# To use the geometry, you need to make use of X for Xylem instead of multiplication sign i.e. *
mac.config(background='#5CFCFF')
icon = PhotoImage(file='.vscode/unhcr-255x300.png')
mac.iconphoto(True, icon)
mac.title("Sam's first GUI Program")

mac.mainloop()
