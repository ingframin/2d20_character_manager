import tkinter as tk
import tkinter.ttk as ttk
from decision1 import *

character = dict()
character["Attributes"] = {"Agility":5,"Awareness":5,"Coordination":5,"Intelligence":5,"Mental":5,"Personality":5,"Physique":5,"Strength":5}

root = tk.Tk()
root.title("Mutant Chronicles Character Generator")

d1 = Decision1(root)
button = tk.Button(d1.frame,text="Ok")
button.grid(row=0,column=1)

if __name__=='__main__':
    root.mainloop()