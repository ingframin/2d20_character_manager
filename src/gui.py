from tkinter import *
from tkinter import ttk


class CharGenGUI(Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Mutant Chronicles 3E Character Generator")
        self.geometry("800x720")
        self.main_frame = ttk.Frame(self,padding="3 3 12 12")
        self.main_frame.grid(column=0, row=0, sticky="NWES")
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        # logo
        self.logo = PhotoImage(file='./assets/logo_w800.png',width=800)
        self.logolab = ttk.Label(self.main_frame, image=self.logo)
        self.logolab.grid(row=0,column=0, columnspan=3)
        # buttons
        self.button_std = ttk.Button(self.main_frame, text='Standard Method', command=lambda : print("test"))
        self.button_std.grid(row=1, column=0, ipadx=50, ipady=10)
        self.button_12lp = ttk.Button(self.main_frame, text='12 Life Points', command=lambda : print("test"))
        self.button_12lp.grid(row=1, column=1, ipadx=50, ipady=10)
        self.button_freem = ttk.Button(self.main_frame, text='Free Method', command=lambda : print("test"))
        self.button_freem.grid(row=1, column=2, ipadx=50, ipady=10)

cgg = CharGenGUI()
cgg.mainloop()

# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
#     except ValueError:
#         pass

# root = Tk()
# root.title("Feet to Meters")

# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# feet = StringVar()
# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))

# meters = StringVar()
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# for child in mainframe.winfo_children(): 
#     child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
# root.bind("<Return>", calculate)

# root.mainloop()