from tkinter import *
import math
import tkinter.messagebox


root = Tk()
root.title("scientific calculator")
root.configure(background="powder bleu")
root.resizable(width=False,height=False)
root.geometry("485x568+0+0")

calculatrice=Frame(root)
calculatrice.grid()

menubar = Menu(calculatrice)
filemenu = Menu(menubar,tearoff=0)

menubar.add_cascade(label="fichier",menu=filemenu)
filemenu.add_comande(Label="standard")
filemenu.add_comande(Label="scientifique")
filemenu.add_separator()
filemenu.add_command(label="quitter")

root.config(menu=menubar)
root.mainloop()