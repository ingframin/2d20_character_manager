import tkinter as tk
from tkinter import ttk

class StartScreen:
    def __init__(self,root) -> None:
        s = ttk.Style()
        s.configure('TFrame',background='black')
        self.frame = ttk.Frame(root,width=1280, height=720,style='TFrame')
        self.frame['padding'] = (5,5,5,5)
        self.logo = tk.PhotoImage(file='logo.png')
        self.logo.configure(width=400,height=200)
        self.logo_lbl = ttk.Label(self.frame)
        self.logo_lbl['image'] = self.logo
        
        self.logo_lbl.pack()
        self.make_buttons()
        self.frame.pack()
    
    def make_buttons(self):
        self.standard_chr_btn = ttk.Button(self.frame,text='Standard Method')
        self.standard_chr_btn.pack()
        self.twelve_pts_btn = ttk.Button(self.frame,text='12 Points')
        self.twelve_pts_btn.pack()
        

        