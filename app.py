import tkinter 
from tkinter import ttk, RIGHT
from workspace import Workspace 
from PIL import ImageTk, Image
import os


def demo():
    root = tkinter.Tk()
    root.title("Motion Planning")
    universal_height = 1000

    nb = ttk.Notebook(root)
    

    # adding Frames as pages for the ttk.Notebook
    # first page, which would get widgets gridded into it
    page1 = ttk.Frame(nb, width= 1080,height = universal_height)
    # second page
    page2 = ttk.Frame(nb,width = 1080,height = universal_height)

    nb.add(page1, text='Workspace')
    nb.add(page2, text='Configspace')
    nb.grid(column=2)

    workspace = Workspace("./resources/robot_BW_small.bmp", "./resources/Room_BW_small.bmp", page1 )
    workspace.drawRobot(0,0)
    def callback(event):
        print ("clicked at", event.x, event.y)
        workspace.drawRobot(event.x,event.y)
        print(workspace.currentPos)
    
    workspace.label.bind("<Button-1>", callback)

    def set_init():
        workspace.setCurrentPosAsInit
    setInitButton = ttk.Button(page1, text = 'Set Init',command = set_init)
    setInitButton.pack(side=tkinter.RIGHT)

    def set_goal():
        workspace.setCurrentPosAsGoal
    setGoalButton = ttk.Button(page1, text = 'Set Goal',command = set_goal)
    setGoalButton.pack(side=tkinter.RIGHT)


    root.mainloop()


if __name__ == "__main__":
    demo()
