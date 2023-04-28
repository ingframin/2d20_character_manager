import tkinter as tk
from tkinter import ttk
from start_screen import *

class CharacterGeneratorApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Mutant Chronicles 3E Character generator")
        icon = tk.PhotoImage(file = 'icon.png')
        self.root.wm_iconphoto(False, icon)
        self.root.geometry('1280x720+10+10')
        self.start_s = StartScreen(self.root)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    capp = CharacterGeneratorApp()
    capp.run()