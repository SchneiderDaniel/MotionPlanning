
from tkinter import ttk

def setBackgroundColor(frame, color):
    style = ttk.Style()     # Create style
    style.configure("A.TFrame", background=color) # Set bg color
    frame.config(style='A.TFrame')    # Apply style to widget
