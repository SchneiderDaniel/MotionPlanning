import tkinter 
from tkinter import ttk
from workspace import Workspace 
from PIL import ImageTk, Image
import os


def demo():
    #root = tk.Tk()
    root = tkinter.Tk()

    root.title("Motion Planning")
    universal_height = 606


    



    nb = ttk.Notebook(root)

    # adding Frames as pages for the ttk.Notebook
    # first page, which would get widgets gridded into it
    page1 = ttk.Frame(nb, width= 1080,height = universal_height)
    # second page
    page2 = ttk.Frame(nb,width = 1080,height = universal_height)

    nb.add(page1, text='Workspace')
    nb.add(page2, text='Configspace')

    nb.grid(column=0)

    workspace = Workspace("./resources/robot_BW_small.bmp", "./resources/Room_BW_small.bmp", page1 )

    workspace.drawRobot(500,500)

    # img = ImageTk.PhotoImage(Image.open("./resources/Room_BW_small.bmp"))
    # label1 = ttk.Label(page1, image =img)
    # label1.pack(side = "bottom", fill = "both", expand = "yes")
    root.mainloop()

    # workspace.drawEnvOnCanvas(label1)


    # day_label = ttk.Label(page2, text="Day2:")
    # day_label.pack()
    # day_label.place(x=0, y=30)



    

    # canvas = schedGraphics.Canvas(page1, width=1080, height=universal_height)
    # canvas.create_rectangle(50, 500, 300, 600, fill="red")
    # canvas.grid(column=1, row=0)




    # canvas2 = schedGraphics.Canvas(page2, width=1080, height=universal_height)
    # canvas2.create_rectangle(50, 500, 300, 600, fill="red")
    # canvas2.grid(column=1, row=0)


    root.mainloop()

if __name__ == "__main__":
    demo()