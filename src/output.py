import tkinter as tk
from tkinter import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()  # Call the __init__ method of tk.Tk to initialize the root window
        
        ## Setting up Initial Things
        self.title("Created by PyLite")
        self.configure(bg="#797D7F")
        self.geometry("500x500")
        
        self.create_widgets()  # Call the method to create widgets

    def create_widgets(self):
        # Create all widgets here
        
        
        RadioButton1 = Checkbutton(self)
        
        RadioButton1.place(x=0,y=0,width="24px",height="24px")
        
        
        CheckBox1 = Checkbutton(self)
        
        CheckBox1.place(x=122,y=160,width="24px",height="24px")
        
        
        Label1 = Label(self,text="Label")
        
        Label1.place(x=160,y=92,width="30px",height="24px")
        

if __name__ == "__main__":
    app = App()
    app.mainloop()  # Start the main loop
