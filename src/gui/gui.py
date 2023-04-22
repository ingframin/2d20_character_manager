import tkinter as tk
from tkinter import ttk

class CharacterGeneratorApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Mutant Chronicles 3E Character generator")
        icon = tk.PhotoImage(file = 'icon.png')
        self.root.wm_iconphoto(False, icon)
    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    capp = CharacterGeneratorApp()
    capp.run()